import speechtotext

#initialize SLASHML
API_KEY="1bd15e1c161ff6d4db2ea1d661d7468b4fa61ca9"
speect_to_text = speechtotext.SpeechToText(API_KEY)
# optional local file to upload, if not an accessible url
file_location="/Users/JJneid/Desktop/SlashMl/s2t_experiments/api_tests/test_audio_1.mp3" 

######################################################
# If your audio files aren't accessible via a URL already, you can upload your audio file using this API
upload_url= speect_to_text.upload_audio(file_location)

# choose your service provider: "asemblyai", "aws", "whisper"
service_provider="assembly"
# transcribe
transcribe_id= speect_to_text.transcribe(upload_url,service_provider)
# get the status, the result will be out after the job is done, so we wait a bit :) 
status=speect_to_text.status(transcribe_id,service_provider=service_provider)

# get the text result
## assembly: status["text"]
## whisper: status["transcription_data"]["transcription"]
## aws: retreive result from json file link

print(status["text"])

