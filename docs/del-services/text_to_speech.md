# Text To Speech

This service provides the best performing automatic speechification models from a variety of different vendors.

### Time to Integrate

Less than 1 minute

### Service Providers
- Google
- AWS

### Instructions

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
> Possible values for service_provider are 'google' and 'aws'

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


### Check status of transcription

Now that the text has been submitted for speech synthesis, we can make requests to GET the status of the synthesis, and eventually the output audio file.

```bash
GET https://api.slashml.com/speech-to-text/v1/transcription/YOUR-TRANSCRIPT-ID/
```

#### Request

```python
import requests

url = 'https://api.slashml.com/text-to-speech/v1/jobs/YOUR-TRANSCRIPT-ID/?service_provider=google'

headers = {
  'Authorization': 'Token <YOUR_API_KEY>'
}

response = requests.get(url, headers=headers)
  
print(response.text)
```

#### Response (200) - In Progress

```bash
{
    "id": "dbe42f9c-f0ce-4683-af80-e6c250b21460",
    "status": "IN_PROGRESS",
}
```

#### Response (200) - Completed

```bash
{
    "id": "dbe42f9c-f0ce-4683-af80-e6c250b21460",
    "status": "COMPLETED",
    "audio_url": "https://slashml.s3.ca-central-1.amazonaws.com/70c34009-8149-4b47-8a6e-29dcb5bd3d3d.mp3"
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
> The status will go from 'QUEUED' to 'IN_PROGRESS' to 'COMPLETED'. If there's an error transcribing your file, the status will go to 'ERROR' and there will be an 'ERROR' key in the response JSON which will contain more information.

