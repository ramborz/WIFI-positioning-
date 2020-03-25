from flask import Flask
from flask import jsonify
from flask import make_response
from flask import request
import json
from WIFI import database

app = Flask(__name__)

@app.route('/api/name', methods=["GET"])
def get_allname():
    return jsonify(database.get_all())

@app.route("/api/name/<name>", methods=["GET"])
def get_name(BSSID):
    try:
        if BSSID is None:
            raise ValueError("ID not specified.")
        x = database.get_name(BSSID)
        if x is None:
            return make_response("No found wifi name", 404)
        return jsonify(x)
    except ValueError as e:
        return make_response(str(e), 400)
    except Exception as e:
        return make_response(str(e), 500)

@app.route("/api/cord", methods=["GET"])
def get_cord(BSSID):
    try:
        if BSSID is None:
            raise ValueError("ID not specified.")
        x = database.get_cord(BSSID)
        if x is None:
            return make_response("No found wifi name", 404)
        return jsonify(x)
    except ValueError as e:
        return make_response(str(e), 400)
    except Exception as e:
        return make_response(str(e), 500)


@app.route("/api/label", methods=["GET"])
def get_label(BSSID):
    try:
        if BSSID is None:
            raise ValueError("ID not specified.")
        x = database.get_label(BSSID)
        if x is None:
            return make_response("No found wifi name", 404)
        return jsonify(x)
    except ValueError as e:
        return make_response(str(e), 400)
    except Exception as e:
        return make_response(str(e), 500)