# flask packages
from flask import jsonify
from flask_restful import Resource

# mongo-engine models
from models.songs import Songs


class SongsApi(Resource):
    def get(self):
        output = Songs.objects()
        return jsonify({'result': output})
