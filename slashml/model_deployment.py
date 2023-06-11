import json
import requests
import time
import tarfile
import truss
from enum import Enum
from .utils import generateURL, baseUrl, generateHeaders, formatResponse, getTaskStatus


import os


class ModelDeployment:
    _base_url = baseUrl("model-deployment", "v1")
    _headers = None

    def __init__(self, api_key: str = None):
        if api_key==None:
            raise Exception("API Key is required for model deployment")
        self._headers = generateHeaders(api_key)

    def create_tar_gz(self, *, folder_path, tar_gz_filename):
        with tarfile.open(tar_gz_filename, "w:gz") as tar:
            tar.add(folder_path, arcname=os.path.basename(folder_path))

    def deploy(self, *, model_name:str, model: str):
        """Submit job"""
        truss.create(model, 'my_model')
        self.create_tar_gz(folder_path='my_model', tar_gz_filename='my_model.tar.gz')

        url = generateURL(self._base_url, "models")
        files = [("model_file", ("my_model.tar.gz", open('my_model.tar.gz', "rb"), "application/octet-stream"))]

        payload = {
            "model_name": model_name,
        }

        import pdb
        pdb.set_trace()

        response = requests.post(url, headers=self._headers, data=payload, files=files)

        return formatResponse(response)

    def status(self, *, model_version_id: str):
        """Check job status"""
        url = generateURL(self._base_url, "models", model_version_id, "status")
        response = requests.get(url, headers=self._headers)
        return formatResponse(response)
    
    def predict(self, model_version_id: str, model_input:str):
        """Check job status"""

        payload = json.dumps({
            "model_input": model_input
        })

        url = generateURL(self._base_url, "models", model_version_id, "predict")
        self._headers['Content-Type'] = 'application/json'
        response = requests.post(url, headers=self._headers, data=payload)
        return formatResponse(response)
