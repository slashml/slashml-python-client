from django.http import JsonResponse
import requests
import os
from pathlib import Path

class SpeechToText:
    # TODO: make sure this is dynamic
    SLASHML_BASE_URL = 'https://api.slashml.com/speech-to-text/v1'
    SLASHML_UPLOAD_URL = SLASHML_BASE_URL+'/upload/'
    SLASHML_TRANSCRIPT_URL = SLASHML_BASE_URL+'/transcribe/'
    SLASHML_STATUS_URL = SLASHML_BASE_URL+'/transcription'
    SLASHML_TRANSCRIPT_STATUS_URL = lambda self,id: f"{SpeechToText.SLASHML_STATUS_URL}/{id}/"
 
    HEADERS:dict = {}
    ## add the api key to sys path envs 
    def __init__(self) -> None:
        self.HEADERS = {'authorization': os.environ.get('SLASHML_API_KEY')}

    def upload_audio(self, file_location:str, API_KEY: str, model_choice: str ):
        # here we can also add the service? assemblyai, aws, gcp?

        token="Token {0}".format(API_KEY)
        headers = {'authorization': token}
        payload = { 'model':model_choice }
        files=[
        ('audio',('test_audio.mp3',open(file_location,'rb'),'audio/mpeg'))
        ]
        #import pdb
        #pdb.set_trace()
        response = requests.post(self.SLASHML_UPLOAD_URL,
                                headers=headers,
                                data=payload,files=files)
        return response.text

    def transcribe(self,upload_url:str, API_KEY: str, model_choice: str ):
        # here we can add more model params
        transcript_request = {'audio_url': upload_url}
        token="Token {0}".format(API_KEY)
        headers = {'authorization': token}
        payload = {
        "uploaded_audio_url": upload_url,
        "model": model_choice
        }

        response = requests.post(self.SLASHML_TRANSCRIPT_URL, headers=headers, data=payload)
        return response.text

    def status(self,job_id:str, API_KEY: str, model_choice: str ):
        token="Token {0}".format(API_KEY)
        headers = {'authorization': token}
        payload = {
        "model": model_choice
        }
    #import pdb
       # pdb.set_trace()        
        response = requests.get(self.SLASHML_TRANSCRIPT_STATUS_URL(job_id) , headers=headers, data=payload)
        return response.text

