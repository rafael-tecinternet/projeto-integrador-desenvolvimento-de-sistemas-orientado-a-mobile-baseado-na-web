import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import random
from app import app, db
from models import Hospital, Specialty, Doctor

with app.app_context():

    hospital_names = [
        "Hospital Central",
        "Hospital São João",
        "Hospital Santa Maria",
        "Hospital da Saúde",
        "Hospital Vida",
        "Hospital Bem-Estar",
        "Hospital Esperança",
        "Hospital São Lucas",
        "Hospital Vitória",
        "Hospital São Marcos"
    ]
    hospitals = []
    for name in hospital_names:
        hospital = Hospital(name=name)
        db.session.add(hospital)
        hospitals.append(hospital)

    specialty_names = [
        "Cardiologia", "Dermatologia", "Neurologia", "Ortopedia", "Pediatria",
        "Ginecologia", "Oncologia", "Psiquiatria", "Oftalmologia", "Urologia",
        "Gastroenterologia", "Endocrinologia", "Reumatologia", "Nefrologia",
        "Cirurgia Geral", "Cirurgia Plástica", "Anestesiologia", "Hematologia",
        "Infectologia", "Radiologia"
    ]
    specialties = []
    for name in specialty_names:
        specialty = Specialty(name=name)
        db.session.add(specialty)
        specialties.append(specialty)

    db.session.commit()

    first_names = ["Carlos", "Ana", "Marcos", "Fernanda", "João", "Juliana", "Paulo", "Beatriz", "Ricardo", "Patrícia"]
    last_names = ["Silva", "Santos", "Oliveira", "Costa", "Pereira", "Rodrigues", "Almeida", "Lima", "Gomes", "Martins"]

    num_doctors = 50 
    for i in range(num_doctors):
        first = random.choice(first_names)
        last = random.choice(last_names)
        name = f"Dr. {first} {last}"
        crm = f"CRM{str(i+1).zfill(4)}" 
        specialty = random.choice(specialties)
        hospital = random.choice(hospitals)
        doctor = Doctor(name=name, crm=crm, specialty_id=specialty.id, hospital_id=hospital.id)
        db.session.add(doctor)

    db.session.commit()
    print("Dados semeados com sucesso!")
