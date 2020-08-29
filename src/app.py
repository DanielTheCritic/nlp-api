import nlp
import api_versioning as ver
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

app=Flask(__name__)

print(__name__)

routePrefix = "/nlp-api/v1"

@app.route(routePrefix)
def get():
    result = "MIA BOT\nVersion: " + ver.getCurrentVersion()
    return result

@app.route(routePrefix, methods=['POST'])
def post():
    jsonRequest = request.json
    jsonResponse = nlp.request(jsonRequest)
    return jsonResponse
