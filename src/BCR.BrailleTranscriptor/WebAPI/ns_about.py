from flask_restx import Namespace, Resource

api = Namespace('About', 'About BCR Transcriptor', path='about')

@api.route('/version')
class version(Resource):
    def get(self):
        return "v0.0.1"

