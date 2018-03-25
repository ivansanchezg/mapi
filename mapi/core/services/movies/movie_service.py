from typing import Any, AnyStr, Dict, List, Union
from mapi.api.exceptions import DuplicatedMovie, NotFound

class MovieService():
    def __init__(self) -> None:
        # TODO: Replace with a Database
        self.movies = []
        self._init_movies_list()
        self.id_counter = len(self.movies) + 1

    def get_movies(self) -> List[Dict[AnyStr, Any]]:
        return self.movies

    def get_movie(self, movie_id: int) -> Dict[AnyStr, Any]:
        for movie in self.movies:
            if movie['id'] == movie_id:
                return movie
        raise NotFound()

    def add_movie(self, data: Dict[AnyStr, Any]) -> Dict[AnyStr, Any]:
        for movie in self.movies:
            if movie['name'] == data['name'] and movie['year'] == data['year']:
                raise DuplicatedMovie()

        data['id'] = self.id_counter
        self.id_counter += 1
        self.movies.append(data)
        return data

    def update_movie(self, movie_id: int, data: Dict[AnyStr, Any]) -> Dict[AnyStr, Any]:
        index = self._get_movie_index(movie_id)
        if index is None:
            raise NotFound()
        
        for key in data:
            self.movies[index][key] = data[key]
        
        return self.movies[index]

    def delete_movie(self, movie_id) -> Dict[AnyStr, Any]:
        index = self._get_movie_index(movie_id)
        if index is None:
            raise NotFound()

        movie = self.movies[index]
        del self.movies[index]
        return movie      

    def _get_movie_index(self, movie_id) -> Union[int, None]:
        for index, movie in enumerate(self.movies):
            if movie['id'] == movie_id:
                return index
        return None

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