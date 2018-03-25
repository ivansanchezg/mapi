from flask import Blueprint, jsonify, abort, request
from marshmallow import ValidationError

from mapi.api.schemas.movie import MovieSchema, MovieUpdateSchema
from mapi.api.exceptions import DuplicatedMovie, NotFound
from mapi.core.services.movies.movie_service import MovieService


movie_blueprint = Blueprint('movies', __name__)
movie_service = MovieService()


# TODO: Add pagination
@movie_blueprint.route('', methods=['GET'])
def movies():
    movies_list = movie_service.get_movies()
    return jsonify(MovieSchema(many=True).dump(movies_list))


