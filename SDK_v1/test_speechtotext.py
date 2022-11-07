#### unit testing
import pytest

import json
def test_upload():
    import speechtotext
    # given: there is a local file
    speect_to_text = speechtotext.SpeechToText()
    file_location="/Users/JJneid/Desktop/SlashMl/s2t_experiments/api_tests/test_audio_1.mp3"
    # when
    API_KEY="1bd15e1c161ff6d4db2ea1d661d7468b4fa61ca9"
    model_choice="assembly"
    result = speect_to_text.upload_audio(file_location,API_KEY, model_choice)
    print(result)
    # then
  #  assert result== 'https://api.slashml.com/v1/speech-to-text/upload'

def test_transcribe():
    import speechtotext
    # given: there is a local file
    speect_to_text = speechtotext.SpeechToText()
    upload_url="https://cdn.assemblyai.com/upload/f973cc7a-45f8-47b9-8ebc-20bd2f63a2bd"
    # when
    API_KEY="1bd15e1c161ff6d4db2ea1d661d7468b4fa61ca9"
    model_choice="assembly"
    result = speect_to_text.transcribe(upload_url,API_KEY, model_choice)

    print(result)

def test_status():
    import speechtotext
    # given: there is a local file
    speect_to_text = speechtotext.SpeechToText()
    upload_url="https://cdn.assemblyai.com/upload/28313e17-9a51-43cd-a29f-68dedd772f83"
    # when
    job_id= "r4ff9gd76c-530e-4e27-bed4-ce12b63b26b0"
    API_KEY="1bd15e1c161ff6d4db2ea1d661d7468b4fa61ca9"
    model_choice="assembly"
    result = speect_to_text.status(job_id,API_KEY, model_choice=model_choice)

    print(json.loads(result)["text"])

#test_transcribe()
#test_transcribe()
test_status()
# API_KEY="1bd15e1c161ff6d4db2ea1d661d7468b4fa61ca9"
# token="Token {api}".format(api=API_KEY) 
# print(token)

# headers = {'authorization': token}
# print(headers)