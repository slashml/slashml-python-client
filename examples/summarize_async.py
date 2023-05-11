from slashml import TextSummarization
import time

def summarize(text, service_provider, api_key):
    # Initialize model
    model = TextSummarization(api_key=api_key)

    # Submit request
    job = model.summarize(text=text, service_provider=service_provider)

    assert job.status != "ERROR", f"{job}"
    print(f"Job ID: {job.id}")

    # Check job status
    response = model.status(job.id, service_provider=service_provider)

    # Keep checking job status until the task is complete
    while response.status == "PENDING":
        print(f"Response = {response}. Retrying in 30 seconds")
        time.sleep(30)
        response = model.status(job.id, service_provider=service_provider)

    return response


# Replace `API_KEY` with your SlasML API token. This example still runs without
# the API token but usage will be limited
API_KEY = "b503d137d229fdd4085f59e9ea06ac95d2706182"
service_provider = TextSummarization.ServiceProvider.OPENAI
input_text = """A good writer doesn't just think, and then write down what he thought, as a sort of transcript. A good writer will almost always discover new things in the process of writing. And there is, as far as I know, no substitute for this kind of discovery. Talking about your ideas with other people is a good way to develop them. But even after doing this, you'll find you still discover new things when you sit down to write. There is a kind of thinking that can only be done by writing."""

# Find all the service providers that we support by running the choices() method
print(f"Available providers: {TextSummarization.ServiceProvider.choices()}")
print(f"Selected provider: {service_provider}")

response = summarize(text=input_text, service_provider=service_provider, api_key=API_KEY)
print(f"{response}\n\nSummary = {response.summarization_data}")
