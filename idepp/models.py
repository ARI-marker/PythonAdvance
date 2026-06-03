from sqlalchemy import Column, Integer, String, Date, ForeignKey
from database import Base

class Application(Base):
    __tablename__ = "applications"

    id = Column(Integer, primary_key=True, index=True)
    company = Column(String)
    title = Column(String)
    status = Column(String)
    applied_date = Column(Date)
    notes = Column(String)