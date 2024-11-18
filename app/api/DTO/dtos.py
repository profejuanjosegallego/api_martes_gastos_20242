from pydantic import BaseModel, Field
from datetime import date

#Los DTOs son clases que establecen el 
#modelo de transferencia de datos
class UsuarioDTOPeticion(BaseModel):
    nombres: str
    email: str
    password: str
    fechaNacimiento: date
    ubicacion: str
    metaAhorro: float
    class Config:
        orm_model = True

class UsuarioDTORespuesta(BaseModel):
    id: int
    nombres: str
    metaAhorro: float
    class Config:
        orm_model = True

class GastosDTOPeticion(BaseModel):
    descripcion: str
    categoria: str
    valor: float
    fecha:date
    class Config:
        orm_model = True

class GastosDTORespuesta(BaseModel):
    id: int
    descripcion: str
    categoria: str
    valor: float
    fecha:date
    class Config:
        orm_model = True

class CategoriasDTOPeticion(BaseModel):
    nombres: str
    descripcion: str
    fotoCategoria: str
    class Config:
        orm_model = True

class CategoriasDTORespuesta(BaseModel):
    id: int
    nombreCategoria: str
    descripcion: str
    fotoCategoria: str
    class Config:
        orm_model = True

class IngresosDTOPeticion(BaseModel):
    valor: float
    descripcion: str
    fecha: date
    class Config:
        orm_model = True

class IngresosDTORespuesta(BaseModel):
    id: int
    valor: float
    descripcion: str
    fecha: date
    class Config:
        orm_model = True

class PrestamosDTOPeticion(BaseModel):
    valor: float
    descripcion: str
    fecha: date
    tiempo:int
    porcentaje: float
    class Config:
        orm_model = True

class PrestamosDTORespuesta(BaseModel):
    id: int
    valor: float
    descripcion: str
    fecha: date
    tiempo:int
    porcentaje: float
    class Config:
        orm_model = True

class InversionesDTOPeticion(BaseModel):
    valor: float
    descripcion: str
    fecha: date
    tiempo: int
    porcentaje: float
    class Config:
        orm_model = True        

class InversionesDTORespuesta(BaseModel):
    id: int
    valor: float
    descripcion: str
    fecha: date
    tiempo: int
    porcentaje: float
    class Config:
        orm_model = True        
