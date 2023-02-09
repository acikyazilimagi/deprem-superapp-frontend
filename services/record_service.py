import os

from helpers.http_helpers import http_helper
def SendHelpCall(params):
    http_helper.send_request(os.getenv("API_BASE_URL"),method="POST",body_params=params)
    pass
