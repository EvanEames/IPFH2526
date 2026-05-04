from dataclasses import dataclass

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
    universities=[]
    programs=[]
    graduation_years=[]
    questionnaire=False
    diploma=False
    cv=False
