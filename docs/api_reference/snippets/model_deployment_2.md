## Instructions

1. (Optional) For deployment we recommend using the python SDK. However, you can also push your model using an API. To do this, you will first have to install `truss` to create a truss folder locally. Then compress that truss folder into a `.tar.gz` file. Then send a post `POST` request to `https://api.slashml.com/model-deployment/v1/models` with the compressed file as the body of the request. Save the `id` in the response object.
2. Check the status of the model deployment by sending a `GET` request to `https://api.slashml.com/model-deployment/v1/models/YOUR-MODEL-ID/status`
3. You can make predctions on the deployed model by sending a `POST` request to `https://api.slashml.com/model-deployment/v1/models/YOUR-MODEL-ID/predict`. The body should contain a json object with `model_input` which is the input prompt to the model.


## Code Blocks

### Submit model for deployment

Install truss

```
pip install truss
```


You can the create a truss object by running the following command from within Python


```python

# you might have to install transfomers and torch
from transformers import pipeline

def train_model():
    # Bring in model from huggingface
    return pipeline('fill-mask', model='bert-base-uncased')

my_model = train_model()

# save the model
truss.create(my_model, 'my_model')
```

Then convert the folder into a `.tar.gz` file

```bash
tar -czvf my_model.tar.gz my_model
```

#### Request

Then send a post `POST` request to `https://api.slashml.com/model-deployment/v1/models` with the compressed file as the body of the request. Save the `id` in the response object.

```python
import requests

url = "https://api.slashml.com/model-deployment/v1/models/"

payload={'model_name': 'test-dep-model'}

files=[
  ('model_file',('my_model.tar.gz',open('path/to/my_model.tar.gz','rb'),'application/octet-stream'))
]

headers = {
  'Authorization': 'Token YOUR_TOKEN'
}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.json())
```


#### Response (200)

```bash
{
    "id": "a5822206-9680-444c-87ec-4b66a7bcfc26",
    "created": "2023-06-13T06:38:55.311751Z",
    "status": "IN_PROGRESS",
    "name": "'test-dep-model'"
}
```

#### Response (400)

```python
{
    "error" : {
        "message" : "something bad happened",
    }
}
```
