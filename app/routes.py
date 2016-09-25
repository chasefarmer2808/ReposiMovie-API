from resources.message import Message

def init_routes(api):
    api.add_resource(Message, '/')
