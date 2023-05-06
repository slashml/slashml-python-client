from slashml import SpeechToText, TextSummarization
import time


def speech_to_text(uploaded_audio_url, service_provider, api_key):
    # Initialize model
    model = SpeechToText(api_key=api_key)

    # Submit transcription request
    job = model.transcribe(uploaded_audio_url, service_provider=service_provider)

    assert job.status != "ERROR", f"{job}"
    print(f"Job ID: {job.id}")

    # check job status
    response = model.status(job.id, service_provider=service_provider)

    while response.status == "IN_PROGRESS":
        time.sleep(30)
        response = model.status(job.id, service_provider=service_provider)
        print(f"Response = {response}. Retrying in 30 seconds")

    return response


def summarize(text, service_provider, api_key):
    # Initialize model
    model = TextSummarization(api_key=api_key)

    # Submit request
    job = model.summarize(text=text, service_provider=service_provider)

    assert job.status != "ERROR", f"{job}"
    print(f"Job ID: {job.id}")

    # Check job status
    response = model.status(job.id, service_provider=service_provider)

    # Keep checking job status until the task is complete
    while response.status == "PENDING":
        print(f"Response = {response}. Retrying in 30 seconds")
        time.sleep(30)
        response = model.status(job.id, service_provider=service_provider)

    return response


# Replace `API_KEY` with your SlasML API token. This example still runs without
# the API token but usage will be limited
API_KEY = "b503d137d229fdd4085f59e9ea06ac95d2706182"

service_provider_speech_to_text = SpeechToText.ServiceProvider.AWS
service_provider_summarize = TextSummarization.ServiceProvider.OPENAI

# 10 minute audio file already uploaded
uploaded_url = (
    "https://slashml.s3.ca-central-1.amazonaws.com/fda70f6a-6057-4541-adf1-2cf4f4182929"
)


response_speech_to_text = speech_to_text(uploaded_url, service_provider_speech_to_text, API_KEY)

transcribed_text = response_speech_to_text.transcription_data.transcription
print (f"Transcribed Text = {transcribed_text}")

response_summarize = summarize(transcribed_text, service_provider_summarize, API_KEY)
summary = response_summarize.summarization_data

print (f"Summarized Text = {summary}")