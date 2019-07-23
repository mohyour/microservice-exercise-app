from flask import Flask
from flask_restful import Resource, Api
from project import config


app = Flask(__name__)
api = Api(app)

app.config.from_object(config.DevConfig)


class UsersPing(Resource):
    def get(self):
        return {
            'status': 'success',
            'message': 'Ping! Welcome user!'
        }

api.add_resource(UsersPing, '/users/ping')
