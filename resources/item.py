import sqlite3
from sqlite3.dbapi2 import connect
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel


class Item(Resource):
    parser = reqparse.RequestParser()
        # parser will parse through JSON/Form payload
    parser.add_argument('price',
            type=float,
            required=True,
            help='This field cannot left blank'
        )
    parser.add_argument('store_id',
            type=int,
            required=True,
            help='Every item need a store id'
        )    
    @jwt_required() # it requires jwt token before the following method executes
    def get(self, name):

        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {'message': 'Item not found'}, 404    

    def post(self, name):
        # data = request.get_json(force=True) # force=True makes formatting without content-type is set as application/json
                                            # slience=True, it wont give any error
        if ItemModel.find_by_name(name):
            return {'message': "the request item '{}' is already present".format(name)}, 400
        #data = request.get_json()
        data = Item.parser.parse_args()
        item = ItemModel(name, data['price'], data['store_id'])
        try:
            item.save_to_db()
        except:
            return {"message": "An error occurred inserting the item"}, 500 # Internal Server Error   
        return item.json(), 201   # 200 - Returns something, 201 - Created, 202 - Delaying the creation. 
    
    def delete(self, name):
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()

        # query = "DELETE FROM items where name=?"
        # cursor.execute(query, (name,))

        # connection.commit()
        # connection.close()
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()    
        return {'message': 'item deleted'}

    def put(self, name):   
        # data = request.get_json()
        data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)
        # updated_item = ItemModel(name, data['price'])
        if item is None:  
            item = ItemModel(name, data['price'], data['store_id'])
            # try:
            #     updated_item.insert()
            # except:
            #     return {"message": "An error occurred inserting an item"}, 500    
        else:
            item.price = data['price']
            # try:
            #     updated_item.update()
            # except:
            #     return {"message": "An error occurred updating the item"}, 500 
        item.save_to_db()  
        return item.json()   
        # return updated_item.json()  


class ItemList(Resource):
    def get(self):
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()

        # query = "SELECT * FROM items"
        # result = cursor.execute(query)
        # items = []

        # for row in result:
        #     items.append({'name': row[0] ,'price': row[1]})
        # connection.commit()
        # connection.close()
        # return {'items': items}
        # return {'items': [item.json() for item in ItemModel.query.all()]}
        return {'items': list(map(lambda x: x.json(),ItemModel.query.all()))}