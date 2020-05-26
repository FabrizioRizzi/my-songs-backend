
# flask packages
from flask import Response, request, jsonify
from flask_restful import Resource
from flask_jwt_extended import jwt_required

# project resources
from models.songs import Songs


class SongsApi(Resource):
    """
    Flask-resftul resource for returning db.songs collection.

    :Example:

    >>> from flask import Flask
    >>> from flask_restful import Api
    >>> from app import default_config

    # Create flask app, config, and resftul api, then add SongsApi route
    >>> app = Flask(__name__)
    >>> app.config.update(default_config)
    >>> api = Api(app=app)
    >>> api.add_resource(SongsApi, '/songs/')

    """
    @jwt_required
    def get(self) -> Response:
        """
        GET response method for all documents in song collection.
        JSON Web Token is required.
        :return: JSON object
        """
        print('ok')
        output = Songs.objects()
        return jsonify({'result': output})

    @jwt_required
    def post(self) -> Response:
        """
        POST response method for creating song.
        JSON Web Token is required.
        Authorization is not required
        To check it Users.objects.get(id=get_jwt_identity()).email for get email
        Import get_jwt_identity from flask_jwt_extended
        :return: JSON object
        """
        data = request.get_json()
        post_song = Songs(**data).save()
        output = {'id': str(post_song.id)}
        return jsonify({'result': output})


class SongApi(Resource):
    """
    Flask-resftul resource for returning db.songs collection.
    :Example:
    >>> from flask import Flask
    >>> from flask_restful import Api
    >>> from app import default_config
    # Create flask app, config, and resftul api, then add SongApi route
    >>> app = Flask(__name__)
    >>> app.config.update(default_config)
    >>> api = Api(app=app)
    >>> api.add_resource(SongApi, '/songs/<song_id>')
    """

    @jwt_required
    def get(self, song_id: str) -> Response:
        """
        GET response method for single documents in songs collection.
        :return: JSON object
        """

        output = Songs.objects.get(id=song_id)
        return jsonify({'result': output})

    @jwt_required
    def put(self, song_id: str) -> Response:
        """
        PUT response method for updating a song.
        JSON Web Token is required.
        Authorization is required: Access(admin=true)
        :return: JSON object
        """

        data = request.get_json()
        put_song = Songs.objects(id=song_id).update(**data)
        return jsonify({'result': put_song})

    @jwt_required
    def delete(self, song_id: str) -> Response:
        """
        DELETE response method for deleting single song.
        JSON Web Token is required.
        :return: JSON object
        """

        output = Songs.objects(id=song_id).delete()
        return jsonify({'result': output})
