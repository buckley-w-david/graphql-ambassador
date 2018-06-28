from flask import Blueprint
from flask import request, Response
from flask import current_app as app
import requests

proxy = Blueprint('proxy', __name__)

def _proxy(host, path):
    print(requests.compat.urljoin(host, path))
    resp = requests.request(
        method=request.method,
        url=requests.compat.urljoin(host, path),
        headers={key: value for (key, value) in request.headers if key != 'Host'},
        data=request.get_data(),
        cookies=request.cookies,
        allow_redirects=False)

    excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
    headers = [(name, value) for (name, value) in resp.raw.headers.items()
               if name.lower() not in excluded_headers]

    return resp, headers

@proxy.route('/', defaults={'path': ''})
@proxy.route('/<path:path>')
def ambassador(path):
    resp, headers = _proxy(app.config.get('PROXY_SITE'), path)
    response = Response(resp.content, resp.status_code, headers)
    return response
