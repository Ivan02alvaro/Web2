from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash
#CREANDO UNA BASE DE DATOS DE TIPO SQLALCHEMY

#SE DEBE INSTALAR IGUAL QUE FLASK

#pip install flask-sqlalchemy
db=SQLAlchemy()


#class Usuario dependera de db y model
class Usuario(db.Model):
    #herramientao orm de objeto relacional para base de datos para python
    #pip install flask-sqlalchemy
    __talename__='usuarios'
    #__talename__='usuarios'  tabla de usuarios

    id=db.Column(db.Integer,primary_key=True)
    nombre=db.Column(db.String(200),nullabel=False)
    correo=db.Column(db.String(100),unique=True, nullabel=False)

    contrasena_hash=db.Column(db.String(256), nullabel=False)
    #nullabel=False indica que siempre debe estar llenado
    #db.Column indica columna
    tareas=db.relationship('Tarea', backref='usuario',Lazy=True)

    def colocar_contrasena(self,contrasena):
        self.contrasena_hash=generate_password_hash(contrasena)
    #permite modificar contraseñ
    #def colocar_contrasena(self,contrasena):
        #self.contrasena_hash=generate_password_hash(contrasena)

    def verificar_contrasena(self,contrasena):
        return check_password_hash(self.contrasena_hash,contrasena)
    #check_password_hash con esto verificamos la contrseña introducida


class Tarea(db.Model):
    __tablename__='tareas'

    id=db.Column(db.Integer,primary_key=False)
    titulo=db.Column(db.String(200),nullabel=False)
    descripcion=db.Column(db.Text,nullabel=True)
    fecha_creacion=db.column(db.DateTime,default=datetime.utcnow)
    fecha_vencimiento=db.column(db.DateTime,nullabel=False)
    completa=db.column(db.Boolean,default=False)
    prioridad=db.column(db.String(50),nullabel=False)
    usuario_id=db.column(db.Integer,db.Foreign_key('usuarios.id'),nullabel=False)
    #db.Foreign_key('usuarios.id') con esta linea relacionamos 
    #la anterior clase usuarios en especifico con su id



