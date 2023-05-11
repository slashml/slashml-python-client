from slashml import SpeechToText, TextSummarization, TextToSpeech

# Replace `API_KEY` with your SlasML API token. This example still runs without
# the API token but usage will be limited
API_KEY = "a7011983a0f3d64ee113317b1e36f8e5bf56c14a"

service_provider_speech_to_text = SpeechToText.ServiceProvider.ASSEMBLY
service_provider_summarize = TextSummarization.ServiceProvider.OPENAI
service_provider_text_to_speech = TextToSpeech.ServiceProvider.AWS

# 10 minute audio file already uploaded
uploaded_url = (
    "https://slashml.s3.ca-central-1.amazonaws.com/fda70f6a-6057-4541-adf1-2cf4f4182929"
)

transcribe = SpeechToText(api_key=API_KEY)
summarize = TextSummarization(api_key=API_KEY)
speechify = TextToSpeech(api_key=API_KEY)


response = transcribe.execute(
    upload_url=uploaded_url, service_provider=service_provider_speech_to_text
)

transcribed_text = response.transcription_data.transcription
print (f"Transcribed Text = {transcribed_text}")

response_summarize = summarize.execute(transcribed_text, service_provider_summarize)

summary = response_summarize.summarization_data

print (f"Summarized Text = {summary}")

response = speechify.execute(summary, service_provider_text_to_speech)

print (f"\n\n\n You can access the audio file here: {response.audio_url}")