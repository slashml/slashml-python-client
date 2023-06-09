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
