from flask import Blueprint, jsonify, request
import requests

GEOCODING_KEY = "key"
GEOCODING_URL = "https://api.opencagedata.com/geocode/v1/json?key=e7f0b2b866d54fe39643e22b6ee94eb0&q="

api = Blueprint("api", __name__)


@api.route('/geocoding', methods=["GET"])
def hello_world():
    key = request.args["key"]
    if key != GEOCODING_KEY:
        return "Access denied wrong key!"
    lat = request.args["lat"]
    lng = request.args["lng"]
    data = requests.get(GEOCODING_URL + lat + "+" + lng)
    try:
        response = jsonify({"country": data.json()["results"][0]["components"]["country"]})
    except IndexError:
        response = jsonify({"country": None})
    return response
