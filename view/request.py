from flask import Blueprint, jsonify, request
from classes.request import UserRequest


request_bp = Blueprint('request_bp', __name__)


@request_bp.route("/perform_query", methods=['POST'])
def perform_query():
    data = request.json
    user_request = UserRequest(data)
    return jsonify(user_request.create_procedure())
