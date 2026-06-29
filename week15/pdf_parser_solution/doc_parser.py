import os
import re
import pandas as pd

from utils import initializeApplicant, extractApplicantInfo

directory_path = '../../../../Admissions_2026'
questionnaire_file = ''

degree_keywords = ['degree', 'diploma', 'transcript']
writing_sample_keywords = ['writing', 'sample', 'essay', 'written']
english_certificate_keywords = ['english', 'ielts', 'toefl', 'duolingo' 'medium', 'language', 'cambridge']
empty_cols_to_add = ['Declaration','Remarks','Confirmation sent']

info_df = pd.DataFrame()
full_checklist_df = pd.DataFrame()

dir_names = []
# Get directory names
with os.scandir(directory_path) as entries:
    for entry in entries:
        if entry.is_dir():
            dir_names.append(entry.name)

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
                    _ = extractApplicantInfo(applicant_dir, applicant)

                # Check if there is a diploma/degree/transcript
                if any(x in entry.name.lower() for x in degree_keywords):
                    applicant.diploma=True

                # Check if there is a cv
                if re.search(r'(?<![a-z])cv(?![a-z])|curriculum vitae', entry.name.lower()):
                    applicant.cv = True

                # Check if there is a writing sample
                if any(x in entry.name.lower() for x in writing_sample_keywords):
                    applicant.sample = True

                # Check if there is an english certificate
                if any(x in entry.name.lower() for x in english_certificate_keywords):
                    applicant.english = True
                    
    if applicant.questionnaire == False:
        print("WARNING: Questionnaire is missing. No data to extract.")

    # Format the dictionaries if this is the first applicant
    if len(info_df) == 0:
        info_df = pd.DataFrame(applicant.app_info_to_dict(), index=[0])
        full_checklist_df = pd.DataFrame(applicant.make_checklist(empty_cols_to_add=empty_cols_to_add), index=[0])
    # Otherwise just append a new row
    else:
        info_df.loc[len(info_df)] = applicant.app_info_to_dict()
        full_checklist_df.loc[len(full_checklist_df)] = applicant.make_checklist()

# Save to csv
info_df.to_csv('./Complete_applicant_data_2026.csv')
full_checklist_df.reset_index(drop=True).to_csv('./Checklist_Admissions_2026.csv')
