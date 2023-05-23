This service exposes the speech-to-text models from a variety of different vendors.

## Time to Integrate

Less than 5 minute

## Service Providers
- Assembly AI
- AWS
- Whisper

## Instructions

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