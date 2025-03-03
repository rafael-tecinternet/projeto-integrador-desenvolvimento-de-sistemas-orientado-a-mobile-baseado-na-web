from flask import Flask
from config import Config
from database import db
from routes.main_routes import main_bp
from routes.api_routes import api_bp
from routes.admin_routes import admin_bp
from routes.admin_auth_routes import admin_auth_bp
from routes.patient_routes import patient_bp
from routes.patient_auth_routes import patient_auth_bp

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
with app.app_context():
    db.create_all()

app.register_blueprint(main_bp)
app.register_blueprint(api_bp)
app.register_blueprint(admin_bp)
app.register_blueprint(admin_auth_bp)
app.register_blueprint(patient_bp)
app.register_blueprint(patient_auth_bp)

if __name__ == '__main__':
    app.run(debug=True)
