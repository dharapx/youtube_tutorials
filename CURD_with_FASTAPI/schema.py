#  Date: 2021.03.01
#  Author: dharapx
#  Feel free to use this code
#  --------------------------------------------------------------------------------
# A schema is a collection of database objects that are logically grouped together.
# These can be anything, tables, views, stored procedure etc.
# Schemas are typically used to logically group objects in a database.
#  ---------------------------------------------------------------------------------
from typing import Optional
from pydantic import BaseModel


class MovieBase(BaseModel):
    movie_name: str
    director: str
    geners: str
    cast: str


class MovieAdd(MovieBase):
    movie_id: str
    # Optional[str] is just a shorthand or alias for Union[str, None].
    # It exists mostly as a convenience to help function signatures look a little cleaner.
    streaming_platform: Optional[str] = None
    membership_required: bool

    # Behaviour of pydantic can be controlled via the Config class on a model
    # to support models that map to ORM objects. Config property orm_mode must be set to True
    class Config:
        orm_mode = True


class Movie(MovieAdd):
    id: int

    # Behaviour of pydantic can be controlled via the Config class on a model
    # to support models that map to ORM objects. Config property orm_mode must be set to True
    class Config:
        orm_mode = True


class UpdateMovie(BaseModel):
    # Optional[str] is just a shorthand or alias for Union[str, None].
    # It exists mostly as a convenience to help function signatures look a little cleaner.
    streaming_platform: Optional[str] = None
    membership_required: bool

    # Behaviour of pydantic can be controlled via the Config class on a model
    # to support models that map to ORM objects. Config property orm_mode must be set to True
    class Config:
        orm_mode = True
