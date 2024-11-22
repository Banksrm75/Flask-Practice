"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User
from api.utils import generate_sitemap, APIException
from flask_cors import CORS

api = Blueprint('api', __name__)

# Allow CORS requests to this API
CORS(api)


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200

@api.route('/people', methods=['GET'])
def get_people():
    
    response_body = [
        {"name": "Luke", "age": 23},
        {"name": "Leia", "age": 23}
    ]

    return jsonify(response_body), 200

@api.route('/vehicles', methods=['POST', 'GET', 'PUT'])
def handle_vehicles():
    
    if request.method == 'POST':
        response = {"message": "We received a POST request." }
        return jsonify(response), 201
    elif request.method == 'GET':
        response = {"message": "We received a GET request." }
        return jsonify(response), 200
    else:
        response = {"message": "ERROR: Unable to process request." }
        return jsonify(response), 404
        

