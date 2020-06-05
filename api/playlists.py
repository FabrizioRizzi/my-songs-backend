
# flask packages
from flask import Response, request, jsonify
from flask_restful import Resource
from flask_jwt_extended import jwt_required

# project resources
from models.playlists import Playlists


class PlaylistsApi(Resource):
    """
    Flask-resftul resource for returning db.playlists collection.

    :Example:

    >>> from flask import Flask
    >>> from flask_restful import Api
    >>> from app import default_config

    # Create flask app, config, and resftul api, then add PlaylistsApi route
    >>> app = Flask(__name__)
    >>> app.config.update(default_config)
    >>> api = Api(app=app)
    >>> api.add_resource(PlaylistsApi, '/playlists/')

    """
    @jwt_required
    def get(self) -> Response:
        """
        GET response method for all documents in playlist collection.
        JSON Web Token is required.
        :return: JSON object
        """
        output = Playlists.objects()
        return jsonify({'result': output})

    @jwt_required
    def post(self) -> Response:
        """
        POST response method for creating playlist.
        JSON Web Token is required.
        Authorization is not required
        To check it Users.objects.get(id=get_jwt_identity()).email for get email
        Import get_jwt_identity from flask_jwt_extended
        :return: JSON object
        """
        data = request.get_json()
        try:
            post_playlist = Playlists(**data).save()
        except Exception as e:
            return jsonify("%s" % e)
        output = {'id': str(post_playlist.id)}
        return jsonify({'result': output})


class PlaylistApi(Resource):
    """
    Flask-resftul resource for returning db.playlists collection.
    :Example:
    >>> from flask import Flask
    >>> from flask_restful import Api
    >>> from app import default_config
    # Create flask app, config, and resftul api, then add PlaylistApi route
    >>> app = Flask(__name__)
    >>> app.config.update(default_config)
    >>> api = Api(app=app)
    >>> api.add_resource(PlaylistApi, '/playlists/<playlist_id>')
    """

    @jwt_required
    def get(self, playlist_id: str) -> Response:
        """
        GET response method for single documents in playlists collection.
        :return: JSON object
        """

        output = Playlists.objects.get(id=playlist_id)
        return jsonify({'result': output})

    @jwt_required
    def put(self, playlist_id: str) -> Response:
        """
        PUT response method for updating a playlist.
        JSON Web Token is required.
        Authorization is required: Access(admin=true)
        :return: JSON object
        """

        data = request.get_json()
        put_playlist = Playlists.objects(id=playlist_id).update(**data)
        return jsonify({'result': put_playlist})

    @jwt_required
    def delete(self, playlist_id: str) -> Response:
        """
        DELETE response method for deleting single playlist.
        JSON Web Token is required.
        :return: JSON object
        """

        output = Playlists.objects(id=playlist_id).delete()
        return jsonify({'result': output})
