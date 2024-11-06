from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship 
from sqlalchemy.ext.declarative import declarative_base

#Llamado a la base para creaar tablas

Base =  declarative_base()

#Definicion de las tablas de mi modelo
#Usuario
class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key = True, autoincrement = True)
    nombres = Column(String(50))
    fechaNacimiento = Column(Date)
    ubicacion = Column(String(100))
    metaAhorro = Column(Float)

class Gastos(Base):
    __tablename__ = 'gastos'
    id = Column(Integer, primary_key = True, autoincrement = True)
    descripcion = Column(String(200))
    categoria = ""
    valor = Column(Float)
    fecha = Column(Date)

class Categorias(Base):
    __tablename__ = 'Categorias'
    id = Column(Integer, primary_key = True, autoincrement = True)
    nombres = Column(String(30))
    descripcion = Column(String(200))
    fotoCategoria = Column(String(200))

class Ingresos(Base):
    __tablename__ = 'Ingresos'
    id = Column(Integer, primary_key = True, autoincrement = True)
    valor = Column(Float)
    descripcion = Column(String(200))
    fecha = Column(Date)

class Prestamos(Base):
    __tablename__ = 'prestamos'
    id = Column(Integer, primary_key = True, autoincrement = True)
    valor = Column(Float)
    descripcion = Column(String(200))
    fecha = Column(Date)
    tiempo = Column(Integer)
    porcentaje = Column(Float)
    
class Inversiones(Base):
    __tablename__ = 'inversiones'
    id = Column(Integer, primary_key = True, autoincrement = True)
    valor = Column(Float)
    descripcion = Column(String(200))
    fecha = Column(Date)
    tiempo = Column(Integer)
    porcentaje = Column(Float)