from flask import Flask
from flask_restx import Api
from flask_cors import CORS

from configuration.app_config import *
from app_startup import *

from WebAPI import *

api = Api(version='1.0', title='BCR Braille Transcriptor', description='BCR Braille Transcriptor API', prefix='/')
api.add_namespace(ns_about)
api.add_namespace(ns_transcribe)

app = Flask(__name__)
api.init_app(app)
CORS(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001, debug=True, use_reloader=False)

