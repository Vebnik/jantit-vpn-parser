from huggingsound import SpeechRecognitionModel
import logging, requests


class AiAudio:
    model: SpeechRecognitionModel

    def __init__(self) -> None:
        self.model = SpeechRecognitionModel('jonatasgrosman/wav2vec2-large-xlsr-53-english')

    def get_audio_from_url(self, url: str) -> None:
        try:
            results = requests.get(url, allow_redirects=True)

            with open('audio.mp3', 'wb') as file:
                file.write(results.content)

        except Exception as ex:
            logging.critical(ex)

    def transcriptions(self, target_url: str) -> list[dict]:
        try:
            self.get_audio_from_url(target_url)
            return self.model.transcribe(['audio.mp3'])
        except Exception as ex:
            logging.critical(ex)
