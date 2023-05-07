from slashml import SpeechToText, TextSummarization, services


# Replace `API_KEY` with your SlasML API token. This example still runs without
# the API token but usage will be limited
API_KEY = "b503d137d229fdd4085f59e9ea06ac95d2706182"

service_provider_speech_to_text = SpeechToText.ServiceProvider.AWS
service_provider_summarize = TextSummarization.ServiceProvider.OPENAI

# 10 minute audio file already uploaded
uploaded_url = (
    "https://slashml.s3.ca-central-1.amazonaws.com/fda70f6a-6057-4541-adf1-2cf4f4182929"
)

 # Convert audio to text
response_speech_to_text = services.speech_to_text(
    uploaded_url, service_provider_speech_to_text, API_KEY
)

# Extract text from API response
transcribed_text = response_speech_to_text.transcription_data.transcription
print(f"Transcribed Text = {transcribed_text}")

# Summarize text
response_summarize = services.summarize_text(
    transcribed_text, service_provider_summarize, API_KEY
)
summary = response_summarize.summarization_data

print(f"Summarized Text = {summary}")
