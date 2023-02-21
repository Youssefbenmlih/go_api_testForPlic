from flask import request, Blueprint
from flask import jsonify
from datetime import datetime
from db_init import db
from dataclasses import dataclass

@dataclass
class Shop(db.Model):
    id: int
    nb_customers : int

    id = db.Column(db.Integer, primary_key=True)
    nb_customers = db.Column(db.Integer)

    def __repr__(self):
        return f"nb_customers: {self.nb_customers}"


shop = Blueprint('shop', __name__, template_folder='templates')


# LIST ALL PUBLIC ROWS

@shop.route('/api/shop/list', methods=['GET'])
def get_shops():
    list = Shop.query.all()
    for shop in list:
        print(shop)
    return jsonify(list), 200

"""
JSON Content:
{
    "nb_customers": 13
}
"""

@shop.route('/api/shop/add', methods=['POST'])
def add_shop():
    r = request.get_json()
    new_shop = Shop(nb_customers=r['nb_customers'])
    try:
        db.session.add(new_shop)
        db.session.commit()
    except Exception as e:
        print(e)
        return "Shop could not be added.", 400
    return "Shop Added !", 200

