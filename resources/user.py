import sqlite3
from sqlite3.dbapi2 import connect
from flask_restful import Resource, reqparse
from models.user import UserModel



    # def __str__(self):
    #     return f"{self.username},{self.password}"    


class UserRegister(Resource):

    parser = reqparse.RequestParser()

    parser.add_argument('username',
        type=str,
        required=True,
        help="This field cannot be blank." 
    )
    
    parser.add_argument('password',
        type=str,
        required=True,
        help="This field cannot be blank." 
    )


    def post(self):
        data = UserRegister.parser.parse_args()
        
        if UserModel.find_by_username(data['username']):
            return "'message: A user with this name {} is already registered".format(data['username']), 400
        
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        
        # insert_query = "INSERT INTO users VALUES (NULL, ?, ?)"
        # cursor.execute(insert_query, (data['username'], data['password'], ))

        # connection.commit()
        # connection.close()
        user = UserModel(data['username'], data['password'])
        user.save_to_db()
        return {"message": "User is created Successfully!!!"}, 201   # success code 201 to state that it is created!


# -- before making as class method

# user = User(5,"gopi", "zxc")
# user.find_by_username("ram")

# -- after making as class method
# User.find_by_username("ram")
