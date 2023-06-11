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

# Replace `API_KEY` with your SlasML API token. This example still runs without
# the API token but usage will be limited
model = TextToSpeech(api_key=None)

input_text = "to be or not to be, that is the question!"

# Submit request
job = model.execute(text=input_text, service_provider=TextToSpeech.ServiceProvider.AWS)

print (f"\n\n\n You can access the audio file here: {job.audio_url}")
```

#### Transcribe an audio file
<!-- write a code snippet in the minimum number of lines  -->

```python
from slashml import SpeechToText

# Replace `API_KEY` with your SlasML API token. This example still runs without
# the API token but usage will be limited
model = SpeechToText(api_key=None)

response = model.execute(
    upload_url='https://slashml.s3.ca-central-1.amazonaws.com/695c711f-9f5d-4ff1-ae4f-4439842eef5f', 
    service_provider=SpeechToText.ServiceProvider.WHISPER
)

print(f"\n\n\n\nTranscription = {response.transcription_data.transcription}")

```

#### Summarize a text input
<!-- write a code snippet in the minimum number of lines  -->

```python
from slashml import TextSummarization

model = TextSummarization(api_key=None)

input_text = """A good writer doesn't just think, and then write down what he thought, as a sort of transcript. A good writer will almost always discover new things in the process of writing. And there is, as far as I know, no substitute for this kind of discovery. Talking about your ideas with other people is a good way to develop them. But even after doing this, you'll find you still discover new things when you sit down to write. There is a kind of thinking that can only be done by writing."""

response = model.execute(text=input_text, service_provider=TextSummarization.ServiceProvider.OPENAI)

print(f"Summary = {response.summarization_data}")

```


#### Deploy your own Model
<!-- write a code snippet in the minimum number of lines  -->

Note: this examples requires the `transformers` and `torch` packages to be installed. You can install them with `pip install transformers torch`

```
pip install transformers torch
```

```python
from slashml import ModelDeployment
import time

# you might have to install transfomers and torch
from transformers import pipeline

def train_model():
    # Bring in model from huggingface
    return pipeline('fill-mask', model='bert-base-uncased')

my_model = train_model()

# Replace `API_KEY` with your SlasML API token.
API_KEY = "YOUR_API_KEY"

model = ModelDeployment(api_key=API_KEY)

# deploy model
response = model.deploy(model_name='my_model_3', model=my_model)

# wait for it to be deployed
time.sleep(2)
status = model.status(model_version_id=response.id)

while status.status != 'READY':
    print(f'status: {status.status}')
    print('trying again in 5 seconds')
    time.sleep(5)
    status = model.status(model_version_id=response.id)

    if status.status == 'FAILED':
        raise Exception('Model deployment failed')

# submit prediction
input_text = 'Steve jobs is the [MASK] of Apple.'
prediction = model.predict(model_version_id=response.id, model_input=input_text)
print(prediction)
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

* [AssemblyAI](https://www.assemblyai.com/)
* [AWS](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe.html) 
* Whisper ([OpenAI](https://openai.com/blog/whisper/))
* [GOOGLE](https://cloud.google.com/speech-to-text)
* [DEEPGRAM](https://deepgram.com/) 
* [REV](https://www.rev.com/services/auto-audio-transcription) 

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
