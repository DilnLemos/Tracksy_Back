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
    store_users = relationship("StoreUser", back_populates="store")

class StoreUser(Base):
    __tablename__ = "store_users"

    id = Column(Integer, primary_key=True, index=True)
    store_id = Column(Integer, ForeignKey("stores.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)  # ← ya no es temporal
    role = Column(String, default="member")
    status = Column(String, default="active")
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Relaciones
    store = relationship("Store", back_populates="store_users")
    user = relationship("User", back_populates="store_users")