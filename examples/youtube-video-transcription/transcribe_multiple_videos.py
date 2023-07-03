from transcribe_youtube_video import transcribe_youtube_file

def transcribe_multiple_youtube_videos(*, youtube_urls:list):
    return list(map(transcribe_youtube_file, youtube_urls))


if __name__=="__main__":
    youtube_urls = ['https://youtu.be/5-TgqZ8nado','https://youtu.be/5-TgqZ8nado']

    list_of_transcriptions = transcribe_multiple_youtube_videos(youtube_urls=youtube_url)
    
    from pprint import pprint as pp
    pp(list_of_transcriptions)
