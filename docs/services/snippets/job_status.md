### Check status of job

Now that the audio file has been submitted for transcription, we can make requests to GET the status of the transcription, and eventually the result of the transcription.

```bash
GET https://api.slashml.com/speech-to-text/v1/status/YOUR-JOB-ID/
```

#### Request

```python
import requests

url = 'https://api.slashml.com/speech-to-text/v1/jobs/YOUR-JOB-ID/?service_provider=assembly'

headers = {
  'Authorization': 'Token <YOUR_API_KEY>'
}

response = requests.get(url, headers=headers, data=payload)
print(response.text)
```

#### Response (200) - In Progress

```bash
{
    # keep track of the id for later
    "id": "ozfv3zim7-9725-4b54-9b71-f527bc21e5ab",
    # note that the status is now "processing"
    "status": "IN_PROGESS",        
    "acoustic_model": "assemblyai_default",
    "language_model": "assemblyai_default",
    "audio_duration": null,
    "audio_url": "https://s3-us-west-2.amazonaws.com/blog.assemblyai.com/audio/8-7-2018-post/7510.mp3",
    "confidence": null,
    "dual_channel": null,
    "text": null,
    "words": null
}
```

#### Response (200) - Completed

```bash
{
    "id": "5551722-f677-48a6-9287-39c0aafd9ac1",
    "status": "COMPLETED",
    "acoustic_model": "assemblyai_default",
    "language_model": "assemblyai_default",
    "audio_duration": 12.0960090702948,
    "audio_url": "https://s3-us-west-2.amazonaws.com/blog.assemblyai.com/audio/8-7-2018-post/7510.mp3",
    "confidence": 0.956,
    "dual_channel": null,
    "text": "You know Demons on TV like that and and for people to expose themselves to being rejected on TV or humiliated by fear factor or.",
    "words": [
        {
            "confidence": 1.0,
            "end": 440,
            "start": 0,
            "text": "You"
        },
        ...
        {
            "confidence": 0.96,
            "end": 10060,
            "start": 9600,
            "text": "factor"
        },
        {
            "confidence": 0.97,
            "end": 10260,
            "start": 10080,
            "text": "or."
        }
    ]
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
> The status will go from 'QUEUED' to 'IN_PROGRESS' to 'COMPLETED'. If there's an error processing your input, the status will go to 'ERROR' and there will be an 'ERROR' key in the response JSON which will contain more information.