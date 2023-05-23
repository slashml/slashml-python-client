import requests
import time
from enum import Enum
from .utils import generateURL, baseUrl, generateHeaders, formatResponse, getTaskStatus

class TextSummarization:
    """Text Summarization Service """
    class ServiceProvider(Enum):
        OPENAI = "openai"
        HUGGING_FACE = "hugging-face"

        @classmethod
        def choices(cls):
            return [key.value for key in cls]

    _base_url = baseUrl("summarization", "v1")
    _headers = None

    def __init__(self, api_key: str = None):
        self._headers = generateHeaders(api_key)

    def submit_job(self, text: str, service_provider: ServiceProvider):
        """Submit Job to server"""
        url = generateURL(self._base_url, "jobs")
        payload = {"text": [text], "service_provider": service_provider.value}
        response = requests.post(url, headers=self._headers, data=payload)
        return formatResponse(response)

    def status(self, job_id: str, service_provider: ServiceProvider):
        """Check job status"""
        return getTaskStatus(self._base_url, self._headers, job_id, service_provider)

    def execute(self, text: str, service_provider: ServiceProvider):
        """Waits for the job to be completed before returning a response"""
        url = generateURL(self._base_url, "jobs")
        payload = {"text": [text], "service_provider": service_provider.value}
        response = requests.post(url, headers=self._headers, data=payload)
        job = formatResponse(response)

        assert job.status != "ERROR", f"{job}"
        print(f"Got Job ID: {job.id}")

        # check job status
        response = getTaskStatus(self._base_url, self._headers, job.id, service_provider)

        while response.status == "IN_PROGRESS":
            time.sleep(5)
            response = getTaskStatus(self._base_url, self._headers, job.id, service_provider)
            print(f"Response = {response}. Retrying in 5 seconds")
        
        return response

