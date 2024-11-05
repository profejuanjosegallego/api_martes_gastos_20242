from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey

from sqlalchemy.orm import relationship

from sqlalchemy.ext.declarative import declarative_base

#LLamado a la base para crear tablas
Base=declarative_base()

#DEFINICION DE LAS TABLAS DE MI MODELO

#usuario
class Usuario(Base):
    __tablename__='usuarios'
    id=Column(Integer, primary_key=True, autoincrement=True)
    nombres=Column(String(50))
    fechaNacimiento=Column(Date)
    ubicacion=Column(String(100))
    metaAhorro=Column(Float)

class Gasto(Base):
    #id
    #descripcion
    #categoria *********
    #valor
    #fecha
    pass
    
class Categoria(Base):
    #id
    #nombre
    #descripcion
    #fotoCategoria
    pass

class Ingreso(Base):
    #id
    #valor
    #descripcion
    #fecha
    pass