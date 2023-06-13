### Submit a prediction to the model


#### Request

Then send a post `POST` request to `https://api.slashml.com/model-deployment/v1/models/YOUR-MODEL-ID/predict` with the model-input as the body of the request.

```python
import requests
import json

url = "https://api.slashml.com/model-deployment/v1/models/YOUR-MODEL-ID/predict"

payload = json.dumps({
  "model_input": [
    "steve jobs is the [MASK] of apple"
  ]
})

headers = {
  'Authorization': 'Token a7011983a0f3d64ee113317b1e36f8e5bf56c14a',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```


#### Response (200)

```bash
{
    "id": "a5822206-9680-444c-87ec-4b66a7bcfc26",
    "model_input": [
        "steve jobs is the [MASK] of apple"
    ],
    "model_response": {
        "predictions": [
            {
                "score": 0.516463041305542,
                "sequence": "steve jobs is the founder of apple",
                "token": 3910,
                "token_str": "founder"
            },
            {
                "score": 0.3604991137981415,
                "sequence": "steve jobs is the ceo of apple",
                "token": 5766,
                "token_str": "ceo"
            },
            {
                "score": 0.04929964989423752,
                "sequence": "steve jobs is the president of apple",
                "token": 2343,
                "token_str": "president"
            },
            {
                "score": 0.021112028509378433,
                "sequence": "steve jobs is the creator of apple",
                "token": 8543,
                "token_str": "creator"
            },
            {
                "score": 0.008550147525966167,
                "sequence": "steve jobs is the father of apple",
                "token": 2269,
                "token_str": "father"
            }
        ]
    }
}
```

#### Response (400)

```python
{
    "error": "some error occured when requesting job status",
    "full_message": [
        "{'error': ErrorDetail(string='model not ready', code='permission_denied'), 'reasons': [ErrorDetail(string='model not ready', code='permission_denied'), ErrorDetail(string='model is still being built or deployed', code='permission_denied')]}"
    ]
}
```
