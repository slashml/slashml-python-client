
# import the model
from slashml import SpeechToText
from utils import download_youtube_file

# Replace `API_KEY` with your SlasML API token. This example still runs without
# the API token but usage will be limited
API_KEY = None

def transcribe_youtube_file(*, youtube_url:str):

    # parse the id from the youtube url
    youtube_id = youtube_url.split('/')[-1]

    # this downloads the file at data/{youtube_id}.mp4 
    download_youtube_file(youtube_url = youtube_url, output_folder='data')
    
    downloaded_file_path= f'data/{youtube_id}.mp4'

    # We recommend using AWS for video transcription
    service_provider = SpeechToText.ServiceProvider.AWS

    model = SpeechToText(api_key=API_KEY)

    # Upload audio
    uploaded_file = model.upload_audio(downloaded_file_path)
    print(f"file uploaded: {uploaded_file}")

    response = model.execute(
        upload_url=uploaded_file["upload_url"], service_provider=service_provider
    )

    return response.transcription_data.transcription

def transcribe_multiple_youtube_videos(*, youtube_urls:list):
    return list(map(transcribe_youtube_file, youtube_urls))

if __name__=='__main__':
    youtube_url = 'https://youtu.be/5-TgqZ8nado'
    print(transcribe_youtube_file(youtube_url=youtube_url))
