from flask import Flask, jsonify, abort
from flask_cors import CORS

days = [
    {"id": 1, "name": "Monday"},
    {"id": 2, "name": "Tuesday"},
    {"id": 3, "name": "Wednesday"},
    {"id": 4, "name": "Thursday"},
    {"id": 5, "name": "Friday"},
    {"id": 6, "name": "Saturday"},
    {"id": 7, "name": "Sunday"},
]

app = Flask(__name__)
#CORS(app)
#commented above to confirm if the lack of CORS is causing error when accessing after deployment to ECS 

@app.route("/", methods=["GET"])
def get_days():
    return jsonify(days)


@app.route("/<int:day_id>", methods=["GET"])
def get_day(day_id):
    day = [day for day in days if day["id"] == day_id]
    if len(day) == 0:
        abort(404)
    return jsonify({"day": day[0]})


@app.route("/", methods=["POST"])
def post_days():
    return jsonify({"success": True}), 201


if __name__ == "__main__":
    # app.run(debug=True) 
    # Commented the above line and inserted the below
    app.run(host='0.0.0.0', port=80)
