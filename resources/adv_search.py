import datetime

from flask_restful import Resource, reqparse, abort
from queries.adv_search import get_movies_advanced

DATE_FORMAT = '%m-%d-%Y'

class Adv_Search(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('title', default="%")
        parser.add_argument('startDate', required=True)
        parser.add_argument('endDate', required=True)
        parser.add_argument('avgRating', default='0 >')
        parser.add_argument('ratingCount', default='0 >')
        parser.add_argument('revenue', default='0 >')
        parser.add_argument('budget', default='0 >')
        parser.add_argument('runtime', default='0 >')
        parser.add_argument('genres', action='append', default=[])
        parser.add_argument('companies', action='append', default=[])
        parser.add_argument('people', action='append', default=[])
        parser.add_argument('limit', type=int)
        args = parser.parse_args()

        convert = datetime.datetime.strptime

        if convert(args['startDate'], DATE_FORMAT) > convert(args['endDate'], DATE_FORMAT):
            return []

        return args,
