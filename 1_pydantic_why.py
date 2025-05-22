from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name: Annotated[str, Field(max_length=50, title='Name of the patient', description='Give the name of the patient in less than 50 characters', examples=['subhadip', 'amit'])]
    email: EmailStr
    linked_url: AnyUrl
    age: int = Field(ge=0, le=120)
    weight: Annotated[float, Field(gt=0, strict=True)]
    married: Annotated[bool, Field(default = None, description='Is the patient married?')]
    allergies: Annotated[Optional[List[str]], Field(default=None, max_length=5)]
    contact_details: Dict[str, str]

def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print('inserted')

def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print('updated')

patient_info = {'name':'subhadip', 'email': 'abc@gmail.com', 'linked_url': 'http://linked.com/123', 'age': 24, 'weight': 70.5, 'married': False, 'allerhies': ['dust', 'pollen'], 'contact_details': {'phone': '2345689'}}

patient1 = Patient(**patient_info)

update_patient_data(patient1)

