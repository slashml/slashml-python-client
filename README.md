# SlashML Python client
[SlashML](https://www.slashml.com/)
# Introduction
## Overview 
This is a Python client (SDK) for SlashML. It allows the user to use the AI-based apps available and active in [SlashML-Dashboard](https://www.slashml.com/dashboard). 
The apps can be together in the same code as long the input/output structure is compatible. For example, if the user wants to transcribe an audio file and get a summary, they can call speechtotext followed by summarization (speech>text>summary), see [Tutorial](##Quickstart-tutorial).

State-of-the-art AI models from several service providers are available. At SlashML, we also do the benchmarking on these models for the user. This will give them an idea of the best service provider for their application. For the full list of the available models thru SlashML, go to section Available service providers. click [here](##Availlable-service-providers)

## Set up and usage
There is a daily limit (throttling) on the number of calls the user performs,  the code runs without specifying a token (API key),  the throttling kicks in and prevents new jobs after exceeding 10 calls per minute. 

If the user intends on using the service more frequently, it is recommended to generate an token or API key from [SlashML-Dashboard](https://www.slashml.com/dashboard). This way, the throttling limit will increase.

Sign up and Grab your token from [SlashML-Dashboard](https://www.slashml.com/dashboard)>settings> new api key and authenticate by setting it as an environment variable (or when you initialize the service, see Quickstart tutorial):

In your terminal
```
export SLASHML_API_KEY=[token]
```
or including it in your python code as follows:
```

import os
os.environ["SLASHML_API_KEY"] = "slashml_api_token"

```

If the user preferes using the API calls directly, the documentation is available [here](https://www.slashml.com/dashboard).
## Available service providers

### Speech-to-text
For transcription, SlashML supports the following service providers:

* AssemblyAI
* AWS
* Whisper (OpenAI)

### Summarization
For text summarization, SlashML supports the following service providers:

* Meta Bart (thru Huggin-face)
* Da-Vinci (OpenAI)

# Benchmarking
Coming soon
# Quickstart tutorial 

## Introduction

In this tutorial, we use slashml sdk to call speechtotext followed by summarization of the output of speechtotext.

Eventually, benchmarking (coming soon) can help you decide which service provider is the best for you. 

* For speech-to-text: "assembly", "aws", "whisper"
* For summarization: "hugging-face", "openai"

```

import slashml
import os 


# Optional: set environment path
import os
os.environ["SLASHML_API_KEY"] = "0d91bfede9c5c9de6ff1d5610ef71c3b6d5be9ee"

# Import SpeechtoText
speect_to_text = slashml.SpeechToText()

# Optional local file to upload, if not an accessible url
file_location="___local_path___"
# If your audio files aren't accessible via a URL already, you can upload your audio file using this API
upload_url= speect_to_text.upload_audio(file_location)


# choose your service provider: "assembly", "aws", "whisper"
# transcribe
transcribe_id= speect_to_text.transcribe(upload_url,service_provider="aws")
print(transcribe_id)

# Wait and run again
text=speect_to_text.status(transcribe_id,service_provider="aws")
print(text)

# Import summarization
summarize = slashml.Summarization()
# Summarize
summarize_id= summarize.summarize(text,service_provider="hugging-face")
# Wait a while, then run 
summary=summarize.status(job_id=summarize_id,service_provider="hugging-face")
print(summary)

```

et voilà, Next steps:
- pip install slashml
