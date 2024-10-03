from flask import Blueprint, jsonify
from app.models import HousingOption

api = Blueprint('api', __name__)

@api.route('/housing')
def api_housing():
    housing_options = HousingOption.query.all()
    data = [ho.to_dict() for ho in housing_options]
    return jsonify(data)

# Add more API routes as needed
