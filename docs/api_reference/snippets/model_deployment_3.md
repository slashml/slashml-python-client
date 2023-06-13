### Check status of model

```bash
GET https://api.slashml.com/model-deployment/v1/models/YOUR-MODEL-ID/status
```

#### Request

```python
import requests

url = 'https://api.slashml.com/model-deployment/v1/models/YOUR-MODEL-ID/status'

headers = {
  'Authorization': 'Token <YOUR_API_KEY>'
}

response = requests.get(url, headers=headers, data=payload)
print(response.json())

```

#### Response (200) - MODEL-READy

```bash
{
    # keep track of the id for later
    "id": "ozfv3zim7-9725-4b54-9b71-f527bc21e5ab",
    "created": "2023-06-13T06:38:55.311751Z",
    "name": "test-dep-model",
    "status": "MODEL_READY",
    "name": "test-dep-model",
}
```

#### Response (400) - Error

```bash
{
    "error" : {
        "message" : "something bad happened"
    }
}

```

> Note: 
> The status will go from 'QUEUED' to 'BUILDING_MODEL' to 'DEPLOYING_MODEL' to 'MODEL_READY'. If there's an error processing your input, the status will go to 'FAILURE' and there will be an 'ERROR' key in the response JSON which will contain more information.