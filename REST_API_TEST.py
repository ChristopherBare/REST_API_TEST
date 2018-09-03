from flask import Flask
from flask_restful import Api, Resource, reqparse
from flask import Flask, request



app = Flask(__name__)
api = Api(app)

users = [
    {
    "name": "Christopher Bare",
    "age": 24,
    "occupation": "It's Complicated."
    },
    {
    "name": "Doodle Bob",
    "age": 37,
    "occupation": "It's different."
    },
    {
    "name": "Dingle B00b",
    "age": 38,
    "occupation": "It's exaggerated."
    }
]


class Users(Resource):
    def get(self):
        return users

class User(Resource):
    def get(self, name):
        for user in users:
            if name == user["name"]:
                return user, 200
        return "User Not FOUND", 404

    def post(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("age")
        parser.add_argument("occupation")
        args = parser.parse_args()

        for user in users:
            if (name == user["name"]):
                return "User with name {} already exists.".format(name), 400
        user = {
        "name": name,
        "age": args["age"],
        "occupation": args["occupation"]
        }
        users.append(user)
        return user, 201

    def put(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("age")
        parser.add_argument("occupation")
        args = parser.parse_args()

        for user in users:
            if name == user["name"]:
                user["age"] = args["age"]
                user["occupation"] = args["occupation"]
                return user, 200
        user = {
        "name": name,
        "age": args["age"],
        "occupation": args["occupation"]
        }
        users.append(user)
        return user, 201

    def delete(self, name):
        global users
        users = [user for user in users if user["name"] != name]
        return "{} is deleted.".format(name), 200


api.add_resource(User, "/user/<string:name>")
api.add_resource(Users, "/users")


app.run(debug=True)
