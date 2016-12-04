from flask_restful import Resource, reqparse

from queries.movie_id import get_movie_by_id

class Movie_Id(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('movie_id', default='0')
        args = parser.parse_args()

        movie = get_movie_by_id(args['movie_id'])

        return movie
