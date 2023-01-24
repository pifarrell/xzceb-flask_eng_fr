"""
Simple EN-FR and FR-EN translator methods
"""
import os
from ibm_watson import LanguageTranslatorV3, ApiException
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

auth =IAMAuthenticator(apikey)
translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=auth
)

translator.set_service_url(url)

def english_to_french(english_text):
    """ Translate given english text to french
    """
    if english_text is not None and len(english_text) > 0:
        try:
            translations = translator.translate(
                text=english_text,
                model_id='en-fr').get_result()
            return translations['translations'][0]['translation']
        except ApiException as ex:
            print(f'Couldn\'t translate text: {english_text}\n\t{ex.message}')

    return english_text


def french_to_english(french_text):
    """ Translate given french text to english
    """

    if french_text is not None and len(french_text) > 0:
        try:
            translations = translator.translate(
                text=french_text,
                model_id='fr-en').get_result()
            return translations['translations'][0]['translation']
        except ApiException as ex:
            print(f'Couldn\'t translate text: {french_text}\n\t{ex.message}')

    return french_text
