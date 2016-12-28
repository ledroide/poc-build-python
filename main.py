import falcon
from waitress import serve
 
class Home:
    def on_get(self, req, resp):
        """Handles GET requests"""
        resp.body = "PLATFORM - API Python 2.*"
 
api = falcon.API()

# Define routes
api.add_route('/', Home())

# 
serve(api, host='*', port=8080)