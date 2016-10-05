from resources.search import Search

SEARCH_SUFFIX = '/search'

def init_routes(api):
    api.add_resource(Search, SEARCH_SUFFIX)
