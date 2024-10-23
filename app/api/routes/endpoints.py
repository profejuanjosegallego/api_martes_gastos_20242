from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from typing import List
from fastapi.params import Depends

from app.api.DTO.dtos import UsuarioDTOPeticion, UsuarioDTORespuesta
from app.api.DTO.dtos import GastosDTOPeticion, GastosDTORespuesta
from app.api.DTO.dtos import CategoriasDTOPeticion, CategoriasDTORespuesta
from app.api.DTO.dtos import IngresosDTOPeticion, IngresosDTORespuesta
from app.api.DTO.dtos import InversionesDTOPeticion, InversionesDTORespuesta
from app.api.DTO.dtos import PrestamosDTOPeticion, PrestamosDTORespuesta
from app.api.models.tablasSQL import Usuario, Gastos,Categorias, Ingresos, Inversiones, Prestamos
from app.database.configuration import sessionLocal, engine

rutas = APIRouter()

def conectarConBD():
    try:
        dataBase = sessionLocal()
        yield dataBase

    except Exception as error:
        dataBase.rollback()
        raise error

    finally:
        dataBase.close

#Construyendo nuestros servicios
#Cada servicio (operacion o transaccion) 
# debe programarse como una funcion
@rutas.post("/usuario", response_model= UsuarioDTORespuesta, summary="Registrar un usuario en la BD")
def guardarUsuario(datosUsuario: UsuarioDTOPeticion, database: Session = Depends(conectarConBD)):
    try:
        usuario = Usuario(
            nombres = datosUsuario.nombres,
            fechaNacimiento = datosUsuario.fechaNacimiento,
            ubicacion = datosUsuario.ubicacion,
            metaAhorro = datosUsuario.metaAhorro
        )
        #Ordenes a la BD
        database.add(usuario)
        database.commit()
        database.refresh(usuario)
        return usuario

    except Exception as error:
        database.rollback()
        raise HTTPException(status_code= 400, detail=f"Tenemos un problema{error}")
    
@rutas.get("/usuario", response_model= List[UsuarioDTORespuesta], summary= "Buscar todos los usuarios en BD")    
def buscarUsuario(database: Session = Depends(conectarConBD)):
    try:
        usuarios= database.query(Usuario).all()
        return usuarios

    except Exception as error:
        database.rollback()
        raise HTTPException(status_code= 400, detail=f"No se puede encontrar el Usuario{error}")

@rutas.post("/gastos", response_model= GastosDTORespuesta, summary="Registrar un gasto en la BD")
def guardarGasto(datosGasto: GastosDTOPeticion, database: Session = Depends(conectarConBD)):
    try:
        gasto = Gastos(
            descripcion = datosGasto.descripcion,
            categoria = datosGasto.categoria,
            valor = datosGasto.valor,
            fecha = datosGasto.fecha
        )
        #Ordenes a la BD
        database.add(gasto)
        database.commit()
        database.refresh(gasto)
        return gasto

    except Exception as error:
        database.rollback()
        raise HTTPException(status_code= 400, detail=f"Tenemos un problema{error}")
    
@rutas.get("/gasto", response_model= List[GastosDTORespuesta], summary= "Buscar todos los gastos en BD")    
def buscarGasto(database: Session = Depends(conectarConBD)):
    try:
        gastos= database.query(Gastos).all()
        return gastos

    except Exception as error:
        database.rollback()
        raise HTTPException(status_code= 400, detail=f"No se puede encontrar el Gasto{error}")

@rutas.post("/categorias", response_model= CategoriasDTORespuesta, summary="Registrar una categoría en la BD")
def guardarCategoria(datosCategoria: CategoriasDTOPeticion, database: Session = Depends(conectarConBD)):
    try:
        categoria = Categorias(
            nombres = datosCategoria.nombres,
            descripcion = datosCategoria.descripcion,
            fotoCategoria = datosCategoria.fotoCategoria
        )
        #Ordenes a la BD
        database.add(categoria)
        database.commit()
        database.refresh(categoria)
        return categoria

    except Exception as error:
        database.rollback()
        raise HTTPException(status_code= 400, detail=f"Tenemos un problema{error}")
    
@rutas.get("/categoria", response_model= List[CategoriasDTORespuesta], summary= "Buscar todos las categorías en BD")    
def buscarCategoria(database: Session = Depends(conectarConBD)):
    try:
        categoria= database.query(Categorias).all()
        return categoria

    except Exception as error:
        database.rollback()
        raise HTTPException(status_code= 400, detail=f"No se puede encontrar la categoria{error}")
    
@rutas.post("/ingresos", response_model= IngresosDTORespuesta, summary="Registrar un ingresos en la BD")
def guardarIngresos(datosIngresos: IngresosDTOPeticion, database: Session = Depends(conectarConBD)):
    try:
        ingreso = Ingresos(
            valor = datosIngresos.valor,
            descripcion = datosIngresos.descripcion,
            fecha = datosIngresos.fecha
        )
        #Ordenes a la BD
        database.add(ingreso)
        database.commit()
        database.refresh(ingreso)
        return ingreso

    except Exception as error:
        database.rollback()
        raise HTTPException(status_code= 400, detail=f"Tenemos un problema{error}")
    
@rutas.get("/ingresos", response_model= List[IngresosDTORespuesta], summary= "Buscar todos los ingresos en BD")    
def buscarIngresos(database: Session = Depends(conectarConBD)):
    try:
        ingreso= database.query(Ingresos).all()
        return ingreso

    except Exception as error:
        database.rollback()
        raise HTTPException(status_code= 400, detail=f"No se puede encontrar el ingreso.{error}")