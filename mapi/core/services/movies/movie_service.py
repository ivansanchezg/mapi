from typing import Any, AnyStr, Dict, List, Union
from mapi.api.exceptions import DuplicatedMovie, NotFound

class MovieService():
    def __init__(self) -> None:
        # TODO: Replace with a Database
        self.movies = []
        self._init_movies_list()

    def get_movies(self) -> List[Dict[AnyStr, Any]]:
        return self.movies

    # TODO: Use a Database
    def _init_movies_list(self):
        self.movies.append({
            'id': 1,
            'name': 'Titanic',
            'director': 'James Cameron',
            'year': 1997,
            'genres': ['Romance', 'Drama']
        })
        self.movies.append({
            'id': 2,
            'name': 'Deadpool',
            'director': 'Tim Miller',
            'year': 2016,
            'genres': ['Comedy', 'Action', 'SciFi']
        })
        self.movies.append({
            'id': 3,
            'name': 'The Lord of the Rings: The Fellowship of the Ring',
            'director': 'Peter Jackson',
            'year': 2001,
            'genres': ['Fantasy', 'Adventure']
        })