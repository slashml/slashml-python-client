import requests
from enum import Enum
from .utils.common import generateURL, baseUrl, generateHeaders, formatResponse, getTaskStatus

class TextSummarization:
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

    def summarize(self, text: str, service_provider: ServiceProvider):
        url = generateURL(self._base_url, "jobs")
        payload = {"text": [text], "service_provider": service_provider.value}
        response = requests.post(url, headers=self._headers, data=payload)
        return formatResponse(response)

    def status(self, job_id: str, service_provider: ServiceProvider):
        return getTaskStatus(self._base_url, self._headers, job_id, service_provider)
        