from database import db
from sqlalchemy.sql import func

# Para crear las tablas, desde el entorno de ejecución de Python, ejecutar:
# from database import app, db
# from estudiante import Estudiante
# app.app_context().push()
# db.create_all()

class Estudiante(db.Model):
    
    __tablename__ = 'estudiantes'
         
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    apellidos = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    edad = db.Column(db.Integer)
    biografia = db.Column(db.Text)
    creado_en = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())
     
    def __init__(self, nombre, apellidos, email, edad, bio):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.edad = edad
        self.biografia = bio

    def __repr__(self):
        return f'<Estudiante {self.id}>: {self.nombre}, {self.apellidos}'
    
    