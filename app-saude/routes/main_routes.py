from flask import Blueprint, render_template
from models import Appointment

main_bp = Blueprint('main_bp', __name__)

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/login')
def login_page():
    return render_template('login.html')

@main_bp.route('/register')
def register_page():
    return render_template('register.html')

@main_bp.route('/dashboard')
def dashboard():
    appointments = Appointment.query.all()
    return render_template('dashboard.html', appointments=appointments)
