from flask_restful import Resource

class Message(Resource):
    def get(self):
        ret = {}
        ret['message'] = 'hello'

        return ret