from slashml import ModelDeployment
import time

from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris

iris = load_iris()
data_x = iris['data']
data_y = iris['target']
my_model = RandomForestClassifier()
my_model.fit(data_x, data_y)

# Replace `API_KEY` with your SlasML API token.
client = ModelDeployment(api_key=None)

# deploy model
response = client.deploy(model_name='sk-learn-model', model=my_model)

# check status
status = client.status(model_version_id=response.id)

# submit prediction
model_input = [[0, 0, 0, 0]]
prediction = client.predict(model_version_id=response.id, model_input=model_input)
print(prediction)
