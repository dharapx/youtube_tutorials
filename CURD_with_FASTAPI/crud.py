from sqlalchemy import update
from sqlalchemy.orm import Session
import model
import schema


def get_movie_by_movie_id(db: Session, movie_id: str):
    return db.query(model.Movies).filter(model.Movies.movie_id == movie_id).first()


def get_movie_by_id(db: Session, sl_id: int):
    return db.query(model.Movies).filter(model.Movies.id == sl_id).first()


def get_movies(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model.Movies).offset(skip).limit(limit).all()


def add_movie_details_to_db(db: Session, movie: schema.MovieAdd):
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

    movie_details = db.query(model.Movies).filter(model.Movies.id == sl_id).first()

    if movie_details is None:
        return None

    db.query(model.Movies).filter(model.Movies.id == sl_id).update(vars(details))
    db.commit()
    return db.query(model.Movies).filter(model.Movies.id == sl_id).first()


def delete_movie_details_by_id(db: Session, sl_id: int):
    try:
        db.query(model.Movies).filter(model.Movies.id == sl_id).delete()
        db.commit()
    except Exception as e:
        raise Exception(e)



