import logging

from src.selenium.app import App
from src.jantit_page.page import JantitPage
from src.ai_audio.app import AiAudio


def main() -> None:
    logging.basicConfig(level=logging.INFO)
    target_url = 'https://www.vpnjantit.com/create-free-account?type=OpenVPN&server=gr1#create'

    ai_app = AiAudio()
    selenium_app = App()
    jantit_page = JantitPage(selenium_app, ai_app)

    selenium_app.open(target_url)

    jantit_page.reject_cookie()
    jantit_page.enter_creds()
    jantit_page.valid_captcha()
    jantit_page.send_form()
    jantit_page.download_zip()

    selenium_app.exit(10)


if __name__ == '__main__':
    main()
