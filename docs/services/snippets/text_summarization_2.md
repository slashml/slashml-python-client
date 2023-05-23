## Instructions

1. Copy your text and pass it in the body of a `POST` request to `https://api.slashml.com/speech-to-text/v1/jobs/`. The body should contain a json object with text field. Which contains the body of the text that you want to summarize. Save the `id` in the response object.
2. Check the status of the transcription by sending a `GET` request to `https://api.slashml.com/speech-to-text/v1/jobs/`

## Code Blocks

### Submit text input for summarization

If your audio files aren't accessible via a URL already (like in an S3 bucket, or a static file server), you can upload your audio file using this API. All uploads are immediately deleted after transcription, we do not store the uploads.

```bash
POST https://api.slashml.com/summarization/v1/summarize/
```

#### Request

```python
import requests
  
  url = 'https://api.slashml.com/speech-to-text/v1/jobs/'
  
  payload = {
  "text": 
  
  '''One reason programmers dislike meetings so much is that they're on a different type of schedule from other people. Meetings cost them more.
  
  There are two types of schedule, which I'll call the manager's schedule and the maker's schedule. The manager's schedule is for bosses. It's embodied in the traditional appointment book, with each day cut into one hour intervals. You can block off several hours for a single task if you need to, but by default you change what you're doing every hour.''',

  "service_provider": "openai"
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
    # keep track of this id for later
    "id": "94f52a16-f2d9-4212-be98-ac87eb068d22",
    "status": "IN_PROGRESS",
    "created": "2022-12-24T01:14:18.543943Z"
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
> The 'id' will be used to fetch the status of the summarization job.