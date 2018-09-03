from flask import Flask
from flask_restful import Api, Resource, reqparse
from flask import Flask, request



app = Flask(__name__)
api = Api(app)

users = [
    {
        "id": 0,
        "name": "Casey Bean",
        "company": "HAWKSTER",
        "age": 192
      },
      {
        "id": 1,
        "name": "Kristy Herring",
        "company": "ECSTASIA",
        "age": 160
      },
      {
        "id": 2,
        "name": "Gwendolyn Park",
        "company": "TROPOLIS",
        "age": 217
      },
      {
        "id": 3,
        "name": "Ballard Schneider",
        "company": "QUADEEBO",
        "age": 120
      },
      {
        "id": 4,
        "name": "Bonita Mcclure",
        "company": "KONNECT",
        "age": 85
      },
      {
        "id": 5,
        "name": "Melendez Trujillo",
        "company": "MANGELICA",
        "age": 311
      },
      {
        "id": 6,
        "name": "Long Osborn",
        "company": "SCHOOLIO",
        "age": 372
      },
      {
        "id": 7,
        "name": "Lorrie Rowe",
        "company": "ZAGGLES",
        "age": 360
      },
      {
        "id": 8,
        "name": "Levine Warren",
        "company": "OTHERWAY",
        "age": 310
      },
      {
        "id": 9,
        "name": "Christopher Bare",
        "age": 24,
        "company": "It's Complicated."
      },
      {
        "id": 10,
        "name": "Doodle Bob",
        "age": 37,
        "company": "It's different."
      },
      {
        "id": 11,
        "name": "Dingle B00b",
        "age": 38,
        "company": "It's exaggerated."
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
