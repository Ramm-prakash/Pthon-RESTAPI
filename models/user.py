import sqlite3
from db import db

class UserModel(db.Model):

    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))


    def __init__(self, username, password):
        # self.id = _id
        self.username = username
        self.password = password
    
    # def find_by_username(self, username): since self is not used inside method, we use make this as class method

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):    
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        # select_query = "SELECT * FROM users where username=?"
        # result = cursor.execute(select_query, (username,)) # here username should be passed as tuple
        # row = result.fetchone()
        # if row is not None:
        #     # print(row[0], row[1], row[2])
        #     user = cls(*row) # *row will unpack the tuple
        # else:
        #     user = None        
        # connection.close()
        # return user
        return cls.query.filter_by(username=username).first()
    
    @classmethod
    def find_by_id(cls, _id):    
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        # select_query = "SELECT * FROM users where id=?"
        # result = cursor.execute(select_query, (_id,)) # here username should be passed as tuple
        # row = result.fetchone()
        # if row is not None:
        #     # print(row[0], row[1], row[2])
        #     user = cls(*row) # *row will unpack the tuple
        # else:
        #     user = None        
        # connection.close()
        # return user
        return cls.query.filter_by(id=_id).first()