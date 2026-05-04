import os
import re
import pandas as pd
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.psparser import PSLiteral, PSSyntaxError
from pdfminer.pdftypes import resolve1, PDFObjRef
from applicant_class import Applicant

directory_path = '../../../Admissions_2026'
questionnaire_file = ''

degree_keywords = ['degree', 'diploma', 'transcript']
empty_cols_to_add = ['Academic Work Sample','English Certificate','Declaration','Remarks','Confirmation sent']

dir_names = []
# Get directory names
with os.scandir(directory_path) as entries:
    for entry in entries:
        if entry.is_dir():
            dir_names.append(entry.name)

def initializeApplicant(directory):
    id = [directory.split('_')[0]]
    last_name = [directory.split('_')[-1]]
    first_name = [' '.join(directory.split('_')[1:-1])]
    applicant = Applicant(id, first_name, last_name)
    return applicant

def extractApplicantInfo(questionnaire_file, applicant):
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
                applicant.date_of_birth=data['Date of Birth']
                applicant.place_of_birth=data['Place of Birth']
                applicant.nationality=data['Nationality']
                applicant.address=data['Current Home Address']
                applicant.phone=data['Telephone']
                applicant.email=data['E-mail Address']
        except:
            print("WARNING: Cannot handle file with digital signature.")
            return {}
        
    return data

# Get Questionnaire info and fill out checklist
for dir in dir_names:
    print(dir)
    applicant = initializeApplicant(dir)
    with os.scandir(directory_path + '/' + dir) as entries:
        for entry in entries:
            if entry.is_file():
                if 'questionnaire' in entry.name.lower():
                    applicant.questionnaire = True
                    questionnaire_file = entry.name
                    applicant_dir = directory_path + '/' + dir + '/' + questionnaire_file
                    extractApplicantInfo(applicant_dir, applicant)

                if any(x in entry.name.lower() for x in degree_keywords):
                    applicant.diploma=True

                if re.search(r'(?<![a-z])cv(?![a-z])|curriculum vitae', entry.name.lower()):
                    applicant.cv = True
                    
    if applicant.questionnaire == False:
        print("WARNING: Questionnaire is missing. No data to extract.")
