from slashml.slashml import SpeechToText
import time

# Initialize your model
model = SpeechToText()
# model = SpeechToText()

service_provider = model.ServiceProvider.ASSEMBLY

uploaded_file = model.upload_audio("test.mp3")
print(uploaded_file)

# # choose a service provider and transcribe
job = model.transcribe(
    uploaded_file['upload_url'], 
    service_provider=service_provider
    )

assert job.status != 'ERROR', f'{job}'
print('transcription job id', job.id)

# check the status
response = model.status(job.id, service_provider=service_provider)

while response.status != 'COMPLETED':
    time.sleep(30)
    response = model.status(job.id, service_provider = service_provider)
    print(f'response got', response , 'trying agagin')

print(response.transcription_data.transcription)