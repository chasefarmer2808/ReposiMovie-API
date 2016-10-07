from resources.search_title import Search_Title

API_PREFIX = '/api/v1'
SEARCH_SUFFIX = '/search_title'

def init_routes(api):
    api.add_resource(Search_Title, API_PREFIX + SEARCH_SUFFIX)
