from pydantic import BaseModel


class Locators:
    inputs_form = 'form > div > input'
    captcha_frame = '[title="reCAPTCHA"]'
    captcha_checkbox = '.recaptcha-checkbox-border'
    captcha_audio = '.rc-button-audio'
    captcha_audio_link = '.rc-audiochallenge-tdownload-link'
    response_input = '#audio-response'
    submit_btn = '#recaptcha-verify-button'
    success_form = '.media.block-6.services.border.text-left'
    reject_cookie_btn = '.fc-button.fc-cta-consent.fc-primary-button'
