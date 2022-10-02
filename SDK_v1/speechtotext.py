class SpeechToText:
    SLASHML_BASE_URL = 'https://api.slashml.com/v1/speech-to-text'
    SLASHML_UPLOAD_URL = SLASHML_BASE_URL+'/upload'
    SLASHML_TRANSCRIPT_URL = SLASHML_BASE_URL+'/transcribe'
    SLASHML_TRANSCRIPT_STATUS_URL = lambda self,id: f"{SpeechToText.SLASHML_TRANSCRIPT_URL}/{id}"


    def upload_audio(self, file_location) :
        # here we can also add the service? assemblyai, aws, gcp?
        return    self.SLASHML_UPLOAD_URL #response.json()

    def transcribe(self,upload_url, model_params:dict()):
        # here we can add more model params
        transcript_request = {'audio_url': upload_url}
        #transcript_response = requests.post( self.SLASHML_TRANSCRIPT_URL, json=transcript_request)
        job_id=self.SLASHML_TRANSCRIPT_URL
        return job_id

    def status(self, job_id:str):
        #options={"status1"="queue","status2":"completed","status3":"deleted","text":"output_api_result"...}
        return self.SLASHML_TRANSCRIPT_STATUS_URL(job_id) 

