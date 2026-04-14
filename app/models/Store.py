from app.db.database import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import func

class Store(Base):
    __tablename__ = "stores"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    owner_id = Column(Integer, nullable=False)
    
    created_at = Column(DateTime, server_default=func.now())
    status = Column(String(50), default="active")

    # Relación: Tienda tiene muchos StoreUser
    users = relationship("StoreUser", back_populates="store")

class StoreUser(Base):
    __tablename__ = "store_users"
    
    id = Column(Integer, primary_key=True, index=True)
    store_id = Column(Integer, ForeignKey("stores.id"), nullable=False)
    user_id = Column(Integer, nullable=False)
    role = Column(String(50), nullable=False, default="admin")
    created_at = Column(DateTime, server_default=func.now())
    status = Column(String(50), default="active")

    # Relacion: StoreUser pertenece a una tienda
    store = relationship("Store", back_populates="users")