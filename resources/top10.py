from flask_restful import Resource, reqparse

from queries.top10 import get_top10
from queries.top10_box import get_top10_box
from queries.top10_box_year import get_top10_box_year
from queries.top10_genres import get_top10_genres
from queries.top10_worst import get_top10_worst

class Top10(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('option', default=True)
        parser.add_argument('year', default = '%2015%')
        args = parser.parse_args()

        top10movies = {}

        if args['option'] == 'top10':
            top10movies = get_top10()
        elif args['option'] == 'top10_box':
            top10movies = get_top10_box()
        elif args['option'] == 'top10_box_year':
            top10movies = get_top10_box_year(args['year'])
        elif args['option'] == 'top10_genres':
            top10movies = get_top10_genres()
        elif args['option'] == 'top10_worst':
            top10movies = get_top10_worst()

        return top10movies