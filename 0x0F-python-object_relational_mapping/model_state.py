#!/usr/bin/python3
"""Contains the class definition of a State and
   an instance Base = declarative_base()"""

from sqlalchemy import Column, String, Integer, Sequence
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """State class definition"""

    __tablename__ = 'states'

    id = Column(Integer, Sequence('state_id_seq'), primary_key=True,
                nullable=False, unique=True)
    name = Column(String(128), nullable=False)
