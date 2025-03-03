from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from models import User, Appointment, Hospital, Specialty, Doctor
from database import db
from werkzeug.security import generate_password_hash

patient_bp = Blueprint('patient_bp', __name__, url_prefix='/patient')

@patient_bp.route('/profile', methods=['GET', 'POST'])
def profile():
    user_id = session.get('user_id')
    if not user_id:
        flash('Você precisa estar logado para acessar sua área.', 'error')
        return redirect(url_for('patient_auth_bp.login'))
    
    user = User.query.get(user_id)
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        if name:
            user.name = name
        if email:
            user.email = email
        if password:
            user.password_hash = generate_password_hash(password)
        db.session.commit()
        flash('Perfil atualizado com sucesso!', 'success')
        return redirect(url_for('patient_bp.profile'))
    
    appointments = Appointment.query.filter_by(user_id=user_id).all()
    return render_template('patient_profile.html', user=user, appointments=appointments)

@patient_bp.route('/schedule', methods=['GET', 'POST'])
def schedule():
    user_id = session.get('user_id')
    if not user_id:
        flash('Você precisa estar logado para agendar uma consulta.', 'error')
        return redirect(url_for('patient_auth_bp.login'))
    
    if request.method == 'POST':
        hospital_id = request.form.get('hospital_id')
        specialty_id = request.form.get('specialty_id')
        doctor_id = request.form.get('doctor_id')
        date = request.form.get('date')
        if not all([hospital_id, specialty_id, doctor_id, date]):
            flash('Todos os campos são obrigatórios para o agendamento.', 'error')
            return redirect(url_for('patient_bp.schedule'))
        new_app = Appointment(
            hospital_id=hospital_id,
            specialty_id=specialty_id,
            doctor_id=doctor_id,
            date=date,
            user_id=user_id
        )
        db.session.add(new_app)
        db.session.commit()
        flash("Agendamento realizado com sucesso!", "success")
        return redirect(url_for('patient_bp.profile'))
    
    # Carrega opções para agendamento
    hospitals = Hospital.query.all()
    specialties = Specialty.query.all()
    doctors = Doctor.query.all()
    return render_template('patient_schedule.html', hospitals=hospitals, specialties=specialties, doctors=doctors)

@patient_bp.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('patient_auth_bp.login'))
