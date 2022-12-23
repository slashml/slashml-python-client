import speechtotext
import os 

#API KEY (optional)
#API_KEY="0d91bfede9c5c9de6ff1d5610ef71c3b6d5be9ee"
# set environment path
os.environ["SLASHML_API_KEY"] = "0d91bfede9c5c9de6ff1d5610ef71c3b6d5be9ee"
# Initialize SlashML 
speect_to_text = speechtotext.SpeechToText()
# optional local file to upload, if not an accessible url
# file_location="/Users/JJneid/Desktop/SlashMl/s2t_experiments/api_tests/test_french_english.mp3"
# # If your audio files aren't accessible via a URL already, you can upload your audio file using this API
# upload_url= speect_to_text.upload_audio(file_location)
# print(upload_url)
# choose your service provider: "asembly", "aws", "whisper"
service_provider="aws"
# transcribe
transcribe_id= "e5f43d08-6fa4-4cd7-86f9-2fb172004032"

# get the status, the result will be out after the job is done, so we wait a bit :) 
status=speect_to_text.status(transcribe_id,service_provider=service_provider)
# get the text result: status["transcription_data"]["transcription"]
print(status)
#print(status["transcription_data"]["transcription"])