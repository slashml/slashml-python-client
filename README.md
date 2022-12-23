# SLASHML Python client

This is a Python client for SLASHML. It lets you run transcription jobs from your Python code or Jupyter notebook. Do a transcription job with three lines of code
```
import speechtotext

speect_to_text = speechtotext.SpeechToText()
transcribe_id= speect_to_text.transcribe(audio_url,service_provider="aws")
status=speect_to_text.status(transcribe_id,service_provider=service_provider)

```
There is a daily limit (throttling) on the number of calls the user performs, transcription jobs can be done without specifying a token (API key). If the user intends on using the service more frequently, it is recommended to generate an token or API key from the dashboard @ [Slashml.com](https://www.slashml.com/).

Grab your token from [https://www.slashml.com/dashboard] (>settings> new api key) and authenticate by setting it as an environment variable (or when you initialize the service, see examples):
```
export SLASHML_API_KEY=[token]
```
or including it in your code as follows:
```
import speechtotext
API_KEY="your_api_key"
speect_to_text = speechtotext.SpeechToText(API_KEY)
transcribe_id= speect_to_text.transcribe(audio_url,service_provider="aws")
status=speect_to_text.status(transcribe_id,service_provider=service_provider)

```

-- update from this part, include examples, sign up, token, service providers, type of servies, benchmarking, link to pricing, Tutorial examples/examples


SDK for SlashML documentation:
- methods: upload_audio, transcribe, status 

Steps to Integrate
1 - (Optional) Upload files where the data points to your audio file
```
# call the class
speect_to_text = speechtotext.SpeechToText()
file_location="path/to/your/file.mp3"
# when
API_KEY="SLASH_ML_API_KEY"
model_choice="assembly"
result_upload = speect_to_text.upload_audio(file_location,API_KEY, model_choice)
print(result_upload)
```
Save the upload_url. You can use this url link in the rest of the calls.


2- Submit your audio file for transcription
```
upload_url=upload_url # you can skip step 1 and just input the accessible link of your # file)

result_transcribe = speect_to_text.transcribe(upload_url,API_KEY, model_choice)

print(result_transcribe)
```
Save the id in the response object.


3 - Check the status and get the text result of the transcription
```
job_id= id
result_status = speect_to_text.status(job_id,API_KEY, model_choice=model_choice)

### get the full details of the result
print(result_status)
### get the text reulst only
print(json.loads(result)["text"])
```


et voilà, Next steps:
- pip install slashml
- add SLASH_API_KEY to sys path
