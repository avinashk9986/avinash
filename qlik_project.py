from flask import Flask
from flask_restful import Api, Resource, reqparse
app = Flask(__name__)
api = Api(app)
message_list = [
    {
        "message": "avinash"
    },
    {
        "message": "alok"
    },
    {
        "message": "vivek"
    }
]
class List(Resource):
    def get(self):
        return message_list, 200

class MSG(Resource):
    def get(self, message):
        for x in message_list:
            if(message == x["message"]):
                            if(message==message[::-1]):
                                a=" string is a palindrome"
                            else:
                                a=" string isn't a palindrome"
                            return "{} {} ".format(x,a), 200
        return "User not found", 404

    def post(self, message):
        parser = reqparse.RequestParser()

        for x in message_list:
            if(message == x["message"]):
                return "User with message {} already exists".format(message), 400

        x = {
            "message": message
        }
        message_list.append(x)
        return x, 201

    def delete(self, message):
        global message_list
        message_list = [x for x in message_list if x["message"] != message]
        return "{} is deleted.".format(message), 200

api.add_resource(MSG, "/message/<string:message>")
api.add_resource(List, "/list")
if __name__ == '__main__':
    app.debug=True
    app.run(host = '0.0.0.0',port=5005)
