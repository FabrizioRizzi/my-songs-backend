# flask packages
from flask import jsonify
from flask_restful import Resource

# mongo-engine models
from models.playlists import Playlists


class PlaylistsApi(Resource):
    @staticmethod
    def get():
        output = Playlists.objects()
        return jsonify({'result': output})
