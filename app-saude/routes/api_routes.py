from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from models import User, Appointment
from database import db

api_bp = Blueprint('api_bp', __name__, url_prefix='/api')

@api_bp.route('/register', methods=['POST'])
def api_register():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')
    
    if not name or not email or not password:
        return jsonify({'error': 'Campos obrigatórios faltando.'}), 400

    if User.query.filter_by(email=email).first():
        return jsonify({'error': 'Email já cadastrado.'}), 400

    hashed_pw = generate_password_hash(password)
    new_user = User(name=name, email=email, password_hash=hashed_pw)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'Usuário registrado com sucesso!'}), 201

@api_bp.route('/login', methods=['POST'])
def api_login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    user = User.query.filter_by(email=email).first()
    if user and check_password_hash(user.password_hash, password):
        return jsonify({'message': 'Login realizado com sucesso!', 'user_id': user.id})
    else:
        return jsonify({'error': 'Credenciais inválidas.'}), 401

@api_bp.route('/appointment', methods=['POST'])
def api_create_appointment():
    data = request.get_json()
    hospital_id = data.get('hospital_id')
    specialty_id = data.get('specialty_id')
    doctor_id = data.get('doctor_id')
    date = data.get('date')
    user_id = data.get('user_id')

    if not all([hospital_id, specialty_id, doctor_id, date, user_id]):
        return jsonify({'error': 'Campos obrigatórios faltando.'}), 400

    new_appointment = Appointment(
        hospital_id=hospital_id,
        specialty_id=specialty_id,
        doctor_id=doctor_id,
        date=date,
        user_id=user_id
    )
    db.session.add(new_appointment)
    db.session.commit()
    return jsonify({'message': 'Agendamento criado com sucesso!'}), 201
