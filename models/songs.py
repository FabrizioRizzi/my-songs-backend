
# mongo-engine packages
from mongoengine import Document, StringField, IntField, BooleanField


class Songs(Document):
    """
    Template for a mongoengine document
    :param artist: required string value, fewer than 50 characters
    :param title: required string value, fewer than 100 characters
    :param difficulty: optional int value, from 1 to 5
    :param acoustic: boolean
    :param dfm: don't forget me! boolean
    :param backing: backing track boolean
    :param tab: tablature boolean
    :param notes: optional string, fewer than 300 characters

    :Example:
    >>> import mongoengine
    >>> from app import default_config
    >>> mongoengine.connect(**default_config['MONGODB_SETTINGS'])
    MongoClient(host=['localhost:27017'], document_class=dict, tz_aware=False, connect=True, read_preference=Primary())
    >>> new_song = Songs(artist="Guthrie Govan",title="Remember when", difficulty=5, acoustic=false, dfm=true, backing=true, tab=true, notes="Non saprei")
    >>> new_song.save()
    <Songs: Songs object>
    """

    artist = StringField(required=True, max_length=50)
    title = StringField(required=True, max_length=100)
    difficulty = IntField(min_value=0, max_value=5)
    acoustic = BooleanField()
    dfm = BooleanField()
    backing = BooleanField()
    tab = BooleanField()
    notes = StringField(max_length=300)
