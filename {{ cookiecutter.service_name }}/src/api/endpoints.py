import os
from datetime import datetime
from flask import Blueprint
from flask import make_response
from flask import request
from http import HTTPStatus
import json

from config import BASE_DIR
from config import logger

# Define blueprint
_api = Blueprint('_api', __name__)

# Health check
@_api.route('/{{ cookiecutter.service_name }}/health', methods=['GET'])
def _health_check():
    """Health check."""
    # Construct response
    response = {
        'message': HTTPStatus.OK.phrase,
        'method': request.method,
        'status-code': HTTPStatus.OK,
        'timestamp': datetime.now().isoformat(),
        'url': request.url,
    }

    # Log
    logger.info(json.dumps(response, indent=4))
    return make_response(jsonify(response), response['status-code'])
