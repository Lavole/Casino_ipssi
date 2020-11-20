from flask import Flask, request
from flask_restx import Resource, Api
from flask_cors import CORS

import bdd_service

app = Flask(__name__)
CORS(app)
api = Api(app)


@api.route('/connexion')
class HelloWorld(Resource):
    def get(self):
        pseudo = request.args.get('pseudo')
        joueur = bdd_service.get_or_create_player(pseudo, 10)
        return joueur


@api.route('/niveau1')
class HelloWorld(Resource):
    def get(self):
        id_joueur = request.args.get('id_joueur')
        joueur = bdd_service.get_max_niveau(id_joueur)
        return joueur


if __name__ == '__main__':
    app.run(debug=True)
