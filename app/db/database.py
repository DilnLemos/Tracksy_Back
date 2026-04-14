from sqlalchemy import create_engine
from sqlalchemy.pool import NullPool
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Fetch variables
USER = os.getenv("DB_USER")
PASSWORD = os.getenv("DB_PASSWORD")
HOST = os.getenv("DB_HOST")
PORT = os.getenv("DB_PORT")
DBNAME = os.getenv("DB_NAME")

# Construct the SQLAlchemy connection string
DATABASE_URL = f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DBNAME}?sslmode=require"

# Create the SQLAlchemy engine
engine = create_engine(
    DATABASE_URL,
    connect_args={"sslmode": "require"},
    # If using Transaction Pooler or Session Pooler, we want to ensure we disable SQLAlchemy client side pooling -
    poolclass=NullPool
)

# sessionlocal: Crea una clase de sesión para interactuar con la base de datos
# Cada instancia de esta sesión representa una transacción con la base de datos
# autocommit=False: Las operaciones no se confirman automáticamente, necesitas hacer commit
# autoflush=False: Los cambios no se envían automáticamente a la BD antes de las consultas
sessionlocal = sessionmaker(bind = engine, autocommit = False, autoflush = False)

# base: Clase base para definir todos los modelos de SQLAlchemy
# Todos los modelos (como User) deben heredar de esta clase para convertirse en tablas
# Permite que SQLAlchemy reconozca y mapee las clases Python a tablas de la base de datos
Base = declarative_base()

# Test the connection
try:
    with engine.connect() as connection:
        print("Connection successful!")
except Exception as e:
    print(f"Failed to connect: {e}")