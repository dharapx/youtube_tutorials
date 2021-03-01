#  Date: 2021.03.01
#  Author: dharapx
#  Feel free to use this code
#  -------------------------------------------------------------------------------
#  Here we are having methods for CRUD operation
#  -------------------------------------------------------------------------------

from sqlalchemy.orm import Session
import model
import schema


def get_movie_by_movie_id(db: Session, movie_id: str):
    """
    This method will return single movie details based on movie_id
    :param db: database session object
    :param movie_id: movie id only
    :return: data row if exist else None
    """
    return db.query(model.Movies).filter(model.Movies.movie_id == movie_id).first()


def get_movie_by_id(db: Session, sl_id: int):
    """
    This method will return single movie details based on id
    :param db: database session object
    :param sl_id: serial id of record or Primary Key
    :return: data row if exist else None
    """
    return db.query(model.Movies).filter(model.Movies.id == sl_id).first()


def get_movies(db: Session, skip: int = 0, limit: int = 100):
    """
    This method will return all movie details which are present in database
    :param db: database session object
    :param skip: the number of rows to skip before including them in the result
    :param limit: to specify the maximum number of results to be returned
    :return: all the row from database
    """
    return db.query(model.Movies).offset(skip).limit(limit).all()


def add_movie_details_to_db(db: Session, movie: schema.MovieAdd):
    """
    this method will add a new record to database. and perform the commit and refresh operation to db
    :param db: database session object
    :param movie: Object of class schema.MovieAdd
    :return: a dictionary object of the record which has inserted
    """
    mv_details = model.Movies(
        movie_id=movie.movie_id,
        movie_name=movie.movie_name,
        director=movie.director,
        geners=movie.geners,
        membership_required=movie.membership_required,
        cast=movie.cast,
        streaming_platform=movie.streaming_platform
    )
    db.add(mv_details)
    db.commit()
    db.refresh(mv_details)
    return model.Movies(**movie.dict())


def update_movie_details(db: Session, sl_id: int, details: schema.UpdateMovie):
    """
    this method will update the database
    :param db: database session object
    :param sl_id: serial id of record or Primary Key
    :param details: Object of class schema.UpdateMovie
    :return: updated movie record
    """
    db.query(model.Movies).filter(model.Movies.id == sl_id).update(vars(details))
    db.commit()
    return db.query(model.Movies).filter(model.Movies.id == sl_id).first()


def delete_movie_details_by_id(db: Session, sl_id: int):
    """
    This will delete the record from database based on primary key
    :param db: database session object
    :param sl_id: serial id of record or Primary Key
    :return: None
    """
    try:
        db.query(model.Movies).filter(model.Movies.id == sl_id).delete()
        db.commit()
    except Exception as e:
        raise Exception(e)
