from enum import Enum
import os
import requests

from .json_to_dot import edict


class TextToSpeech:
    class ServiceProvider(Enum):
        GOOGLE = "google"
        AWS = "aws"

        @classmethod
        def choices(cls):
            return [key.name for key in cls]

    SLASHML_SPEECH_TO_TEXT_URL = "https://api.slashml.com/text-to-speech/v1"
    # SLASHML_SUMMARIZATION_URL = "http://127.0.0.1:8000/summarization/v1"
    SLASHML_SPEECHIFY_URL = SLASHML_SPEECH_TO_TEXT_URL + "/jobs"
    SLASHML_SPEECHIFICATION_STATUS_URL = (
        lambda self, id: f"{TextToSpeech.SLASHML_SPEECH_TO_TEXT_URL}/jobs/{id}/"
    )

    HEADERS: dict = {}

    ## add the api key to sys path envs
    def __init__(self, API_KEY: str = None):
        self.API_KEY = None
        if API_KEY:
            token = "Token {0}".format(API_KEY)
            self.HEADERS = {"authorization": token}

        elif os.environ.get("SLASHML_API_KEY"):
            key_env = os.environ.get("SLASHML_API_KEY")
            token = "Token {0}".format(key_env)
            self.HEADERS = {"authorization": token}

        else:
            self.HEADERS = None
            print("No Auth, there are certain limites to the usage")

    def speechify(self, text: str, service_provider: ServiceProvider, header=None):
        headers = self.HEADERS

        payload = {"text": text, "service_provider": service_provider.value}

        response = requests.post(
            self.SLASHML_SPEECHIFY_URL, headers=headers, data=payload
        )

        if response.status_code == 500:
            return edict({"status": "ERROR", "reason": response.text})
        elif response.status_code != 200:
            return edict({"status": "ERROR", "reason": response.json()})

        return edict(response.json())

    def status(
        self: "TextToSpeech",
        job_id: str,
        service_provider: ServiceProvider,
        header=None,
    ):
        headers = self.HEADERS
        params = {"service_provider": service_provider.value}
        response = requests.get(
            self.SLASHML_SPEECHIFICATION_STATUS_URL(job_id),
            headers=headers,
            params=params,
        )

        # Check the status code of the response
        if response.status_code == 500:
            return edict({"status": "ERROR", "reason": response.text})
        elif response.status_code != 200:
            return edict({"status": "ERROR", "reason": response.json()})

        return edict(response.json())
