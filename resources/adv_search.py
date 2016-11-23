import datetime

from flask_restful import Resource, reqparse, abort

DATE_FORMAT = '%m-%d-%Y'

class Adv_Search(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('title', default="%")
        parser.add_argument('startDate', required=True)
        parser.add_argument('endDate', required=True)
        parser.add_argument('avgRating', default='0>')
        parser.add_argument('ratingCount', default='0>')
        parser.add_argument('revenue', default='0>')
        parser.add_argument('budget', default='0>')
        parser.add_argument('runtime', default='0>')
        parser.add_argument('genres', action='append', default=[])
        parser.add_argument('companies', action='append', default=[])
        parser.add_argument('people', action='append', default=[])
        parser.add_argument('limit', type=int)
        args = parser.parse_args()

        args['startDate'] = datetime.datetime.strptime(args['startDate'], DATE_FORMAT)
        args['endDate'] = datetime.datetime.strptime(args['endDate'], DATE_FORMAT)

        if args['startDate'] > args['endDate']:
            abort(400, message='Start date must be before End date')

        args['avgRating'] = {
            'value': args['avgRating'][0:len(args['avgRating'])-1],
            'equality': args['avgRating'][len(args['avgRating'])-1]
        }
        args['ratingCount'] = {
            'value': args['ratingCount'][0:len(args['ratingCount']) - 1],
            'equality': args['ratingCount'][len(args['ratingCount']) - 1]
        }
        args['revenue'] = {
            'value': args['revenue'][0:len(args['revenue']) - 1],
            'equality': args['revenue'][len(args['revenue']) - 1]
        }
        args['budget'] = {
            'value': args['budget'][0:len(args['budget']) - 1],
            'equality': args['budget'][len(args['budget']) - 1]
        }
        args['runtime'] = {
            'value': args['runtime'][0:len(args['runtime']) - 1],
            'equality': args['runtime'][len(args['runtime']) - 1]
        }

        print(args)

        return