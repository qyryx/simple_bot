import random
import names
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class Person:
    def __init__(self):
        self.first = names.get_first_name()
        self.last = names.get_last_name()
        self.email = self.first.lower() + '.' + self.last.lower() + '@gmail.com'
        self.phone = get_number()

    def get_first(self):
        return self.first

    def get_last(self):
        return self.last

    def get_email(self):
        return self.email

    def get_phone(self):
        return self.phone


def launch_browser():
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    browser.maximize_window()
    return browser


driver = launch_browser()


def wait_for_element(path, by_what, value, to_do):
    is_loaded = False
    count = 0
    while not is_loaded and count < 300:
        try:
            element = driver.find_element(*(by_what, path))
            do_action(element, to_do, value)
            is_loaded = True
        except:
            count += 1
            pass
    if count == 300:
        raise Exception('Timed out')


def do_action(element, to_do, value):
    match to_do:
        case "click":
            element.click()
        case "send":
            element.send_keys(value)
        case "clear":
            element.clear()
        case "select":
            Select(element).select_by_value(value)


def get_number():
    number = '+4219'
    for i in range(8):
        number += str(random.randint(0, 9))
    return number


def main():
    while 1:
        time.sleep(3)
        driver.get('https://appt.link/speai/junak')
        person = Person()

        wait_for_element('//*[@id="id-0"]', By.XPATH, None, "click")

        try:
            wait_for_element("firstName", By.NAME, person.get_first(), "send")
        except:
            wait_for_element('//*[@id="id-0"]', By.XPATH, None, "click")
            wait_for_element("firstName", By.NAME, person.get_first(), "send")

        wait_for_element("lastName", By.NAME, person.get_last(), "send")
        wait_for_element("email", By.NAME, person.get_email(), "send")
        wait_for_element("mpvju", By.NAME, person.get_phone(), "send")

        wait_for_element('//*[@id="content-container"]/div/div/div[2]/div/form/div[2]/div[2]/button', By.XPATH, None,
                         "click")


main()
