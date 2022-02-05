from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class League(Base):
    __tablename__ = 'leagues'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    country = Column(String)

    def __repr__(self):
        return f"<League(id={self.id}, name={self.name}, nickname={self.country})>"