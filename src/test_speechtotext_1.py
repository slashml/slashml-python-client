import slashml
import os 

#API KEY (optional)

# set environment path
os.environ["SLASHML_API_KEY"] = "0d91bfede9c5c9de6ff1d5610ef71c3b6d5be9ee"
# Initialize SlashML 
speect_to_text = slashml.SpeechToText()
# optional local file to upload, if not an accessible url
file_location="/Users/JJneid/Desktop/SlashMl/Benchmarking/podcast1/podcast1_long_trim.mp3"
# If your audio files aren't accessible via a URL already, you can upload your audio file using this API
upload_url= speect_to_text.upload_audio(file_location)
# choose your service provider: "asembly", "aws", "whisper"
service_provider="aws"
# transcribe
transcribe_id= speect_to_text.transcribe(upload_url,service_provider)
print(transcribe_id)

status=speect_to_text.status(transcribe_id,service_provider=service_provider)
print(status)