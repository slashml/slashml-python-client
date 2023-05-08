# SlashML Python client
[SlashML](https://www.slashml.com/)

One API for all your machine learning needs.

# Installation guide

```
pip install slashml
```

# Quickstart

#### Convert text to audio
<!-- write a code snippet in the minimum number of lines  -->

```python
from slashml import TextToSpeech
import time

# Initialize model
model = TextToSpeech()

service_provider = TextToSpeech.ServiceProvider.GOOGLE

# Submit speechification request
job = model.speechify(text="To be or not to be, that is the question!", service_provider=service_provider)

assert job.status != "ERROR", f"{job}"
print(f"Job ID: {job.id}")

# check job status
response = model.status(job.id, service_provider=service_provider)

while response.status == "IN_PROGRESS":
    time.sleep(30)
    response = model.status(job.id, service_provider=service_provider)
    print(f"Response = {response}. Retrying in 30 seconds")

print(response)
```

#### Transcribe an audio file
<!-- write a code snippet in the minimum number of lines  -->

```python
from slashml import SpeechToText
import time

# Initialize model
model = SpeechToText()

service_provider = SpeechToText.ServiceProvider.WHISPER
# Submit transcription request
job = model.transcribe(upload_url="https://slashml.s3.ca-central-1.amazonaws.com/c7d38026-3ab4-4a04-ad9e-b6679ab79a87", service_provider=service_provider)

assert job.status != "ERROR", f"{job}"
print(f"Job ID: {job.id}")

# check job status
response = model.status(job.id, service_provider=service_provider)

while response.status == "IN_PROGRESS":
    time.sleep(5)
    response = model.status(job.id, service_provider=service_provider)
    print(f"Response = {response}. Retrying in 5 seconds")

print(response)
```

#### Summarize a text input
<!-- write a code snippet in the minimum number of lines  -->

```python
from slashml import TextSummarization
import time

# Initialize model
model = TextSummarization()

service_provider = TextSummarization.ServiceProvider.OPENAI

# Submit summariztion request
job = model.summarize(text="There are of course kinds of thinking that can be done without writing. If you don't need to go too deeply into a problem, you can solve it without writing. If you're thinking about how two pieces of machinery should fit together, writing about it probably won't help much. And when a problem can be described formally, you can sometimes solve it in your head. But if you need to solve a complicated, ill-defined problem, it will almost always help to write about it. Which in turn means that someone who's not good at writing will almost always be at a disadvantage in solving such problems.", service_provider=service_provider)

assert job.status != "ERROR", f"{job}"
print(f"Job ID: {job.id}")

# check job status
response = model.status(job.id, service_provider=service_provider)

while response.status == "IN_PROGRESS":
    time.sleep(5)
    response = model.status(job.id, service_provider=service_provider)
    print(f"Response = {response}. Retrying in 5 seconds")

print(response)
```




### View the list of service providers available

```python
from slashml import TextToSpeech

print(TextToSpeech.ServiceProvider.choices())

# you can repeat the same thing for all services 
# print(TextSummarization.ServiceProvider.choices())
# print(SpeechToText.ServiceProvider.choices())

```


# Introduction

## Overview 

This is the Python client (SDK) for SlashML. It allows users to use the endpoints available and active https://docs.slashml.com.

## Set up and usage
There is a daily limit (throttling) on the number of calls the user performs. The code can run without specifying the API key. The throttling kicks in and prevents new jobs after exceeding 10 calls per minute. 

If the user intends on using the service more frequently, it is recommended to generate an token or API key from https://www.slashml.com/settings/api-key. You can pass the API key when creating a model, if you don't the api will still work but you will be throttled.


```python
from slashml import TextToSpeech

# Initialize model
text_to_speech = TextToSpeech(api_key="YOUR_API_KEY")

# summarizer = TextSummarization(api_key="YOUR_API_KEY")
# speech_to_text = SpeechToText(api_key="YOUR_API_KEY")

```


If the user preferes using the API calls directly, the documentation is available [here](https://docs.slashml.com/).

## Available service providers

### Speech-to-text
For transcription, SlashML supports the following service providers:

* [AssemblyAI](https://github.com/AssemblyAI)
* [AWS](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe.html) 
* Whisper ([OpenAI](https://openai.com/blog/whisper/))

### Summarization
For text summarization, SlashML supports the following service providers:

* Meta Bart (thru [Huggin-face](https://huggingface.co/facebook/bart-large-cnn?text=The+tower+is+324+metres+%281%2C063+ft%29+tall%2C+about+the+same+height+as+an+81-storey+building%2C+and+the+tallest+structure+in+Paris.+Its+base+is+square%2C+measuring+125+metres+%28410+ft%29+on+each+side.+During+its+construction%2C+the+Eiffel+Tower+surpassed+the+Washington+Monument+to+become+the+tallest+man-made+structure+in+the+world%2C+a+title+it+held+for+41+years+until+the+Chrysler+Building+in+New+York+City+was+finished+in+1930.+It+was+the+first+structure+to+reach+a+height+of+300+metres.+Due+to+the+addition+of+a+broadcasting+aerial+at+the+top+of+the+tower+in+1957%2C+it+is+now+taller+than+the+Chrysler+Building+by+5.2+metres+%2817+ft%29.+Excluding+transmitters%2C+the+Eiffel+Tower+is+the+second+tallest+free-standing+structure+in+France+after+the+Millau+Viaduct))
* Da-Vinci ([OpenAI](https://beta.openai.com/docs/models/overview))


### Text-to-Speech
For speechification, SlashML supports the following service providers:

* [Google](https://cloud.google.com/text-to-speech/docs/apis)
* [AWS](https://docs.aws.amazon.com/polly/index.html) 


## Documentation

For production ready use cases, look at the [examples](https://github.com/slashml/slashml-python-client/tree/main/examples) folder
