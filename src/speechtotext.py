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
    def __init__(self,API_KEY: str = None):
        self.API_KEY=None
        if API_KEY:
            token="Token {0}".format(API_KEY)
            self.HEADERS = {'authorization': token}
           # print("Auth with "+API_KEY+"\nMake sure this matches your API Key generated in the dashboard settings")
        elif os.environ.get('SLASHML_API_KEY'):
            key_env =  os.environ.get('SLASHML_API_KEY')
            token="Token {0}".format(key_env)
            self.HEADERS = {'authorization': token}
           # print("Auth with environment variable SLASHML_API_KEY")
        else:
            self.HEADERS=None 
            print("No Auth, there are certain limites to the usage")

    def upload_audio(self, file_location:str,header=None):
        headers = self.HEADERS
        files=[
        ('audio',('test_audio.mp3',open(file_location,'rb'),'audio/mpeg'))
        ]
        response = requests.post(self.SLASHML_UPLOAD_URL,
                                headers=headers,files=files)
        return  response.json()["upload_url"]

    def transcribe(self,upload_url:str,  service_provider: str,header=None ):

        transcript_request = {'audio_url': upload_url}
        headers = self.HEADERS
        payload = {
        "uploaded_audio_url": upload_url,
        "service_provider": service_provider
        }
        response = requests.post(self.SLASHML_TRANSCRIPT_URL, headers=headers, data=payload)
        # Check the status code of the response
        if response.status_code == 200:
            return response.json()["id"]
        
        elif response.status_code == 429:
            return "THROTTLED"
        
        elif response.status_code == 404:
            return "NOT FOUND"
        
        elif response.status_code == 500:
            return "SERVER ERROR"
        else:
            return "UNKNOWN ERROR"
        
    def status(self,job_id:str, service_provider: str ,header=None):
        headers = self.HEADERS
        payload = {
        "service_provider": service_provider
        }
       
        response = requests.get(self.SLASHML_TRANSCRIPT_STATUS_URL(job_id) , headers=headers, data=payload)

        # Check the status code of the response
        if response.status_code == 200:
            return response.json()["transcription_data"]["transcription"]
        
        elif response.status_code == 429:
            return "THROTTLED"
        
        elif response.status_code == 404:
            return "NOT FOUND"
        
        elif response.status_code == 500:
            return "SERVER ERROR"
        else:
            return "UNKNOWN ERROR"