from os import path

BASE_DIR = path.abspath(path.join(path.dirname(__file__), '..'))

class Config:
    SECRET_KEY = 'AAKKKSJDDHDHDHDH%5'
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + path.join(BASE_DIR, 'test.db')
    UPLOAD_PATH = path.join(BASE_DIR, 'static', 'uploads')