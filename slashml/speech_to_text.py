import requests
from enum import Enum
from .utils.common import generateURL, baseUrl, generateHeaders, formatResponse, getTaskStatus


class SpeechToText:
    class ServiceProvider(Enum):
        ASSEMBLY = "assembly"
        AWS = "aws"
        WHISPER = "whisper"

        @classmethod
        def choices(cls):
            return [key.value for key in cls]

    _base_url = baseUrl("speech-to-text", "v1")
    _headers = None

    def __init__(self, api_key: str = None):
        self._headers = generateHeaders(api_key)

    def upload_audio(self, file_location: str):
        url = generateURL(self._base_url, "upload")
        files = [("audio", ("test_audio.mp3", open(file_location, "rb"), "audio/mpeg"))]
        response = requests.post(url, headers=self._headers, files=files)
        return formatResponse(response)

    def transcribe(self, upload_url: str, service_provider: ServiceProvider):
        url = generateURL(self._base_url, "jobs")
        payload = {
            "uploaded_audio_url": upload_url,
            "service_provider": service_provider.value,
        }
        response = requests.post(url, headers=self._headers, data=payload)
        return formatResponse(response)

    def status(self, job_id: str, service_provider: ServiceProvider):
        return getTaskStatus(self._base_url, self._headers, job_id, service_provider)
