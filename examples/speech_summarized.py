
from slashml import SpeechToText, Summarization
import time

# Initialize your model
model = SpeechToText()

service_provider = model.ServiceProvider.AWS

# long audio file already uploaded
upload_url = 'https://slashml.s3.ca-central-1.amazonaws.com/fda70f6a-6057-4541-adf1-2cf4f4182929'

# # choose a service provider and transcribe
print('transcribing file')
job = model.transcribe(
    upload_url, 
    service_provider=service_provider
    )

assert job.status != 'ERROR', f'{job}'

print('transcription job id', job.id)

# check the status
response = model.status(job.id, service_provider=service_provider)

while response.status != 'COMPLETED':
    print(f'response got', response , 'trying again')
    time.sleep(30)
    response = model.status(job.id, service_provider = service_provider)

text_to_summarize = response.transcription_data.transcription

print('summarizing text', text_to_summarize)

model:Summarization = Summarization()
service_provider = model.ServiceProvider.OPENAI

print('summarizing text')
# choose a service provider and transcribe
job = model.summarize(
    text=text_to_summarize, 
    service_provider=service_provider
    )

assert job.status != 'ERROR', f'{job}'

print('summarization job id', job.id)

# check the status
response = model.status(job.id, service_provider=service_provider)

while response.status != 'COMPLETED':
    print(f'response got', response , 'trying again')
    time.sleep(30)
    response = model.status(job.id, service_provider = service_provider)

print(response.summarization_data)