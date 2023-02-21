from db_init import db
from flask import Flask
import psycopg2
from shop.shop_endpoints import shop

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(user='youben',pw='123',url='localhost',db='gotest')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # silence the deprecation warning

db.init_app(app)

app.register_blueprint(shop)

with app.app_context():
    db.create_all()


@app.route('/', methods=['GET'])
def home():
    return "welcome to the plic test api"


app.run(host='0.0.0.0', port=8080, debug=False)