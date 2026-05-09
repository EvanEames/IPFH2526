from dataclasses import dataclass, field
import pandas as pd

@dataclass
class Applicant:
    id: int
    first_name: str
    last_name: str
    date_of_birth=None
    place_of_birth=None
    nationality=None
    address=None
    email=None
    phone=None
    degrees: list = field(default_factory=list)
    programs: list = field(default_factory=list)
    universities: list = field(default_factory=list)
    graduation_years: list = field(default_factory=list)
    questionnaire=False
    diploma=False
    cv=False

    def update_data(self, data):
        self.date_of_birth=data['Date of Birth']
        self.place_of_birth=data['Place of Birth']
        self.nationality=data['Nationality']
        self.address=data['Current Home Address']
        self.phone=data['Telephone']
        self.email=data['E-mail Address']

        degree_strings = ['1st Degree', '2nd Degree', '3rd Degree']
        for i, degree in enumerate(degree_strings):
            self.degrees.append(data[degree])
            self.programs.append(data[str(i+1) + ' Full Name of Program'])
            self.universities.append(data[str(i+1) + ' University'])
            self.graduation_years.append(data[str(i+1) + ' Year of graduation'])
            

    def app_info_to_dict(self):
        dict = {'Application No.': self.id,
                'Surname': self.last_name,
                'First name': self.first_name,
                'Date of Birth': self.date_of_birth,
                'Place of Birth': self.place_of_birth,
                'Nationality': self.nationality,
                'Current Home Address': self.address,
                'E-mail Address': self.email,
                'Telephone': self.phone
                }
        degree_strings = ['1st Degree', '2nd Degree', '3rd Degree']
        for i in range(len(self.degrees)):
            dict[degree_strings[i]] = self.degrees[i]
            dict[str(i+1) + ' Full Name of Program'] = self.programs[i]
            dict[str(i+1) + ' University'] = self.universities[i]
            dict[str(i+1) + ' Year of graduation'] = self.graduation_years[i]
        
        return dict
    
    def make_checklist(self, empty_cols_to_add=[]):
        dict={'Application No.': self.id,
              'Surname': self.last_name,
              'First name': self.first_name,
              'CV': "Present" if self.cv else None,
              'Questionnaire': "Present" if self.questionnaire else None,
              'Diploma/ToR': "Present" if self.diploma else None,
              'E-mail': self.email
                }
        
        for col in empty_cols_to_add:
            dict[col] = None
        
        return dict