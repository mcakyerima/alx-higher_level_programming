#!/usr/bin/python3
"""
Defines the State class.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class State(Base):
    """
    Represents a state, linked to the cities table.
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, nullable=False, unique=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state")

    def __repr__(self):
        """
        Return a string representation of the State object.
        """
        return f"State(id={self.id}, name='{self.name}')"
