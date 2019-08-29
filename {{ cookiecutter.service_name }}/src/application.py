import os
from flask import Flask
from flask import jsonify
from flask import make_response
from flask import request
from http import HTTPStatus

from {{ cookiecutter.package_name }}.config import DevelopmentConfig
from {{ cookiecutter.package_name }}.config import ProductionConfig
from {{ cookiecutter.package_name }}.api.endpoints import _api

# Define Flask app
application = Flask(__name__)
application.url_map.strict_slashes = False
application.config['JSON_SORT_KEYS'] = False

# Configurations
config = {
    'dev': 'config.DevelopmentConfig',
    'prod': 'config.ProductionConfig',
}
config_name = os.getenv('ENV', 'dev')
application.config.from_object(config[config_name])

# Register blueprints
application.register_blueprint(_api)

# BAD_REQUEST
@application.errorhandler(400)
def bad_request(error):
    """Redirect all bad requests."""
    response = {
        "message": HTTPStatus.BAD_REQUEST.phrase,
        "method": request.method,
        "status-code": HTTPStatus.BAD_REQUEST,
        "url": request.url,
    }
    return make_response(jsonify(response), response["status-code"])

# NOT_FOUND
@application.errorhandler(404)
def not_found(error):
    """Redirect all nonexistent URLS."""
    response = {
        "message": HTTPStatus.NOT_FOUND.phrase,
        "method": request.method,
        "status-code": HTTPStatus.NOT_FOUND,
        "url": request.url,
    }
    return make_response(jsonify(response), response["status-code"])

# INTERNAL_SERVER_ERROR
@application.errorhandler(500)
def internal_server_error(error):
    """Internal server error."""
    response = {
        "message": HTTPStatus.INTERNAL_SERVER_ERROR.phrase,
        "method": request.method,
        "status-code": HTTPStatus.INTERNAL_SERVER_ERROR,
        "url": request.url,
    }
    return make_response(jsonify(response), response["status-code"])
