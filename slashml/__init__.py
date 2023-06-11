"""SlashML"""

from slashml.text_summarization import TextSummarization  # noqa: F401,E402
from slashml.speech_to_text import SpeechToText  # noqa: F401,E402
from slashml.text_to_speech import TextToSpeech  # noqa: F401,E402
from slashml.model_deployment import ModelDeployment  # noqa: F401,E402

__all__ = ["TextSummarization", "SpeechToText", "TextToSpeech"]