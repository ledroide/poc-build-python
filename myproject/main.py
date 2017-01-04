import falcon
from waitress import serve
import logging
import sys

# logger and formatter setup
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s :: %(levelname)s :: %(message)s')
# standard outputs
stdout_handler = logging.StreamHandler(sys.stdout)
stdout_handler.setLevel(logging.DEBUG)
logger.addHandler(stdout_handler)
stderr_handler = logging.StreamHandler(sys.stderr)
stderr_handler.setLevel(logging.WARNING)
logger.addHandler(stderr_handler)
# testing the logger
logger.info('Starting sample API')

class Home:
    def on_get(self, req, resp):
        """Handles GET requests"""
        resp.status = falcon.HTTP_200
        resp.body = "PLATFORM - API Python " + str(sys.version_info.major) + "." + str(sys.version_info.minor)
        # logging test
        logger.info('{0} {1} {2} {3} {4}'.format(req.method, req.relative_uri, req.remote_addr, resp.status[:3], req.user_agent))
        logger.warning('{0} {1} {2}'.format('warning', resp.status[:15], resp.body[:30]))
 
api = falcon.API()

# Define routes
api.add_route('/', Home())

serve(api, host='*', port=8080)