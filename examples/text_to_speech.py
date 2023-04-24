
from slashml import TextToSpeech

# Initialize your model
model = TextToSpeech()
# model = SpeechToText()

service_provider = model.ServiceProvider.AWS

# # choose a service provider and transcribe
job = model.speechify(
    text ='this is my text',
    service_provider=service_provider
    )

print(job)