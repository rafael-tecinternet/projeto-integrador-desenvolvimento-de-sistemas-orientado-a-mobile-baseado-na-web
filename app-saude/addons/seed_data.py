import random
from app import app, db
from models import Hospital, Specialty, Doctor

with app.app_context():
    # Opcional: Limpa os registros existentes (cuidado em produção)
    # db.drop_all()
    # db.create_all()

    # Lista de hospitais (máximo 10)
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

    # Lista de especialidades (cerca de 20)
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

    # Confirma a criação de hospitais e especialidades
    db.session.commit()

    # Dados para gerar nomes aleatórios para os médicos
    first_names = ["Carlos", "Ana", "Marcos", "Fernanda", "João", "Juliana", "Paulo", "Beatriz", "Ricardo", "Patrícia"]
    last_names = ["Silva", "Santos", "Oliveira", "Costa", "Pereira", "Rodrigues", "Almeida", "Lima", "Gomes", "Martins"]

    num_doctors = 50  # Quantidade de médicos a serem criados
    for i in range(num_doctors):
        first = random.choice(first_names)
        last = random.choice(last_names)
        name = f"Dr. {first} {last}"
        crm = f"CRM{str(i+1).zfill(4)}"  # Ex.: CRM0001, CRM0002, etc.
        # Seleciona aleatoriamente uma especialidade e um hospital
        specialty = random.choice(specialties)
        hospital = random.choice(hospitals)
        doctor = Doctor(name=name, crm=crm, specialty_id=specialty.id, hospital_id=hospital.id)
        db.session.add(doctor)

    db.session.commit()
    print("Dados semeados com sucesso!")
