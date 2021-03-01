#  Date: 2021.03.01
#  Author: dharapx
#  Feel free to use this code
#  --------------------------------------------------------------------------------------------
# A data model in a database should be relational which means it is described by tables.
# The data describes how the data is stored and organized.
# A data model may belong to one or more schemas, usually, it just belongs to one schema
#  --------------------------------------------------------------------------------------------
from sqlalchemy import Boolean, Column, Integer, String
from db_handler import Base


class Movies(Base):
    """
    This is a model class. which is having the movie table structure with all the constraint
    """
    __tablename__ = "movie"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True, nullable=False)
    movie_id = Column(String, unique=True, index=True, nullable=False)
    movie_name = Column(String(255), index=True, nullable=False)
    director = Column(String(100), index=True, nullable=False)
    geners = Column(String, index=True, nullable=False)
    membership_required = Column(Boolean, nullable=False, default=True)
    cast = Column(String(255), index=True, nullable=False)
    streaming_platform = Column(String, index=True)
