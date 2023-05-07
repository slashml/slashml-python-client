from slashml import SpeechToText, services

# Replace `API_KEY` with your SlasML API token. This example still runs without
# the API token but usage will be limited
API_KEY = None
service_provider = SpeechToText.ServiceProvider.ASSEMBLY
audio_filepath = "test.mp3"

# Find all the service providers that we support by running the choices() method
print(f"Available providers: {SpeechToText.ServiceProvider.choices()}")
print(f"Selected provider: {service_provider}")

response = services.speech_to_text(
    audio_filepath=audio_filepath, service_provider=service_provider, api_key=API_KEY
)
print(f"{response}\n\nTranscription = {response.transcription_data.transcription}")
