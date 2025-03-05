import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app, db
from models import Admin
from werkzeug.security import generate_password_hash

with app.app_context():
    username = "admin"          # Defina o nome de usuário desejado
    password = "minhaSenhaForte"  # Defina uma senha forte

    # Verifica se já existe um admin com esse nome
    if not Admin.query.filter_by(username=username).first():
        new_admin = Admin(username=username, password_hash=generate_password_hash(password))
        db.session.add(new_admin)
        db.session.commit()
        print("Admin criado com sucesso!")
    else:
        print("Admin já existe!")
