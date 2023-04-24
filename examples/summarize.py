
from slashml import Summarization
import time

# Initialize your model
model = Summarization("e33f38aebe7120930fbd8488ab738b321b647840")
# model = Summarization()
service_provider = model.ServiceProvider.OPENAI

in_text = '''A good writer doesn't just think, and then write down what he thought, as a sort of transcript. A good writer will almost always discover new things in the process of writing. And there is, as far as I know, no substitute for this kind of discovery. Talking about your ideas with other people is a good way to develop them. But even after doing this, you'll find you still discover new things when you sit down to write. There is a kind of thinking that can only be done by writing.'''

# # choose a service provider and transcribe
job = model.summarize(
    text=in_text,
    service_provider=service_provider
    )

assert job.status != 'ERROR', f'{job}'

print('transcription job id', job.id)

# check the status
response = model.status(job.id, service_provider = service_provider)

while response.status != 'COMPLETED':
    time.sleep(30)
    response = model.status(job['id'], service_provider = service_provider)
    print(f'response got', response , 'trying again')

print(response)