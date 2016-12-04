from flask_restful import Resource, reqparse

from queries.people_by_name import get_people_by_name

class Search_Name(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', default="'%'")
        parser.add_argument('limit', type=int, default=0)
        args = parser.parse_args()

        names = get_people_by_name(args['name'], args['limit'])

        return names
