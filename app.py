from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList   # since store will import StoreModel, store table will be created by SQLAchemy automatically

app = Flask(__name__)   

# It just disable the Flask SQLAlchemy track modification, but SQLAlchemy track is enabled by default. 
# it is tracking changes to SQLAchemy session 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db' # SQLALCHEMY works with MYSQL, Postgers SQL as well
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'ram'   # this key is used to encode or decode token
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()


jwt = JWT(app, authenticate, identity)   # it creats /auth as endpoint, it validates user using authenticate function and it returns jwt token

# when jwt is used, it calls identify function, it will identify user. If it can identify user, then jwt token is authenticated




api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(StoreList, '/stores')
api.add_resource(UserRegister, '/register')

if __name__== '__main__':  # which means that app.run only run when we run app.py application, it wont run when we import app.py in another module
    # when we run using python app.py, python assigns a special name "__main__" to that file

    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)