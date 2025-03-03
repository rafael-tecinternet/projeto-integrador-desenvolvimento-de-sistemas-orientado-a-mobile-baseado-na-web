from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from models import Admin
from werkzeug.security import check_password_hash
from database import db

admin_auth_bp = Blueprint('admin_auth_bp', __name__, url_prefix='/admin')

@admin_auth_bp.route('/login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        admin = Admin.query.filter_by(username=username).first()
        if admin and check_password_hash(admin.password_hash, password):
            session['admin_id'] = admin.id
            return redirect(url_for('admin_bp.admin_dashboard'))
        else:
            flash('Credenciais inválidas', 'error')
    return render_template('admin_login.html')

@admin_auth_bp.route('/logout')
def admin_logout():
    session.pop('admin_id', None)
    return redirect(url_for('admin_auth_bp.admin_login'))
