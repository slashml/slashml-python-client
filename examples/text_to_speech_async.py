from slashml import TextToSpeech
import time

# Replace `API_KEY` with your SlasML API token. This example still runs without
# the API token but usage will be limited
API_KEY = "YOUR_API_KEY"
service_provider = TextToSpeech.ServiceProvider.AWS
input_text = "To be or not to be, that is the question!"

# Find all the service providers that we support by running the choices() method
print(f"Available providers: {TextToSpeech.ServiceProvider.choices()}")
print(f"Selected provider: {service_provider}")

model = TextToSpeech(api_key=API_KEY)

# Submit request
job = model.submit_job(text=input_text, service_provider=service_provider)
print(job)

# check job status
response = model.status(job.id, service_provider=service_provider)

while response.status == "IN_PROGRESS":
    print(f"Response = {response}. Retrying in 30 seconds")
    time.sleep(30)
    response = model.status(job.id, service_provider=service_provider)

print (f"\nYou can access the audio file here: {response.audio_url}")
