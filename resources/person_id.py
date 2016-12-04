from flask_restful import Resource, reqparse

from queries.person_id import get_person_by_id

class Person_Id(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('person_id', default='0')
        args = parser.parse_args()

        person = get_person_by_id(args['person_id'])

        return person
