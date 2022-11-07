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
upload_url=upload_url

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
