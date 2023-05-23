# Speech To Text

This service exposes the speech-to-text models from a variety of different vendors.

### Time to Integrate

Less than 5 minute

### Service Providers
- Assembly AI
- AWS
- Whisper

### Instructions

1. (Optional) Upload files to a static server by sending `POST` request to `https://api.slashml.com/speech-to-text/v1/upload/` where the data points to your audio file. Save the `upload_url`. You can use this url link in the rest of the calls.
2. Submit your audio file for transcription by sending `POST` request to `https://api.slashml.com/speech-to-text/v1/jobs/`. The body should contain a json object with `audio_url` which points to an audio file that is publicly available. Save the `id` in the response object.
3. Check the status of the transcription by sending a `GET` request to `https://api.slashml.com/speech-to-text/v1/jobs/YOUR-TRANSCRIPT-ID/`

> Note: 
> The uploaded_url will be used when submitting a transcription job.

## Code Blocks

### Upload audio file to static storage

If your audio files aren't accessible via a URL already (like in an S3 bucket, or a static file server), you can upload your audio file using this API. All uploads have a 24hr deletion policy.

```bash
POST https://api.slashml.com/speech-to-text/v1/upload/
```

#### Request

```python
import requests

url = "https://api.slashml.com/speech-to-text/v1/upload/"

headers = {'authorization': "Token <YOUR_API_KEY>"}
payload = { 'service_provider':'assembly' }
files=[
  ('audio',('test_audio.mp3',open('/path/to/your_audio.mp3','rb'),'audio/mpeg'))
]

response = requests.post(url, headers = headers, data = payload, files = files)

print(response.text)
```

#### Response (200)

```bash
{
    "uploaded_url": "https://cdn.slashml.com/upload/ccbbbfaf-f319-4455-9556-272d48faaf7f"
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
> The uploaded_url will be used when submitting a transcription job.

### Check status of transcription

Now that the audio file has been submitted for transcription, we can make requests to GET the status of the transcription, and eventually the result of the transcription.

```bash
GET https://api.slashml.com/speech-to-text/v1/transcription/YOUR-TRANSCRIPT-ID/
```

#### Request

```python
import requests

url = 'https://api.slashml.com/speech-to-text/v1/jobs/YOUR-TRANSCRIPT-ID/?service_provider=assembly'

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
> The status will go from 'QUEUED' to 'IN_PROGRESS' to 'COMPLETED'. If there's an error transcribing your file, the status will go to 'ERROR' and there will be an 'ERROR' key in the response JSON which will contain more information.