### Convert audio to text

The body of the request should contain a field `uploaded_audio_url`, the value of which shall contain the link to the uploaded audio url, and `service_provider` which is the name of the service provider you want to use.

```bash
POST https://api.slashml.com/speech-to-text/v1/jobs/
```

#### Request

```python
import requests

url = 'https://api.slashml.com/speech-to-text/v1/jobs/'

payload = {
  "uploaded_audio_url": "https://cdn.slashml.com/upload/ccbbbfaf-f319-4455-9556-272d48faaf7f",
  "service_provider": 'assembly'
}
headers = {
    "Authorization": "Token <YOUR_API_KEY>",
}

response = requests.post(url, headers=headers, data=payload)
print(response.text)
```

#### Response (200)

```bash
{
    # keep track of the id for later
    "id": "ozfv3zim7-9725-4b54-9b71-f527bc21e5ab",
    # note that the status is now "processing"
    "status": "IN_PROGESS",        
    "audio_duration": null,
    "audio_url": "https://cdn.slashml.com/upload/ccbbbfaf-f319-4455-9556-272d48faaf7f",
    "text": null,
}
```

#### Response (400)

```bash
{
    "error" : {
        "message" : "something bad happened"
    }
}
```

> Note: 
> The 'id' will be used to fetch the status of the job, in the status endpoint.