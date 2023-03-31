from src.selenium.app import App
from src.ai_audio.app import AiAudio
from src.jantit_page.models import Locators

from faker import Faker
import logging, time


class JantitPage:
    app: App
    ai_app: AiAudio
    fake: Faker
    locale: str = 'en_US'

    def __init__(self, app: App, ai_app: AiAudio) -> None:
        self.fake = Faker(self.locale)
        self.app = app
        self.ai_app = ai_app

    def enter_creds(self) -> None:
        logging.info('Input creds')
        time.sleep(10)

        name = self.fake.name().split(' ')[0]
        password = '12345678'

        inputs = self.app.query_selector_all(Locators.inputs_form)

        time.sleep(2)
        for key in name: time.sleep(0.3); inputs[0].send_keys(key)
        time.sleep(2)
        for key in password: time.sleep(0.3); inputs[1].send_keys(key)
        time.sleep(2)

    def valid_captcha(self) -> None:
        logging.info('Valid captcha')

        frame = self.app.query_selector(Locators.captcha_frame)

        self.app.switch_to_frame(frame)

        captcha_box = self.app.query_selector(Locators.captcha_checkbox)
        captcha_box.click()
        time.sleep(2)

        self.app.switch_to_default()

        frames = self.app.query_selector_all('iframe')
        captcha_frames = [el for el in frames if 'CAPTCHA' in el.get_attribute('title')]

        self.app.switch_to_frame(captcha_frames[1])

        captcha_audio = self.app.query_selector(Locators.captcha_audio)
        captcha_audio.click()
        time.sleep(2)

        captcha_audio_link = self.app.query_selector(Locators.captcha_audio_link)
        link = captcha_audio_link.get_attribute('href')
        time.sleep(2)

        logging.info('Send to transcription')
        results = self.ai_app.transcriptions(link)[0].get('transcription')

        response_input = self.app.query_selector(Locators.response_input)
        response_input.send_keys(results)
        time.sleep(2)

        submit_btn = self.app.query_selector(Locators.submit_btn)
        submit_btn.click()
        time.sleep(3)

        self.app.switch_to_default()

        time.sleep(4)

    def send_form(self) -> None:
        logging.info('Send form')

        inputs = self.app.query_selector_all(Locators.inputs_form)
        inputs[2].click()

        time.sleep(10)

    def download_zip(self) -> None:
        logging.info('Download zip')

        success_form = self.app.query_selector_all(Locators.success_form)[1]
        text_data = success_form.text; print(text_data)

        with open('data.txt', 'w') as file:
            file.write(text_data)

    def reject_cookie(self) -> None:
        logging.info('Reject cookie')
        time.sleep(5)

        reject_btn = self.app.query_selector(Locators.reject_cookie_btn)
        reject_btn.click()

        time.sleep(3)
