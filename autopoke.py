#!/bin/env python
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
from time import sleep
from getpass import getpass
from random import randint


if __name__ == '__main__':
    driver = webdriver.phantomjs.webdriver.WebDriver()
    driver.get('https://facebook.com')
    driver.find_element_by_id('email').send_keys(input('Email: '))
    driver.find_element_by_id('pass').send_keys(getpass())
    driver.find_element_by_id('loginbutton').click()
    driver.get('https://facebook.com/pokes/')
    assert "Forgot password?" not in driver.page_source

    c = 0
    e = 0
    while True:
        try:
            for i in driver.find_elements_by_link_text("Poke Back"):
                sleep(randint(3,300))
                i.click()
                c += 1
                print("Clicked so far: " + str(c))
        except StaleElementReferenceException:
            e += 1
            if e == 10:
                print("Found exception, reloading page")
                driver.get('https://facebook.com/pokes/')
                e = 0
            else:
                print("Found exception, doing nothing")

        sleep(1)
