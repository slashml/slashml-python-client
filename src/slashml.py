import requests
import os
from pathlib import Path
import json

from json_to_dot import edict

class SpeechToText:

    SLASHML_BASE_URL = 'https://api.slashml.com/speech-to-text/v1'
    SLASHML_UPLOAD_URL = SLASHML_BASE_URL+'/upload/'
    SLASHML_TRANSCRIPT_URL = SLASHML_BASE_URL+'/transcribe/'
    SLASHML_STATUS_URL = SLASHML_BASE_URL+'/transcription'
    SLASHML_TRANSCRIPT_STATUS_URL = lambda self,id: f"{SpeechToText.SLASHML_STATUS_URL}/{id}/"

    HEADERS:dict = {}
    ## add the api key to sys path envs 
    def __init__(self,API_KEY: str = None):
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
            print("No API key provided, there are limits to the usage.")

    def upload_audio(self, file_location:str, header=None):
        headers = self.HEADERS

        files=[
            ('audio',('test_audio.mp3',open(file_location,'rb'),'audio/mpeg'))
        ]

        response = requests.post(self.SLASHML_UPLOAD_URL,
                                headers=headers,files=files)
        
        return edict(response.json())

        
    def transcribe(self, upload_url:str, service_provider: str, header = None ):
        headers = self.HEADERS

        payload = {
            "uploaded_audio_url": upload_url,
            "service_provider": service_provider
        }

        response = requests.post(self.SLASHML_TRANSCRIPT_URL, headers=headers, data=payload)

        # Check the status code of the response
        return edict(response.json())
        
    def status(self,job_id:str, service_provider: str ,header=None):
        headers = self.HEADERS
        payload = {
        "service_provider": service_provider
        }
       
        response = requests.get(self.SLASHML_TRANSCRIPT_STATUS_URL(job_id) , headers=headers, data=payload)

        return edict(response.json())

class Summarization:
    SLASHML_SUMMARIZATION_URL = 'https://api.slashml.com/summarization/v1'
    SLASHML_SUMMARIZE_URL = SLASHML_SUMMARIZATION_URL+'/summarize/'
    SLASHML_SUMMARIZE_STATUS_URL = lambda self,id: f"{Summarization.SLASHML_SUMMARIZATION_URL}/jobs/{id}/"

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

    def summarize(self,text:str,service_provider: str,header=None):
        headers = self.HEADERS
        payload = {
        "text": [text],
        "service_provider": service_provider
        }
        response = requests.post(self.SLASHML_SUMMARIZE_URL, headers=headers, data=payload)
        # Check the status code of the response
        if response.status_code == 200:
            return response.json()["id"]
        else:
            return "ERROR"+ str(response.json())
        
    def status(self,job_id:str, service_provider: str ,header=None):
        headers = self.HEADERS
        payload = {"service_provider": service_provider}
        response = requests.get(self.SLASHML_SUMMARIZE_STATUS_URL(job_id) , headers=headers, data=payload)
        # Check the status code of the response
        if response.status_code == 200:
            if response.json()["status"]=="IN_PROGRESS":
                return "Summarization is still in progress"
            elif response.json()["status"]=="COMPLETED":
                return response.json()['summarization_data']

        else:
            return "ERROR"+ str(response.json())