
# mongo-engine packages
from mongoengine import Document, StringField, IntField


class Standards(Document):
    """
    Template for a mongoengine document
    :param title: required string value, fewer than 100 characters
    :param difficulty: optional int value, from 1 to 5
    :param aebersold: optional string, fewer than 200 characters
    :param notes: optional string, fewer than 300 characters

    :Example:
    >>> import mongoengine
    >>> from app import default_config
    >>> mongoengine.connect(**default_config['MONGODB_SETTINGS'])
    MongoClient(host=['localhost:27017'], document_class=dict, tz_aware=False, connect=True, read_preference=Primary())
    >>> new_standard = Standards(title="Autumn Leaves", difficulty=1, aebersold="54", notes="Non saprei")
    >>> new_standard.save()
    <Standards: Standards object>
    """

    title = StringField(required=True, max_length=100)
    difficulty = IntField(min_value=0, max_value=5)
    aebersold = StringField(max_length=200)
    notes = StringField(max_length=300)
