import sqlite3

from sqlalchemy.orm import query
from db import db

class ItemModel(db.Model):
    __tablename__ = "items"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))
    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    store = db.relationship('StoreModel')
    def __init__(self, name, price, store_id):
        self.name = name
        self.price = price
        self.store_id = store_id

    def json(self):
        return {'name': self.name, 'price': self.price}

    @classmethod
    def find_by_name(cls, name):
        # connnection = sqlite3.connect('data.db')
        # cursor = connnection.cursor()
        
        # query = "SELECT * from items where name=?"
        # cursor.execute(query,(name,))
        # row = cursor.fetchone()
        # connnection.close()

        # if row:
        #     # return cls(row[0], row[1])   # it retuns the ItemModel object, here cls represents the class
        #     return cls(*row)  # we can pack it

        #SQLALchemy
        return  ItemModel.query.filter_by(name=name).first() # SELECT * from items where name= name limit 1
        # it translates table row to object


    def save_to_db(self):
    # def insert(self):
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()

        # query = "INSERT INTO items VALUES(?, ?)"
        # cursor.execute(query, (self.name, self.price))

        # connection.commit()
        # connection.close()       
        # 
        # SQL ALCHEMY
        db.session.add(self) # session represents here is a collection of object
        db.session.commit() 

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()


    # def update(self):
    #     connection = sqlite3.connect('data.db')
    #     cursor = connection.cursor()

    #     query = "UPDATE items SET price=? WHERE name=?"
    #     cursor.execute(query, (self.price, self.name))

    #     connection.commit()
    #     connection.close()    