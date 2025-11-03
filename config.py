import os

SECRET_KEY = 'CHAVE-SUPER-SECRETA'  # Chave secreta para criptografia
DEBUG = True
# Configurações do banco de dados Firebird
DB_HOST = 'localhost'
DB_NAME = r'C:\Users\User\Downloads\Nova-API-LIBRIS-main\Nova-API-LIBRIS-main\BANCO_LIBRIS.FDB'
#UPLOAD_FOLDER = os.path.join(os.getcwd(), 'static/uploads')
UPLOAD_FOLDER = os.path.join(os.getcwd(), 'static', 'uploads')


DB_USER = 'sysdba'
DB_PASSWORD = 'sysdba'

