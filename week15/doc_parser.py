import os
import re
import pandas as pd
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.psparser import PSLiteral, PSSyntaxError
from pdfminer.pdftypes import resolve1, PDFObjRef

directory_path = './Admissions_2026'
questionnaire_file = ''

degree_keywords = ['degree', 'diploma', 'transcript']
empty_cols_to_add = ['Academic Work Sample','English Certificate','Declaration','Remarks','Confirmation sent']

def extractApplicantInfo(questionnaire_file):
    data = {}
    with open(questionnaire_file, 'rb') as fp:
        try:
            parser = PDFParser(fp)  # This line has issues when there is a digital signature (hence the try-except)
            doc = PDFDocument(parser)

            # Check if AcroForm exists (if not document is a scan)
            if 'AcroForm' not in resolve1(doc.catalog):
                print("WARNING: Questionnaire is a scan.")
                return {}
            
            fields = resolve1(doc.catalog['AcroForm'])['Fields']
            for f in fields:
                field = resolve1(f)
                name, value = field.get('T'), field.get('V')
                if isinstance(name, PSLiteral):
                    name = name.name
                if isinstance(value, PDFObjRef):
                    value = resolve1(value)
                if isinstance(value, PSLiteral):
                    value = value.name
                if value is not None and not isinstance(value,(str,dict)):
                    value = value.decode('utf-8')
                
                data[name.decode('utf-8')] = value
                for col_to_drop in ['Signature', 'Form of address', 'Date of signature', 'E-mail-Notification', 'Place name']:
                    if col_to_drop in data.keys():
                        del data[col_to_drop]
        except:
            print("WARNING: Cannot handle file with digital signature.")
            return {}
        
    return data

def initializeChecklist(applicant):
    checklist_df = pd.DataFrame()
    checklist_df['Appl. no'] = [applicant.split('_')[0]]
    checklist_df['Last name'] = [applicant.split('_')[-1]]
    checklist_df['First name(s)'] = [' '.join(applicant.split('_')[1:-1])]
    return checklist_df

dir_names = []
# Get directory names
with os.scandir(directory_path) as entries:
    for entry in entries:
        if entry.is_dir():
            dir_names.append(entry.name)

# Get Questionnaire info and fill out checklist
info_df = pd.DataFrame()
full_checklist_df = pd.DataFrame()
for applicant in dir_names:
    print(applicant)
    questionnaire_found = False
    checklist_df = initializeChecklist(applicant)
    with os.scandir(directory_path + '/' + applicant) as entries:
        for entry in entries:
            if entry.is_file():
                if 'questionnaire' in entry.name.lower():
                    questionnaire_found = True
                    questionnaire_file = entry.name
                    applicant_info = extractApplicantInfo(directory_path + '/' + applicant + '/' + questionnaire_file)
                    checklist_df['Questionnaire'] = 'Present'
                    info_df = pd.concat([info_df, pd.DataFrame(applicant_info, index = [applicant[0:3]])])

                if any(x in entry.name.lower() for x in degree_keywords):
                    checklist_df['Diploma/ToR'] = 'Present'

                if re.search(r'(?<![a-z])cv(?![a-z])|curriculum vitae', entry.name.lower()):
                    checklist_df['CV'] = 'Present'
                    
    if questionnaire_found == False:
        print("WARNING: Questionnaire is missing. No data to extract.")
        info_df = pd.concat([info_df, pd.DataFrame({'E-mail Address': None}, index = [applicant[0:3]])])  # Necessary so that len(info_df) = len(full_checklist_df) when copying e-mail addresses further down

    full_checklist_df = pd.concat([full_checklist_df, checklist_df])

# Add empty checklist columns to be filled out by hand
for col in empty_cols_to_add:
    full_checklist_df[col] = ""
# Copy e-mail addresses to the checklist
full_checklist_df['E-mail'] = info_df['E-mail Address'].values

info_df.to_csv('./Complete_applicant_data_2026.csv')
full_checklist_df.reset_index(drop=True).to_csv('./Checklist_Admissions_2026.csv')