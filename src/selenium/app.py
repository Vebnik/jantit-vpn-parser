from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

import logging
import time
from faker import Faker


class App:
    driver: webdriver.Chrome
    options: webdriver.ChromeOptions
    fake: Faker

    def __init__(self) -> None:
        try:
            self.driver = webdriver.Chrome()
            self.options = webdriver.ChromeOptions()
            self.fake = Faker()

            self.options.add_argument(f'user-agent={self.fake.chrome()}')

            self.driver = webdriver.Chrome(chrome_options=self.options)
        except Exception as ex:
            logging.critical(ex)

    def open(self, url: str) -> None:
        self.driver.get(url)

    def exit(self, delay: int) -> None:
        time.sleep(delay)
        self.driver.quit()

    def query_selector_all(self, css_selector: str):
        try:
            return self.driver.find_elements(By.CSS_SELECTOR, css_selector)
        except Exception as ex:
            logging.critical(ex)

    def query_selector(self, css_selector: str):
        try:
            return self.driver.find_element(By.CSS_SELECTOR, css_selector)
        except Exception as ex:
            logging.critical(f'{ex}\n{css_selector}')

    def find_by_name(self, name_selector: str) -> WebElement:
        try:
            return self.driver.find_element(By.NAME, name_selector)
        except Exception as ex:
            logging.critical(f'{ex}\n{name_selector}')

    def switch_to_frame(self, frame: WebElement) -> None:
        try:
            self.driver.switch_to.frame(frame)
        except Exception as ex:
            logging.critical(ex)

    def switch_to_default(self) -> None:
        try:
            self.driver.switch_to.default_content()
        except Exception as ex:
            logging.critical(ex)
