import os
import sys
import logging

from Alpha import AlphaToBrailleTranscriptor 
from Alpha import BrailleToAlphaTranscriptor 
from Alpha.languages import Spanish

from opencensus.ext.azure.log_exporter import AzureLogHandler

from flask import request, make_response, jsonify
from flask_restx import Namespace, Resource

logger = logging.getLogger(__name__)
logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler(sys.stdout))
logger.setLevel('INFO')

if (os.environ['INSIGHTS_CNN_STRING']):
    logger.addHandler(AzureLogHandler(connection_string=os.environ['INSIGHTS_CNN_STRING']))   

api = Namespace('Transcribe', 'Transcribe alpha <>braille', path='/transcribe')

def get_language(language):
    if language == 'ES':
        return Spanish()



@api.route('/brailletoalpha')
class braille_alpha(Resource):
    def post(self):
        try:
            text = request.json['text']
            words = request.json['words']
            language = request.json['language']

            result, appliedRules, wordResults = self.__transcribe_from_braille_to_alpha__(text, words, language)

            result = {
                'text': result,
                'appliedRules': appliedRules,
                'words': wordResults
            }

            return result
         
        except Exception as ex:
            logger.exception('Captured exception.', extra={'exception': str(ex)})
            return { 'error': str(ex) }, 400

    def __transcribe_from_braille_to_alpha__(self, string, words, lang):
        
        language = get_language(lang)
        self.transcriptor = BrailleToAlphaTranscriptor(language)
        result, appliedRules = self.transcriptor.transcribe(string)

        wordResults = []
        for word in words:
            wordresult, appliedRules = self.transcriptor.transcribe(word)
            wordResults.append(wordresult)

        return result, appliedRules, wordResults

@api.route('/alphatobraille')
class alpha_braille(Resource):
    def post(self, string, language):
        try:
            return self.__transcribe_from_alpha_to_braille__(string, language)
         
        except Exception as ex:
            logger.exception('Captured exception.', extra={'exception': str(ex)})
            return { 'error': str(ex) }, 400

    def __transcribe_from_alpha_to_braille__(self, string, lang):
        
        language = get_language(lang)
        self.transcriptor = AlphaToBrailleTranscriptor(language)
        result, appliedRules = self.transcriptor.transcribe(string)
        return result, appliedRules

@api.route('/results')
class results(Resource):
    def get(self):
        return "v0.0.1"

