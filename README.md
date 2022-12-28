# SlashML Python client
[SlashML](https://www.slashml.com/)
# Introduction
## Overview 
This is a Python client (SDK) for SlashML. It allows the user to use the apps available and active in [SlashML-Dashboard](https://www.slashml.com/dashboard). 
The apps can be together in the same code. For example, if the user wants to transcribe an audio file and get a summary, they can call speechtotext followed by summarization.

State-of-the-art AI models from several service providers are available. At SlashML, we also do the benchmarking on these models for the user. This will give them an idea of the best service provider for their application. For the full list of the available models thru SlashML, click [here](##availlable-service-providers)



to lets you run transcription jobs from your Python code or Jupyter notebook. The transcription can be done with three lines of code
```
import slashml

speect_to_text = slashml.SpeechToText()
transcribe_id= speect_to_text.transcribe(audio_url,service_provider="aws")
status=speect_to_text.status(transcribe_id,service_provider=service_provider)

```

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
## Availlable service providers

### Speech-to-text

AssemblyAI
AWS
Whisper (OpenAI)

### Summarization
hugging-face summarization based on Meta... include links
# Quickstart tutorial 

## Introduction

### Start with initializing the service 

### Specify your service provider

In this step, benchmarking will help you decide which service provider is the best for you. 
For speech-to-text: "assembly", "aws", "whisper"
For summarization: "hugging-face", "openai"


et voilà, Next steps:
- pip install slashml
