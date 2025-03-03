from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from models import User, Specialty, Doctor, Hospital
from database import db
from functools import wraps

admin_bp = Blueprint('admin_bp', __name__, url_prefix='/admin')

def admin_required(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if not session.get('admin_id'):
            flash('Acesso negado. Faça login como administrador.', 'error')
            return redirect(url_for('admin_auth_bp.admin_login'))
        return func(*args, **kwargs)
    return decorated_function

@admin_bp.route('/')
@admin_required
def admin_dashboard():
    users = User.query.all()
    specialties = Specialty.query.all()
    doctors = Doctor.query.all()
    hospitals = Hospital.query.all()
    return render_template('admin_dashboard.html', users=users, specialties=specialties, doctors=doctors, hospitals=hospitals)

@admin_bp.route('/add_hospital', methods=['POST'])
@admin_required
def add_hospital():
    name = request.form.get('name')
    if not name:
        flash('O nome do hospital é obrigatório.', 'error')
        return redirect(url_for('admin_bp.admin_dashboard'))
    if Hospital.query.filter_by(name=name).first():
        flash('Hospital já existe.', 'error')
        return redirect(url_for('admin_bp.admin_dashboard'))
    hospital = Hospital(name=name)
    db.session.add(hospital)
    db.session.commit()
    flash('Hospital adicionado com sucesso!', 'success')
    return redirect(url_for('admin_bp.admin_dashboard'))

@admin_bp.route('/add_specialty', methods=['POST'])
@admin_required
def add_specialty():
    name = request.form.get('name')
    if not name:
        flash('O nome da especialidade é obrigatório.', 'error')
        return redirect(url_for('admin_bp.admin_dashboard'))
    if Specialty.query.filter_by(name=name).first():
        flash('Especialidade já existe.', 'error')
        return redirect(url_for('admin_bp.admin_dashboard'))
    specialty = Specialty(name=name)
    db.session.add(specialty)
    db.session.commit()
    flash('Especialidade adicionada com sucesso!', 'success')
    return redirect(url_for('admin_bp.admin_dashboard'))

@admin_bp.route('/add_doctor', methods=['POST'])
@admin_required
def add_doctor():
    name = request.form.get('name')
    crm = request.form.get('crm')
    specialty_id = request.form.get('specialty_id')
    hospital_id = request.form.get('hospital_id')
    if not name or not crm or not specialty_id or not hospital_id:
        flash('Todos os campos do doutor são obrigatórios.', 'error')
        return redirect(url_for('admin_bp.admin_dashboard'))
    doctor = Doctor(name=name, crm=crm, specialty_id=specialty_id, hospital_id=hospital_id)
    db.session.add(doctor)
    db.session.commit()
    flash('Doutor adicionado com sucesso!', 'success')
    return redirect(url_for('admin_bp.admin_dashboard'))
