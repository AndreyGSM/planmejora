from marshmallow import Schema, fields
from flask import Flask
from werkzeug.security import generate_password_hash, check_password_hash
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Rol(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(100), nullable=False)
    super_admin = db.Column(db.Boolean, default=False)

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(100), nullable=False)
    
    rol_id = db.Column(db.Integer, db.ForeignKey('rol.id'), nullable=False)  
    rol = db.relationship('Rol', backref='usuarios', lazy=True)  

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')
    
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)
        
    def verificar_password(self, password):
        return check_password_hash(self.password_hash, password)

    @property
    def es_superadmin(self):
        return self.rol.super_admin
    

class Departamento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)

class Empleado(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    departamento_id = db.Column(db.Integer, db.ForeignKey('departamento.id'), nullable=False)
    foto_url = db.Column(db.String(300))
    departamento = db.relationship('Departamento', backref='empleados')

class Familiar(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    parentesco = db.Column(db.String(50), nullable=False)
    vive_con_empleado = db.Column(db.Boolean, default=True)
    empleado_id = db.Column(db.Integer, db.ForeignKey('empleado.id'), nullable=False)
    empleado = db.relationship('Empleado', backref='familiares')
    
    

#serializacion de modelos
class ROlSchema(SQLAlchemyAutoSchema):
    class Meta:
        Mode = Rol
        include_relationships = True
        Load_Instance = True


class UsuarioSchema(SQLAlchemyAutoSchema):
    class Meta:
        Mode = Usuario
        include_relationships = True
        Load_Instance = True

class EmpleadoSchema(SQLAlchemyAutoSchema):
    class Meta:
        Mode = Empleado
        include_relationships = True
        Load_Instance = True

class DepartamenoSchema(SQLAlchemyAutoSchema):
    class Meta:
        Mode = Departamento
        include_relationships = True
        Load_Instance = True
