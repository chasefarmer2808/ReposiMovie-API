from flask_restful import Resource, reqparse

from queries.movies_by_genre import get_movie_by_genre

class Search_Genre(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('genre', action='append')
        parser.add_argument('limit', type=int)
        args = parser.parse_args()

        movies = get_movie_by_genre(list(set(args['genre'])), args['limit'])

        return movies