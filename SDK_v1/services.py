from django.http import JsonResponse
import requests
import os
from pathlib import Path

def upload_audio(*, audio_data, service_name) -> None:
    # with open('test.mp3', 'wb+') as mp3:
    #     for chunk in audio_data.chunks():
    #         mp3.write(chunk)

    if service_name == 'assembly':
        Assembly().upload_audio(audio_file=audio_data)



class Assembly:
    ASSEMBLY_BASE_URL = 'https://api.assemblyai.com/v2'
    ASSEMBLY_UPLOAD_URL = ASSEMBLY_BASE_URL+'/upload'
    ASSEMBLY_TRANSCRIPT_URL = ASSEMBLY_BASE_URL+'/transcript'
    ASSEMBLY_TRANSCRIPT_STATUS_URL = lambda id: f"{Assembly.ASSEMBLY_BASE_URL}+/transcript/{id}"

    HEADERS:dict = {}

    def __init__(self) -> None:
        self.HEADERS = {'authorization': os.environ.get('ASSEMBLY_API_KEY')}

    def _read_file(filename, chunk_size=5242880):
        with open(filename, 'rb') as _file:
            while True:
                data = _file.read(chunk_size)
                if not data:
                    break
                yield data

    def upload_audio(self, *, audio_file:Path, headers:dict=None) -> JsonResponse:
        import pdb
        pdb.set_trace()
        response = requests.post(self.ASSEMBLY_UPLOAD_URL,
                                headers=headers if headers else self.HEADERS,
                                data=self._read_file(audio_file))
        return response.json()

    def request_transcript(self, *, upload_url:dict, headers:dict=None):

        transcript_request = {
            'audio_url': upload_url['upload_url']
        }

        transcript_response = requests.post(
            self.ASSEMBLY_TRANSCRIPT_URL,
            json=transcript_request,
            headers=headers if headers else self.HEADERS,
        )

        return transcript_response.json()

    def transcription_status(self, *, transcript_id:str, upload_url:dict, headers:dict=None):

        transcript_request = {
            'audio_url': upload_url['upload_url']
        }

        transcript_response = requests.post(
            self.ASSEMBLY_TRANSCRIPT_STATUS_URL(transcript_id),
            json=transcript_request,
            headers=headers if headers else self.HEADERS,
        )

        return transcript_response.json()