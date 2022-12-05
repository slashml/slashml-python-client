from django.http import JsonResponse
import requests
import os
from pathlib import Path
import json

class SpeechToText:

    SLASHML_BASE_URL = 'https://api.slashml.com/speech-to-text/v1'
    SLASHML_UPLOAD_URL = SLASHML_BASE_URL+'/upload/'
    SLASHML_TRANSCRIPT_URL = SLASHML_BASE_URL+'/transcribe/'
    SLASHML_STATUS_URL = SLASHML_BASE_URL+'/transcription'
    SLASHML_TRANSCRIPT_STATUS_URL = lambda self,id: f"{SpeechToText.SLASHML_STATUS_URL}/{id}/"
 
    HEADERS:dict = {}
    ## add the api key to sys path envs 
    def __init__(self,SLASHML_API_KEY) -> None:
        self.HEADERS = {'authorization': os.environ.get('SLASHML_API_KEY')},
        self.API_KEY=SLASHML_API_KEY

    def upload_audio(self, file_location:str):

        token="Token {0}".format(self.API_KEY)
        headers = {'authorization': token}

        files=[
        ('audio',('test_audio.mp3',open(file_location,'rb'),'audio/mpeg'))
        ]
        response = requests.post(self.SLASHML_UPLOAD_URL,
                                headers=headers,files=files)
        
        return json.loads(response.text)["upload_url"]

    def transcribe(self,upload_url:str,  service_provider: str ):

        transcript_request = {'audio_url': upload_url}
        token="Token {0}".format(self.API_KEY)
        headers = {'authorization': token}
        payload = {
        "uploaded_audio_url": upload_url,
        "service_provider": service_provider
        }
        response = requests.post(self.SLASHML_TRANSCRIPT_URL, headers=headers, data=payload)
        return json.loads(response.text)["id"]

    def status(self,job_id:str, service_provider: str ):
        token="Token {0}".format(self.API_KEY)
        headers = {'authorization': token}
        payload = {
        "service_provider": service_provider
        }
       
        response = requests.get(self.SLASHML_TRANSCRIPT_STATUS_URL(job_id) , headers=headers, data=payload)
        return json.loads(response.text)

