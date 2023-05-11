from slashml import SpeechToText
import time

# update the examples using execute from the SpeechToText class

def speech_to_text(audio_filepath, service_provider, api_key):
    # Initialize model
    model = SpeechToText(api_key=api_key)

    # Upload audio
    uploaded_file = model.upload_audio(audio_filepath)
    print(f"file uploaded: {uploaded_file}")

    # Submit transcription request
    job = model.transcribe(
        uploaded_file["upload_url"], service_provider=service_provider
    )

    assert job.status != "ERROR", f"{job}"
    print(f"Job ID: {job.id}")

    # check job status
    response = model.status(job.id, service_provider=service_provider)

    while response.status == "IN_PROGRESS":
        print(f"Response = {response}. Retrying in 30 seconds")
        time.sleep(30)
        response = model.status(job.id, service_provider=service_provider)

    return response


# Replace `API_KEY` with your SlasML API token. This example still runs without
# the API token but usage will be limited
API_KEY = None
service_provider = SpeechToText.ServiceProvider.ASSEMBLY
audio_filepath = "test.mp3"

# Find all the service providers that we support by running the choices() method
print(f"Available providers: {SpeechToText.ServiceProvider.choices()}")
print(f"Selected provider: {service_provider}")


response = speech_to_text(
    audio_filepath=audio_filepath, service_provider=service_provider, api_key=API_KEY
)
print(f"{response}\n\nTranscription = {response.transcription_data.transcription}")
