# This model defines how contact form submissions will be stored in MySQL.

from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.sql import func

from app.database import Base



class Contact(Base):
    __tablename__ = "contacts"
    
    id = Column(Integer, primary_key=True, nullable=False, index=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    message = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    