import os
basedir = os.path.abspath(os.path.dirname(__file__))

data_dir = os.path.join(basedir, 'data')
if not os.path.exists(data_dir):
    os.makedirs(data_dir)

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(data_dir, 'db.sqlite3')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "UmaChaveMuitoSecreta"
#config