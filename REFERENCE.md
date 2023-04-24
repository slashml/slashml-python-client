# SpeechToText

This class provides functionality for uploading audio files and transcribing them into text using a speech-to-text service provider.

## SpeechToText.ServiceProvider

An enumeration of available speech-to-text service providers.

### SpeechToText.ServiceProvider.choices()

Returns a list of available service provider choices.

## SpeechToText.upload_audio(file_location: str, header=None) -> Dict[str, Any]

Uploads an audio file to the speech-to-text service provider.

### Parameters

- `file_location` (`str`): The location of the audio file to upload.
- `header` (`Any`): Optional header information.

### Returns

- `Dict[str, Any]`: The response from the speech-to-text service provider.

## SpeechToText.transcribe(upload_url: str, service_provider: ServiceProvider, header=None) -> Dict[str, Any]

Transcribes an uploaded audio file into text using a specified service provider.

### Parameters

- `upload_url` (`str`): The URL of the uploaded audio file.
- `service_provider` (`SpeechToText.ServiceProvider`): The service provider to use for transcription.
- `header` (`Any`): Optional header information.

### Returns

- `Dict[str, Any]`: The response from the speech-to-text service provider.

## SpeechToText.status(job_id: str, service_provider: ServiceProvider, header=None) -> Dict[str, Any]

Retrieves the status of a transcription job using a specified service provider.

### Parameters

- `job_id` (`str`): The ID of the transcription job.
- `service_provider` (`SpeechToText.ServiceProvider`): The service provider used for the transcription job.
- `header` (`Any`): Optional header information.

### Returns

- `Dict[str, Any]`: The response from the speech-to-text service provider.


# Summarization

This class provides functionality for summarizing text using a summarization service provider.

## Summarization.ServiceProvider

An enumeration of available summarization service providers.

### Summarization.ServiceProvider.choices()

Returns a list of available service provider choices.

## Summarization.summarize(text: str, service_provider: ServiceProvider, header=None) -> Dict[str, Any]

Summarizes a block of text using a specified service provider.

### Parameters

- `text` (`str`): The text to summarize.
- `service_provider` (`Summarization.ServiceProvider`): The service provider to use for summarization.
- `header` (`Any`): Optional header information.

### Returns

- `Dict[str, Any]`: The response from the summarization service provider.


# TextToSpeech

This class provides functionality for converting text to audio using a text-to-speech service provider.

## TextToSpeech.ServiceProvider

An enumeration of available text-to-speech service providers.

### TextToSpeech.ServiceProvider.choices()

Returns a list of available service provider choices.

## TextToSpeech.synthesize(text: str, service_provider: ServiceProvider, voice=None, speed=None, header=None) -> bytes

Synthesizes text into audio using a specified service provider.

### Parameters

- `text` (`str`): The text to synthesize.
- `service_provider` (`TextToSpeech.ServiceProvider`): The service provider to use for text-to-speech conversion.
- `voice` (`Any`): Optional voice information.
- `speed` (`Any`): Optional speed information.
- `header` (`Any`): Optional header information.

### Returns

- `bytes`: The audio data in bytes format.

## TextToSpeech.save_audio(text: str, output_path: str, service_provider: ServiceProvider, voice=None, speed=None, header=None) -> None

Synthesizes text into audio using a specified service provider and saves it to a file.

### Parameters

- `text` (`str`): The text to synthesize.
- `output_path` (`str`): The path to save the output audio file.
- `service_provider` (`TextToSpeech.ServiceProvider`): The service provider to use for text-to-speech conversion.
- `voice` (`Any`): Optional voice information.
- `speed` (`Any`): Optional speed information.
- `header` (`Any`): Optional header information.

### Returns

- `None`

## TextToSpeech.list_voices(service_provider: ServiceProvider, header=None) -> Dict[str, Any]

Returns a list of available voices for a specified service provider.

### Parameters

- `service_provider` (`TextToSpeech.ServiceProvider`): The service provider to use for voice listing.
- `header` (`Any`): Optional header information.

### Returns

- `Dict[str, Any]`: The response from the text-to-speech service provider containing the list of available voices.
