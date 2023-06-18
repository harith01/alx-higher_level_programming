#!/usr/bin/python3
"""Defines a City model."""

from model_state import Base
from sqlalchemy import Column, String, Integer, Sequence, ForeignKey


class City(Base):
    """City Class Definition

    Attributes:
        id (Integer): id
        name (String): City's name
        state_id (String): City's id
    """

    __tablename__ = 'cities'

    id = Column(Integer, Sequence('cities_id'), nullable=False,
                primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
