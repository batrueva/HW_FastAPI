from fastapi import APIRouter, FastAPI, HTTPException, Query
from models import Movie

router = APIRouter()

movie_list = [
    Movie(title="Film1", year=1999, description="The film of 1"),
    Movie(title="Film2", year=1991, description="The film of 2"),
    Movie(title="Film5", year=1992, description="The film of 3"),
    Movie(title="Film4", year=1993, description="The film of 4"),
    Movie(title="Film5", year=1993, description="The film of 5")
]


@router.get("/movies/", response_model=list[Movie])
def get_movies(
    year: int = Query(None, description="The year of movies"),
    title: str = Query(None, description="The title of movies")
):
    """"""
    result = movie_list
    if year is not None:
        result = [movie for movie in result if movie.year == year]
    if title is not None:
        result = [movie for movie in result if movie.title == title]
    return result


@router.get("/movies/{movie_id}", response_model=Movie)
def get_movie_by_id(movie_id: int):
    """получить информацию по фильму"""
    if movie_id < 0 or movie_id >= len(movie_list):
        raise HTTPException(status_code=404, detail="Movie not found")
    else:
        return movie_list[movie_id]


@router.post("/movies/", response_model=Movie, status_code=201)
def create_movie(movie: Movie):
    """добавить новый фильм."""
    for m in movie_list:
        if m.title == movie.title and m.year == movie.year:
            raise HTTPException(status_code=409, detail="Такой фильм есть")
    movie_list.append(movie)
    return movie


@router.put("/movies/{movie_id}")
def edit_movie(movie_id: int, movie: Movie):
    """добавить новый фильм."""
    if movie_id < 0 or movie_id >= len(movie_list):
        raise HTTPException(status_code=404, detail="Movie not found")
    movie_list[movie_id] = movie
    return movie_list[movie_id]


@router.delete("/movies/{movie_id}")
def delete_movie(movie_id: int):
    """добавить новый фильм."""
    if movie_id < 0 or movie_id >= len(movie_list):
        raise HTTPException(status_code=404, detail="Movie not found")

    return movie_list.pop(movie_id)
