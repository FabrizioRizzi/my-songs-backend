from api.song import SongsApi
from api.playlist import PlaylistsApi


def create_routes(api):
    api.add_resource(SongsApi, '/songs/')

    api.add_resource(PlaylistsApi, '/playlists/')
