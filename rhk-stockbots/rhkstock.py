import os
import time

# Windows 10 Version 1.1

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome("chromedriver_v96.exe", options=options)
# xm-18 real webpage = ("https://www.monkeyedge.com/Hinderer-Knives-XM-18-3-5-Inch-Spanto-3V-MEFP-p/rhk1843.htm")

#handle screws test
webpage = ("https://www.rickhindererknives.com/product/eklipse-3-5-od-green-micarta-textured-scale/")

print("initializing")
driver.get(webpage)
time.sleep(1)

driver.find_element_by_xpath("//*[@id='page-content']/section[2]/div/div[1]/div/section/div/div/div/div/div/div[1]/div[2]/div/div/div[4]/form/button").click()
time.sleep(1)

driver.find_element_by_xpath("//*[@id='woocommerce_widget_cart-2']/div/p[2]/a[2]").click()
time.sleep(1)

driver.find_element_by_xpath("//*[@id='page-content']/div/section/div/div/div/div/div/div/div[2]/div/a").click()
time.sleep(1)

usernameinput = driver.find_element_by_xpath("//*[@id='username']")
usernameinput.send_keys("narisma.isaiah@gmail.com")

passwordinput = driver.find_element_by_xpath("//*[@id='password']")
passwordinput.send_keys("null")
time.sleep(1)

driver.find_element_by_xpath("//*[@id='page-content']/div/section/div/div/div/div/div/div/form[1]/p[4]/button").click()
time.sleep(1)

driver.find_element_by_xpath("//*[@id='payment']/ul/li[2]/label").click()
driver.find_element_by_xpath("//*[@id='terms']").click()
driver.find_element_by_xpath("//*[@id='place_order']").click()

time.sleep(1)

print("Item is in Stock!")

webpage2 = ("https://accounts.google.com/signin/v2/identifier?service=mail&passive=true&rm=false&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
driver.get(webpage2)


class DriverXPath:
    def __init__(self, path):
        self.path = driver.find_element_by_xpath(path).click()

testgmail_name = driver.find_element_by_xpath("//*[@id='identifierId']")
testgmail_name.send_keys("inarismatest@gmail.com")
DriverXPath("//*[@id='identifierNext']/div/button")
time.sleep(2)
testgmail_pass = driver.find_element_by_xpath("//*[@id='password']/div[1]/div/div[1]/input")
testgmail_pass.send_keys("null")
DriverXPath("//*[@id='passwordNext']/div/button")
time.sleep(7)
DriverXPath("/html/body/div[7]/div[3]/div/div[2]/div[1]/div[1]/div[1]/div/div/div/div[1]/div/div")
#time.sleep(7)

#DriverXPath("/html/body/div[7]/div[3]/div/div[2]/div[1]/div[1]/div[1]/div/div/div/div[1]/div/div")
time.sleep(3)
to_email = driver.find_element_by_xpath("//*[@id=':8d']")
to_email.send_keys("narisma.isaiah@gmail.com")
email_subject = driver.find_element_by_xpath("//*[@id=':7v']")
email_subject.send_keys("RHK 'ITEM' IS IN YOUR CART")
email_body = driver.find_element_by_xpath("//*[@id=':91']")
email_body.send_keys("https://www.rickhindererknives.com/cart/")

DriverXPath("//*[@id=':7l']")
print("In Stock Alert Email Sent")

"""
ccnumber = driver.find_element_by_xpath("//*[@id='wc-elavon-converge-credit-card-account-number']")
driver.find_element_by_xpath("//*[@id='wc-elavon-converge-credit-card-account-number']").click()
ccnumber.send_keys("123456789")
time.sleep(0.5)

ccdate = driver.find_element_by_xpath("//*[@id='wc-elavon-converge-credit-card-expiry']")
driver.find_element_by_xpath("//*[@id='wc-elavon-converge-credit-card-expiry']").click()
ccdate.send_keys("1125")
time.sleep(0.5)

cccsc = driver.find_element_by_xpath("//*[@id='wc-elavon-converge-credit-card-csc']")
driver.find_element_by_xpath("//*[@id='wc-elavon-converge-credit-card-csc']").click()
cccsc.send_keys("123")
"""


time.sleep(1)
























































'''
try:
    time.sleep(.5)
    # driver.find_element_by_xpath("//*[@id='v65-checkout-guest-cell']/input").click()
    print("Item is in Stock!")

    webpage2 = ("https://accounts.google.com/signin/v2/identifier?service=mail&passive=true&rm=false&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
    driver.get(webpage2)


    class DriverXPath:
        def __init__(self, path):
            self.path = driver.find_element_by_xpath(path).click()

    testgmail_name = driver.find_element_by_xpath("//*[@id='identifierId']")
    testgmail_name.send_keys("inarismatest@gmail.com")
    DriverXPath("//*[@id='identifierNext']/div/button")
    time.sleep(2)
    testgmail_pass = driver.find_element_by_xpath("//*[@id='password']/div[1]/div/div[1]/input")
    testgmail_pass.send_keys("intest123")
    DriverXPath("//*[@id='passwordNext']/div/button")
    time.sleep(7)
    DriverXPath("/html/body/div[7]/div[3]/div/div[2]/div[1]/div[1]/div[1]/div/div/div/div[1]/div/div")
    #time.sleep(7)

    #DriverXPath("/html/body/div[7]/div[3]/div/div[2]/div[1]/div[1]/div[1]/div/div/div/div[1]/div/div")
    time.sleep(3)
    to_email = driver.find_element_by_xpath("/html/body/div[20]/div/div/div/div[1]/div[3]/div[1]/div[1]/div/div/div/div[3]/div/div/div[4]/table/tbody/tr/td[2]/form/div[2]")
    to_email.send_keys("narisma.isaiah@gmail.com")
    email_subject = driver.find_element_by_xpath("/html/body/div[20]/div/div/div/div[1]/div[3]/div[1]/div[1]/div/div/div/div[3]/div/div/div[4]/table/tbody/tr/td[2]/form/div[3]/div/input")
    email_subject.send_keys("Monkey Edge Frag Pattern XM-18 is NOW AVAILABLE")
    email_body = driver.find_element_by_xpath("/html/body/div[20]/div/div/div/div[1]/div[3]/div[1]/div[1]/div/div/div/div[3]/div/div/div[4]/table/tbody/tr/td[2]/table/tbody/tr[1]/td/div/div[1]/div[2]/div[1]/div/table/tbody/tr/td[2]/div[2]/div")
    email_body.send_keys("https://www.monkeyedge.com/Hinderer-Knives-XM-18-3-5-Inch-Spanto-3V-MEFP-p/rhk1843.htm")

    DriverXPath("//*[@id=':8l']")
    print("In Stock Alert Email Sent")



except NoSuchElementException:
    print("Item is currently out of stock")
    driver.refresh()


"""
    
    username_textbox = driver.find_element_by_name("email")
    username_textbox.send_keys("narisma.isaiah@gmail.com")
    password_textbox = driver.find_element_by_name("password")
    password_textbox.send_keys("!StockAlert")

    class DriverXPath:
        def __init__(self, path):
            self.path = driver.find_element_by_xpath(path).click()

    DriverXPath("//*[@id='v65-checkout-login-button-cell']/input[1]") #Login
    selectaddy = Select(driver.find_element_by_xpath("//*[@id='v65-onepage-saved-billing-table']/tbody/tr/td/select"))
    selectaddy.select_by_visible_text('1665 Seattle Slew Way, CA')
    DriverXPath("//*[@id='v65-onepage-CopyBillingToShippingLink']") #Copy Billing
    DriverXPath("//*[@id='ShipResidentialY']") #Residential
    time.sleep(2)
    selectshipping = Select(driver.find_element_by_xpath("//*[@id='DisplayShippingSpeedChoicesTD']/select"))
    time.sleep(2)
    # selectshipping.select_by_visible_text('USPS Priority Mail (NO Insurance See Policies) $10.31')
    selectshipping.select_by_visible_text('FedEx 2Day® (Mon-Fri) $23.15')
    print("selected shipping")
    time.sleep(3)

    DriverXPath("//*[@id='PayPalExpress']") #paypal
    time.sleep(5)
    DriverXPath("//*[@id='buttons-container']/div/div[1]/div")
    time.sleep(2)
    paypallogin = driver.find_element_by_name("login_email")
    paypallogin.send_keys("info@inmediaworks.com")
    DriverXPath("//*[@id='btnNext']")
    DriverXPath("//*[@id='content']/div/div/form/p/a")
    paypalpassword = driver.find_element_by_name("login_password")
    paypalpassword.send_keys("NULL")
    DriverXPath("//*[@id='payment-submit-btn']")
    print("Ready to Place the Order")
    
"""

"""
    DriverXPath("//*[@id='CreditCard']") #creditcard
    time.sleep(3)
    cardholdernametextbox = driver.find_element_by_xpath("//*[@id='CardHoldersName']")
    cardholdernametextbox.send_keys("Isaiah Narisma")
    print("entered card name")
    creditcardnumber_textbox = driver.find_element_by_xpath("//*[@id='CreditCardNumber']")
    creditcardnumber_textbox.send_keys("1234")
    print("entered card number")
    time.sleep(2)
    selectexpirationmonth = Select(driver.find_element_by_xpath("//*[@id='CC_ExpDate_Month']"))
    time.sleep(2)
    selectexpirationmonth.select_by_visible_text('11 - November')
    time.sleep(2)
    selectexpirationyear = Select(driver.find_element_by_xpath("//*[@id='CC_ExpDate_Year']"))
    time.sleep(2)
    selectexpirationyear.select_by_visible_text('2025')
    time.sleep(2)
    securitycode = driver.find_element_by_name("CVV2")
    securitycode.send_keys('123')
"""
'''
