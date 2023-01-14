import slashml
import os 
from time import sleep 


# set environment path
import os
os.environ["SLASHML_API_KEY"] = "0d91bfede9c5c9de6ff1d5610ef71c3b6d5be9ee"

# Import SpeechtoText
speect_to_text = slashml.SpeechToText()
# optional local file to upload, if not an accessible url
file_location="/Users/JJneid/Desktop/SlashMl/s2t_experiments/api_tests/test_audio_1.mp3"
# If your audio files aren't accessible via a URL already, you can upload your audio file using this API
upload_url= speect_to_text.upload_audio(file_location)
# choose your service provider: "assembly", "aws", "whisper"
# transcribe
transcribe= speect_to_text.transcribe(upload_url,service_provider="aws")
print(transcribe)

# if name error, wait and re-run again
sleep(30)
text=speect_to_text.status(transcribe,service_provider="aws")
print(text)

# Import summarization
summarize = slashml.Summarization()
# transcribe
summarize_id= summarize.summarize(text,service_provider="hugging-face")
# wait a while, then run (name error, wait and re run)
sleep(25)
summary=summarize.status(job_id=summarize_id,service_provider="hugging-face")
print(summary)