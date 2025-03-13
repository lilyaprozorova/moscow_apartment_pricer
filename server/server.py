from flask import Flask, request, jsonify
import util
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/get_categories_names', methods=['GET'])
def get_location_names():
    response = jsonify(util.get_categories_names())
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/predict_home_price', methods=['GET', 'POST'])
def predict_home_price():
    print("message sent")
    house_age = 2024 - float(request.form['house_year'])
    dist_to_subway = float(request.form['dist_to_subway'])
    subway_type = float(request.form['subway_type']) - 1
    rooms = int(request.form['rooms'])
    
    footage = float(request.form['footage'])
    floor = int(request.form['floor'])
    print(4)
    max_floor = int(request.form['max_floor'])
    print(3)
    dist_to_center = float(request.form['dist_to_center'])
    print(3)
    area = request.form['area']
    print(1)
    material = request.form['material']
    print(2)

    response = jsonify({
        'estimated_price': util.get_estimated_price(
            house_age, dist_to_subway, subway_type, rooms, footage,
            floor, max_floor,
            dist_to_center, area, material
        )
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    app.run()