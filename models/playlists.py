
# mongo-engine packages
from mongoengine import Document, StringField, IntField


class Playlists(Document):
    """
    Template for a mongoengine document
    :param artist: required string value, fewer than 50 characters
    :param album: required string value, fewer than 100 characters
    :param genre: string value, fewer than 50 characters
    :param rating: number value, from 1 to 5

    :Example:
    >>> import mongoengine
    >>> from app import default_config
    >>> mongoengine.connect(**default_config['MONGODB_SETTINGS'])
    MongoClient(host=['localhost:27017'], document_class=dict, tz_aware=False, connect=True, read_preference=Primary())
    >>> new_playlist = Playlists(artist="Marillion", album="Jester's tears", genre="Prog", rating="5" )
    >>> new_playlist.save()
    <Playlists: Playlists object>
    """

    artist = StringField(required=True, max_length=50)
    album = StringField(required=True, max_length=100)
    genre = StringField(max_length=50)
    rating = IntField(min_value=1, max_value=5)
