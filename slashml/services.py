from slashml import TextSummarization, SpeechToText
import time


def summarize_text(text, service_provider, api_key):
    # Initialize model
    model = TextSummarization(api_key=api_key)

    # Submit request
    job = model.summarize(text=text, service_provider=service_provider)

    assert job.status != "ERROR", f"{job}"
    print(f"Job ID: {job.id}")

    # Check job status
    response = model.status(job.id, service_provider=service_provider)

    # Keep checking job status until the task is complete
    while response.status == "IN_PROGRESS":
        print(f"Response = {response}. Retrying in 30 seconds")
        time.sleep(30)
        response = model.status(job.id, service_provider=service_provider)

    return response


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
