import csv
import os
import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

env1 = os.environ.get('infosecenvironmentvariable1')
env2 = os.environ.get('infosecenvironmentvariable2')

driver = webdriver.Chrome("chromedriver.exe", options=options)
webpage = ("https://securityiq.infosecinstitute.com/users/login?redirect=%2FDashboard%2Findex")

print("Initializing... ")
driver.get(webpage)

username_textbox = driver.find_element_by_name("email")
username_textbox.send_keys(env1)
password_textbox = driver.find_element_by_name("password")
password_textbox.send_keys(env2)


class DriverXPath:
    def __init__(self, path):
        self.path = driver.find_element_by_xpath(path).click()


DriverXPath("//*[@id='loginForm']/button")
DriverXPath("//*[@id='dashboard-container']/div[2]/div/div/button")
DriverXPath("//*[@id='page-header-nav']/li[3]/a")
time.sleep(1)

with open("evq_infosec_rm_learnerslist.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file)

    for line in csv_reader:
        element_to_hover_over = driver.find_element_by_xpath("//*[@id='campaigns']/div[2]/div/div/ul/span[1]/li")
        ActionChains(driver).move_to_element(element_to_hover_over).perform()
        time.sleep(1.5)

        DriverXPath("//*[@id='campaigns']/div[2]/div/div/ul/span[1]/li/div[1]/div[5]")
        time.sleep(1.5)

        DriverXPath("//*[@id='mega-learner-modal']/span/div[1]/a[1]")
        addsearchbox = driver.find_element_by_xpath(
            "//*[@id='mega-learner-modal']/span/div[2]/div[1]/div/div[2]/div[2]/input")
        emails = (line[0])
        addsearchbox.send_keys(emails)
        DriverXPath("//*[@id='mega-learner-modal']/span/div[2]/div[1]/div/div[2]/div[2]/div")
        DriverXPath("//*[@id='mega-learner-modal']/span/div[2]/div[1]/div/div[2]/div[1]/div/table/tbody/tr")
        DriverXPath("//*[@id='campaign-container']/div/span[3]/div/div/div[3]/a[1]")

print("Complete. ")
