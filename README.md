# SlashML Python client
[SlashML](https://www.slashml.com/)

Do you want to use state-of-the-art machine learning models with few clicks, without going through a lot of documentation and through many service providers? At SlashML we guarantee the best ML model for your application through our API. We do the benchmarking for you and offer you the best results all in one API call.

Supported services so far: speech-to-text, Summarization, text-to-speech

# Installation guide

To install this packaged, clone this repository by running `git@github.com:slashml/slashml-python-client.git` in the terminal. This command will clone this repo. Then `cd slashml-python-client` to get into the cloned repository. Then install the repo as a pip package by running `pip install -e .`.

# Quickstart tutorial 

**Note** : make sure slashml is installed as a pip package. 

In this tutorial, we use slashml sdk to call speechtotext followed by summarization of the output of speechtotext. All the user needs is an audio URL that can be used directly as ```upload_url```  or a local path to the audio file, preferrably ```.mp3```. The user can also set their ```SLASHML_API_KEY``` and not be blocked by certain throttling limits.

Benchmarking can help you decide which ```service provider``` is the best for you. 

* For speech-to-text: "assembly", "aws", "whisper"
* For summarization: "hugging-face", "openai"

```
from slashml import SpeechToText, Summarization
import time

# Optional: set environment path
import os
os.environ["SLASHML_API_KEY"] = "SlashML_token"

# Initialize your model
model = SpeechToText()

# choose your service provider: "assembly", "aws", "whisper"
service_provider = model.ServiceProvider.WHISPER

# Optional local file to upload, if not an accessible url
file_location = "audio_local_path.mp3"
# If your audio files aren't accessible via a URL already, you can upload your audio file using this API
uploaded_file = model.upload_audio(LOCAL_FILE_PATH)

# # choose a service provider and transcribe
job = model.transcribe(
    uploaded_file['upload_url'], 
    service_provider=service_provider
    )

assert job.status != 'ERROR', f'{job}'

print('transcription job id', job.id)

# check the status
response = model.status(job.id, service_provider=service_provider)

while response.status != 'COMPLETED':
    print(f'response got', response , 'trying again')
    time.sleep(30)
    response = model.status(job.id, service_provider = service_provider)

text_to_summarize = response.transcription_data.transcription

model = Summarization()

# choose your servie_provider: "hugging-face", "openai"
service_provicer = summarizer.ServiceProvider.OPENAI

job = model.summarize(
        text=text_to_summarize, 
        service_provider=service_provider
        )

assert job.status != 'ERROR', f'{job}'

print('summarization job id', job.id)

# check the status
response = model.status(job.id, service_provider=service_provider)

while response.status != 'COMPLETED':
    print(f'response got', response , 'trying again')
    time.sleep(30)
    response = model.status(job.id, service_provider = service_provider)

print(response)
```


# Introduction
## Overview 
This is a Python client (SDK) for SlashML. It allows the user to use the endpoints available and active in [SlashML-Dashboard](https://www.slashml.com/dashboard). 
The APIsls
 can be used together in the same code as long the input/output structure is compatible. For example, if the user wants to transcribe an audio file and get a summary, they can call speechtotext followed by summarization (speech>text>summary), see [Tutorial](##Quickstart-tutorial).

State-of-the-art AI models from several service providers are available. At SlashML, we also do the benchmarking on these models for the user. This will give them an idea of the best service provider for their application. For the full list of the available models through SlashML, go to section Available service providers. Click [here](##Availlable-service-providers)

## Set up and usage
There is a daily limit (throttling) on the number of calls the user performs. The code runs without specifying SlashML token (API key). The throttling kicks in and prevents new jobs after exceeding 10 calls per minute. 

If the user intends on using the service more frequently, it is recommended to generate an token or API key from [SlashML-Dashboard](https://www.slashml.com/dashboard). This way, the throttling limit will increase.

Sign up and Grab your SlashML token from [SlashML-Dashboard](https://www.slashml.com/dashboard) > settings > new api key and authenticate by setting it as an environment variable (or when you initialize the service, see Quickstart tutorial):

* For MAC OS users, in your terminal:
```
export SLASHML_API_KEY=[token]
```
* For Windows users, in your terminal:
```
set SLASHML_API_KEY=[token]
```

or including it in your python code as follows:
```

import os
os.environ["SLASHML_API_KEY"] = "slashml_api_token"

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

For use cases, look at the `examples` folder. For detail documentation, checkout the (REFERENCE.md)[https://github.com/slashml/slashml-python-client/blob/main/REFERENCE.md]
