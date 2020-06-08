
# flask packages
from flask import Response, request, jsonify
from flask_restful import Resource
from flask_jwt_extended import jwt_required

# project resources
from models.standards import Standards


class StandardsApi(Resource):
    """
    Flask-resftul resource for returning db.standards collection.

    :Example:

    >>> from flask import Flask
    >>> from flask_restful import Api
    >>> from app import default_config

    # Create flask app, config, and resftul api, then add PlaylistApi route
    >>> app = Flask(__name__)
    >>> app.config.update(default_config)
    >>> api = Api(app=app)
    >>> api.add_resource(StandardsApi, '/standards/')

    """
    @jwt_required
    def get(self) -> Response:
        """
        GET response method for all documents in standards collection.
        JSON Web Token is required.
        :return: JSON object
        """
        output = Standards.objects()
        return jsonify({'result': output})

    @jwt_required
    def post(self) -> Response:
        """
        POST response method for creating standard.
        JSON Web Token is required.
        Authorization is not required
        To check it Users.objects.get(id=get_jwt_identity()).email for get email
        Import get_jwt_identity from flask_jwt_extended
        :return: JSON object
        """
        data = request.get_json()
        post_standard = Standards(**data).save()
        output = {'id': str(post_standard.id)}
        return jsonify({'result': output})


class StandardApi(Resource):
    """
    Flask-resftul resource for returning db.standards collection.
    :Example:
    >>> from flask import Flask
    >>> from flask_restful import Api
    >>> from app import default_config

    # Create flask app, config, and resftul api, then add StandardApi route
    >>> app = Flask(__name__)
    >>> app.config.update(default_config)
    >>> api = Api(app=app)
    >>> api.add_resource(StandardApi, '/standards/<standard_id>')
    """

    @jwt_required
    def get(self, standard_id: str) -> Response:
        """
        GET response method for single documents in standard collection.
        :return: JSON object
        """

        output = Standards.objects.get(id=standard_id)
        return jsonify({'result': output})

    @jwt_required
    def put(self, standard_id: str) -> Response:
        """
        PUT response method for updating a standard.
        JSON Web Token is required.
        Authorization is required: Access(admin=true)
        :return: JSON object
        """

        data = request.get_json()
        put_standard = Standards.objects(id=standard_id).update(**data)
        return jsonify({'result': put_standard})

    @jwt_required
    def delete(self, standard_id: str) -> Response:
        """
        DELETE response method for deleting single standard.
        JSON Web Token is required.
        :return: JSON object
        """

        output = Standards.objects(id=standard_id).delete()
        return jsonify({'result': output})
