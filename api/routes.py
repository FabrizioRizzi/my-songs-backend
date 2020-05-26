
# flask packages
from flask_restful import Api

# project resources
from api.authentication import SignUpApi, LoginApi
from api.songs import SongsApi, SongApi
from api.playlists import PlaylistsApi, PlaylistApi


def create_routes(api: Api):
    """Adds resources to the api.
    :param api: Flask-RESTful Api Object
    :Example:
        api.add_resource(HelloWorld, '/', '/hello')
        api.add_resource(Foo, '/foo', endpoint="foo")
        api.add_resource(FooSpecial, '/special/foo', endpoint="foo")
    """
    api.add_resource(SignUpApi, '/authentication/signup/')
    api.add_resource(LoginApi, '/authentication/login/')

    api.add_resource(SongsApi, '/songs/')
    api.add_resource(SongApi, '/songs/<song_id>')

    api.add_resource(PlaylistsApi, '/playlists/')
    api.add_resource(PlaylistApi, '/playlists/<playlist_id>')
