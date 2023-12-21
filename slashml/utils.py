

import os
from addict import Dict
import requests


def envApiKey():
    return "SLASHML_API_KEY"


def apiRoot():
    # return "http://localhost:8000"
    return "https://api.slashml.com"


def baseUrl(service_name, version):
    return f"{apiRoot()}/{service_name}/{version}"


def generateURL(*path):
    return "/".join(d for d in path)


def generateHeaders(api_key):
    if api_key:
        return {"authorization": f"Token {api_key}"}
    if os.environ.get(envApiKey()):
        key_env = os.environ.get(envApiKey())
        return {"authorization": f"Token {key_env}"}
    log(noTokenWarning())
    return None


def formatResponse(response):
    if response.status_code == 500:
        return Dict({"status": "ERROR", "reason": response.text})
    elif response.status_code != 200:
        return Dict({"status": "ERROR", "reason": response.json()})
    return Dict(response.json())


def getTaskStatus(base_url, headers, job_id, service_provider):
    url = generateURL(base_url, "jobs", job_id)
    params = {"service_provider": service_provider.value}
    response = requests.get(url, headers=headers, params=params)
    return formatResponse(response)


def noTokenWarning():
    return "No API Key provided, there are certain limits to the usage"


def log(msg):
    print(msg)
