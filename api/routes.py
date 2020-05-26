
# flask packages
from flask_restful import Api

# project resources
from api.authentication import SignUpApi, LoginApi
from api.songs import SongsApi, SongApi
from api.playlists import PlaylistsApi, PlaylistApi

from flask import Response, request, jsonify
from flask_restful import Resource


class InitApi(Resource):
    def post(self) -> Response:
        """
        GET response method for all documents in song collection.
        JSON Web Token is required.
        :return: JSON object
        """
        print('e', request)
        print('eccolo', request.data)
        print('eccolo2', request.args)
        print('eccolo3', request.form.get('data'))
        print('eccolo4', request.json)
        return 'ok'

    def get(self) -> Response:
        """
        GET response method for all documents in song collection.
        JSON Web Token is required.
        :return: JSON object
        """
        print('eccolo get')
        return 'ok'


def create_routes(api: Api):
    """Adds resources to the api.
    :param api: Flask-RESTful Api Object
    :Example:
        api.add_resource(HelloWorld, '/', '/hello')
        api.add_resource(Foo, '/foo', endpoint="foo")
        api.add_resource(FooSpecial, '/special/foo', endpoint="foo")
    """

    api.add_resource(InitApi, '/')
    api.add_resource(SignUpApi, '/authentication/signup/')
    api.add_resource(LoginApi, '/authentication/login/')

    api.add_resource(SongsApi, '/songs/')
    api.add_resource(SongApi, '/songs/<song_id>')

    api.add_resource(PlaylistsApi, '/playlists/')
    api.add_resource(PlaylistApi, '/playlists/<playlist_id>')
