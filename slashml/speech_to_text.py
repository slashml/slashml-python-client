import requests
import time
from enum import Enum
from .utils import generateURL, baseUrl, generateHeaders, formatResponse, getTaskStatus


class SpeechToText:
    """Speech to Text Service """
    class ServiceProvider(Enum):
        ASSEMBLY = "assembly"
        AWS = "aws"
        WHISPER = "whisper"
        DEEPGRAM = 'deepgram'
        GOOGLE = 'google'
        REV = 'rev'

        @classmethod
        def choices(cls):
            return [key.value for key in cls]

    _base_url = baseUrl("speech-to-text", "v1")
    _headers = None

    def __init__(self, api_key: str = None):
        self._headers = generateHeaders(api_key)

    def upload_audio(self, file_location: str):
        """Upload audio to server"""
        url = generateURL(self._base_url, "upload")
        files = [("audio", ("test_audio.mp3", open(file_location, "rb"), "audio/mpeg"))]
        response = requests.post(url, headers=self._headers, files=files)
        return formatResponse(response)

    def submit_job(self, upload_url: str, service_provider: ServiceProvider):
        """Submit job"""
        url = generateURL(self._base_url, "jobs")
        payload = {
            "uploaded_audio_url": upload_url,
            "service_provider": service_provider.value,
        }
        response = requests.post(url, headers=self._headers, data=payload)
        return formatResponse(response)

    def status(self, job_id: str, service_provider: ServiceProvider):
        """Check job status"""
        return getTaskStatus(self._base_url, self._headers, job_id, service_provider)

    def execute(self, upload_url: str, service_provider: ServiceProvider):
        """Waits for the job to be completed before returning a response"""
        url = generateURL(self._base_url, "jobs")

        payload = {
            "uploaded_audio_url": upload_url,
            "service_provider": service_provider.value,
        }

        response = requests.post(url, headers=self._headers, data=payload)
        job = formatResponse(response)

        assert job.status != "ERROR", f"{job}"
        print(f"Got Job ID: {job.id}")
        
        # check job status
        response = getTaskStatus(self._base_url, self._headers, job.id, service_provider)

        # while response.status == "IN_PROGRESS":
        while response.status == "IN_PROGRESS":
            time.sleep(5)
            response = getTaskStatus(self._base_url, self._headers, job.id, service_provider)
            print(f"Response = {response}. Retrying in 5 seconds")

        return response
    
