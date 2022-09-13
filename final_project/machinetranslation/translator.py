"""Beginning of translator"""
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv


load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
authenticator = IAMAuthenticator('YsJPMjucI3du1vbQo45_K1g7ozhKDlOI32Z30MkS_9dB')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
language_translator.set_service_url('https://api.us-east.language-translator.watson.cloud.ibm.com/instances/31381b10-2818-44ae-a3bf-5a88d6f0c21b')
def english_to_french(english_text):
    """English to french function"""
    translation=language_translator.translate(text=english_text, model_id="en-fr").get_result()
    french_text=translation['translations'][0]['translation']
    return french_text
def french_to_english(french_text):
    """French to english function"""
    translation=language_translator.translate(text=french_text,model_id="fr-en").get_result()
    english_text=translation['translations'][0]['translation']
    return english_text
