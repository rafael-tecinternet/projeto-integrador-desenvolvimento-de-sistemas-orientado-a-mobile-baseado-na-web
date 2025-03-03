from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from models import User
from werkzeug.security import generate_password_hash, check_password_hash
from database import db

patient_auth_bp = Blueprint('patient_auth_bp', __name__, url_prefix='/patient')

@patient_auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password_hash, password):
            session['user_id'] = user.id
            return redirect(url_for('patient_bp.profile'))
        else:
            flash('Credenciais inválidas', 'error')
    return render_template('patient_login.html')
    
@patient_auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        if not name or not email or not password:
            flash('Todos os campos são obrigatórios.', 'error')
            return redirect(url_for('patient_auth_bp.register'))
        if User.query.filter_by(email=email).first():
            flash('Email já cadastrado.', 'error')
            return redirect(url_for('patient_auth_bp.register'))
        new_user = User(name=name, email=email, password_hash=generate_password_hash(password))
        db.session.add(new_user)
        db.session.commit()
        flash('Usuário registrado com sucesso! Faça login para continuar.', 'success')
        return redirect(url_for('patient_auth_bp.login'))
    return render_template('patient_register.html')

@patient_auth_bp.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('patient_auth_bp.login'))
