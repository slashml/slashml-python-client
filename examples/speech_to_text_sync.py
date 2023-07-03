from slashml import SpeechToText

# Replace `API_KEY` with your SlasML API token. This example still runs without
# the API token but usage will be limited
API_KEY = "YOUR_API_KEY"

service_provider = SpeechToText.ServiceProvider.AWS

# we support many formats, including mp3, mp4, wav, etc.
file_path = "test.mp4"

# Find all the service providers that we support by running the choices() method
print(f"Available providers: {SpeechToText.ServiceProvider.choices()}")
print(f"Selected provider: {service_provider}")


model = SpeechToText(api_key=API_KEY)

# Upload audio
uploaded_file = model.upload_audio(file_path)
print(f"file uploaded: {uploaded_file}")

response = model.execute(
    upload_url=uploaded_file["upload_url"], service_provider=service_provider
)

print(f"\n\n\n\nTranscription = {response.transcription_data.transcription}")
