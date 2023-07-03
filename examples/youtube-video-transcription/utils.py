import youtube_dl

def download_youtube_file(*, youtube_url:str, output_folder:str):
    ydl = youtube_dl.YoutubeDL({'outtmpl': output_folder+'/%(id)s.%(ext)s'})

    with ydl:
        ydl.download([youtube_url])
    
if __name__=='__main__':
    download_youtube_file(youtube_url='https://youtu.be/5-TgqZ8nado', output_folder='data')