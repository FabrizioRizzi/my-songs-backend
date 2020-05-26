
# mongo-engine packages
from mongoengine import Document, StringField


class Playlists(Document):
    """
    Template for a mongoengine document
    :param artist: required string value, fewer than 50 characters
    :param album: required string value, fewer than 100 characters
    :param genre: string value, fewer than 50 characters

    :Example:
    >>> import mongoengine
    >>> from app import default_config
    >>> mongoengine.connect(**default_config['MONGODB_SETTINGS'])
    MongoClient(host=['localhost:27017'], document_class=dict, tz_aware=False, connect=True, read_preference=Primary())
    >>> new_playlist = Playlists(artist="Marillion", title="Jester's tears", genre="Prog")
    >>> new_playlist.save()
    <Playlists: Playlists object>
    """

    artist = StringField(required=True, max_length=50)
    title = StringField(required=True, max_length=100)
    genre = StringField(max_length=50)
