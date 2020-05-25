
# mongo-engine packages
from mongoengine import Document, StringField, IntField


class Songs(Document):
    """
    Template for a mongoengine document, which represents a user's favorite meal.
    :param artist: required string value, fewer than 50 characters
    :param title: required string value, fewer than 100 characters
    :param difficulty: optional int value, from 1 to 5

    :Example:
    >>> import mongoengine
    >>> from app import default_config
    >>> mongoengine.connect(**default_config['MONGODB_SETTINGS'])
    MongoClient(host=['localhost:27017'], document_class=dict, tz_aware=False, connect=True, read_preference=Primary())
    >>> new_song = Songs(artist= "Guthrie Govan", \
                        title= "Remember when", \
                        difficulty= 5)
    >>> new_song.save()
    <Song: Song object>
    """

    artist = StringField(required=True, max_length=50)
    description = StringField(required=True, max_length=240)
    difficulty = IntField(min_value=1, max_value=5)
