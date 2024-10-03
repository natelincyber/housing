# app/views/main.py

from flask import Blueprint, render_template, request, jsonify
from app.models import HousingOption
from app.utils.helpers import filter_housing_options

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/housing')
def get_housing():
    # Fetch query parameters
    price_min = request.args.get('price_min', type=float)
    price_max = request.args.get('price_max', type=float)
    distance = request.args.get('distance', type=float)
    # Add other filters as needed

    # Query database
    query = HousingOption.query
    if price_min is not None:
        query = query.filter(HousingOption.price >= price_min)
    if price_max is not None:
        query = query.filter(HousingOption.price <= price_max)
    if distance is not None:
        query = query.filter(HousingOption.distance_to_college <= distance)
    # Apply other filters

    housing_options = query.all()
    # Serialize data
    data = [ho.to_dict() for ho in housing_options]
    return jsonify(data)
