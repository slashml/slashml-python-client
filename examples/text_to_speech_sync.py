from slashml import TextToSpeech

# Replace `API_KEY` with your SlasML API token. This example still runs without
# the API token but usage will be limited
API_KEY = "YOUR_API_KEY"
API_KEY = None
service_provider = TextToSpeech.ServiceProvider.AWS
input_text = "To be or not to be, that is the question!"

# Find all the service providers that we support by running the choices() method
print(f"Available providers: {TextToSpeech.ServiceProvider.choices()}")
print(f"Selected provider: {service_provider}")

model = TextToSpeech(api_key=API_KEY)

# Submit request
job = model.execute(text=input_text, service_provider=service_provider)

print(f"\n\n\n You can access the audio file here: {job.audio_url}")
