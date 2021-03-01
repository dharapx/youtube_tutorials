#  Date: 2021.03.01
#  Author: dharapx
#  Feel free to use this code
#  ------------------------------------------------------------------------------------------------
# This is an API. which are having four end points to perform the CRUD operation with SQLite
#  ------------------------------------------------------------------------------------------------
from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud
import model
import schema
from db_handler import SessionLocal, engine

model.Base.metadata.create_all(bind=engine)

# initiating app
app = FastAPI(
    title="Movie Details",
    description="You can perform CRUD operation by using this API",
    version="1.0.0"
)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/retrieve_all_movies_details', response_model=List[schema.Movie])
def retrieve_all_movies_details(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    movies = crud.get_movies(db=db, skip=skip, limit=limit)
    return movies


@app.post('/add_new_movie', response_model=schema.MovieAdd)
def add_new_movie(movie: schema.MovieAdd, db: Session = Depends(get_db)):
    movie_id = crud.get_movie_by_movie_id(db=db, movie_id=movie.movie_id)
    if movie_id:
        raise HTTPException(status_code=400, detail=f"Movie id {movie.movie_id} already exist in database: {movie_id}")
    return crud.add_movie_details_to_db(db=db, movie=movie)


@app.delete('/delete_movie_by_id')
def delete_movie_by_id(sl_id: int, db: Session = Depends(get_db)):
    details = crud.get_movie_by_id(db=db, sl_id=sl_id)
    if not details:
        raise HTTPException(status_code=404, detail=f"No record found to delete")

    try:
        crud.delete_movie_details_by_id(db=db, sl_id=sl_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Unable to delete: {e}")
    return {"delete status": "success"}


@app.put('/update_movie_details', response_model=schema.Movie)
def update_movie_details(sl_id: int, update_param: schema.UpdateMovie, db: Session = Depends(get_db)):
    details = crud.get_movie_by_id(db=db, sl_id=sl_id)
    if not details:
        raise HTTPException(status_code=404, detail=f"No record found to update")

    return crud.update_movie_details(db=db, details=update_param, sl_id=sl_id)
