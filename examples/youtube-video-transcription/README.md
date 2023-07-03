
## Setup
Create a new python virtual env and install the requirements:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Transcribing a single video
update the `youtube_url` variable at line 36 in `youtube_video_transcription.py` with the url of the video you want to transcribe.

Run the script:

```bash
python3 transcribe_youtube_video.py
```
The result should contain the transcription of the video.

## Multiple Videos
For transcribing a list of videos, update the `youtube_urls` variable at line 8 in `youtube_video_transcription.py` with the list of urls of the videos you want to transcribe.

Then execute the script:

```bash
python transcribe_multiple_youtube_videos.py
```

This will print a list of transcription texts.


For more information, read our docs at https://docs.slashml.com/reference/service/speech_to_text.html
