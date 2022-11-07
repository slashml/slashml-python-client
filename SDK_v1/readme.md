SDK for SlashML documentation:
- methods: upload_audio, transcribe, status 

Steps to Integrate
1 - (Optional) Upload files where the data points to your audio file
```
speect_to_text = speechtotext.SpeechToText()
file_location="/Users/JJneid/Desktop/SlashMl/s2t_experiments/api_tests/test_audio_1.mp3"
# when
API_KEY="1bd15e1c161ff6d4db2ea1d661d7468b4fa61ca9"
model_choice="assembly"
result = speect_to_text.upload_audio(file_location,API_KEY, model_choice)
```
Save the upload_url. You can use this url link in the rest of the calls.

2- Submit your audio file for transcription by sendingPOST request tohttps://api.slashml.com/speech-to-text/v1/transcribe/. The body should contain a json object with audio_url which points to an audio file that is publicly available.
Save the id in the response object.

3 - Check the status of the transcription by sending a GETrequest tohttps://api.slashml.com/speech-to-text/v1/transcription/

Next steps:
- pip install slashml
- add SLASH_API_KEY to sys path
