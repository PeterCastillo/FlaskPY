from flask import Flask, request
from config import conexion
from flask_migrate import Migrate
from os import environ
from dotenv import load_dotenv
from src.models.usuarios import UsuarioModel

load_dotenv()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL')

conexion.init_app(app)

migrate = Migrate(app,conexion)

if __name__ == ('__main__'):
    app.run(debug=True)
 

@app.route("/")
def index():
    return 'Hola soy un servidor de Flask'

@app.route("/users")
def home():
    usuarios = [
        {
            "nombre": "Peter",
            "apellido": "Castillo"
        },
        {
            "nombre": "Stanley",
            "apellido": "Castillo"
        }
    ]
    for user in usuarios:
        return f'El nombre del usuario es: {user["nombre"]}'

@app.route("/user/<name>")
def user(name):
    return f'Usuario ingresado: {name}'

@app.route("/login", methods=['POST'])
def login():
    print(request.method)
    return 'Esta es la ruta login'