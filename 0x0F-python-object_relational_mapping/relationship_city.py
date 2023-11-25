#!/usr/bin/python3
"""
This Schema Defines the City class.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from relationship_state import Base, State

class City(Base):
    """
    Represents a city, linked to the states table.
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, nullable=False, unique=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey(State.id), nullable=False)
    state = relationship("State", back_populates="cities")

    def __repr__(self):
        """
        Return a string representation of the City object.
        """
        return f"City(id={self.id}, name='{self.name}', state_id={self.state_id})"
