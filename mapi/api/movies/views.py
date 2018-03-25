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


@movie_blueprint.route('/<int:movie_id>')
def get_movie(movie_id):
    try:
        movie = movie_service.get_movie(movie_id)
    except NotFound:
        abort(404)

    return jsonify(MovieSchema().dump(movie))

@movie_blueprint.route('', methods=['POST'])
def add_movie():
    try:
        data = MovieSchema().load(request.get_json())
    except ValidationError:
        abort(400)

    try:
        movie = movie_service.add_movie(data)
    except DuplicatedMovie:
        abort(400)

    return jsonify(MovieSchema().dump(movie)), 201