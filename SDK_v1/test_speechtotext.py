#### unit testing
import pytest


def test_upload():
    import speechtotext
    # given: there is a local file
    speect_to_text = speechtotext.SpeechToText()
    file_location="local_path"
    # when
    result = speect_to_text.upload_audio(file_location)

    # then
    assert result== 'https://api.slashml.com/v1/speech-to-text/upload'

def test_transcribe():
    import speechtotext
    # given: there is a local file
    speect_to_text = speechtotext.SpeechToText()
    upload_url="local_path"
    # when
    result = speect_to_text.transcribe(upload_url,dict())

    # then
    assert result== 'https://api.slashml.com/v1/speech-to-text/transcribe'


def test_status():
    import speechtotext
    # given: there is a local file
    speect_to_text = speechtotext.SpeechToText()
    # when
    job_id = '123'
    result = speect_to_text.status(job_id)

    # then
    assert result== 'https://api.slashml.com/v1/speech-to-text/transcribe/{}'.format(job_id)


# def test_status():
#     assert 
