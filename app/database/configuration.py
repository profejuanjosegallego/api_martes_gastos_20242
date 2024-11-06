<<<<<<< HEAD
from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import Engine

=======
from sqlalchemy import create_engine,event
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import Engine


>>>>>>> e56970047174ac8f6b145be43202dd767a975555
#datos para la conexion a BD

dataBaseName="gestordb"
userName="root"
userPassword=""
connectionPort=3306
server="localhost"

#creando la conexion
dataBaseConnection=f"mysql+mysqlconnector://{userName}:{userPassword}@{server}:{connectionPort}/{dataBaseName}"

<<<<<<< HEAD
#Creo motor de conexion
engine = create_engine(dataBaseConnection)

#Abrir la sesion con la base de datos
sessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)

=======
#creo el motor de conexion
engine=create_engine(dataBaseConnection)

#abrir la sesion con la bd
SessionLocal=sessionmaker(autocommit=False, autoflush=False, bind=engine)
>>>>>>> e56970047174ac8f6b145be43202dd767a975555

