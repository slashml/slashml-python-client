## Instructions

1. Send a POST request to `https://api.slashml.com/text-to-speech/v1/upload/` with the text in the body. Save the id in the response object returned.
2. Check the status of the speechification by sending a `GET` request to `https://api.slashml.com/speech-to-text/v1/jobs/YOUR-JOB-ID/`

## Code Blocks

### Convert text to audio

The body of the request should contain a field `text`, the value of which shall contain the relevant text that you want to generate an audio file for.

```bash
POST https://api.slashml.com/text-to-speech/v1/jobs/
```

#### Request

```python
import requests

url = 'https://api.slashml.com/text-to-speech/v1/jobs/'

payload = {
  "text": "this is my text that I want to convert to an audio file"
  "service_provider": 'google'
}
headers = {
    "Authorization": "Token <YOUR_API_KEY>",
}

response = requests.post(url, headers=headers, data=payload)
print(response.text)
```

> Note: 
> Possible values for service_provider are 'X' and 'Y'

#### Response (200)

```bash
{
    # keep track of the id for later
    "id": "dbe42f9c-f0ce-4683-af80-e6c250b21460",
    "status": "COMPLETED",

    # url to publicly hosted audio file
    "audio_url": "https://slashml.s3.ca-central-1.amazonaws.com/70c34009-8149-4b47-8a6e-29dcb5bd3d3d.mp3"
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