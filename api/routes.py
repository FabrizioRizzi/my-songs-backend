from api.song import SongsApi


def create_routes(api):
    api.add_resource(SongsApi, '/song/')
