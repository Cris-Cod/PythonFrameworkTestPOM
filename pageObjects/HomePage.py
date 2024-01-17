from selenium.webdriver.common.by import By
from pageObjects.CheckoutPage import CheckoutPage

class HomePage:

    def __init__(self, driver):
        self.driver = driver

    name = (By.CSS_SELECTOR,"input[name='name']")
    email = (By.CSS_SELECTOR, "input[name='email']")
    password = (By.ID, "exampleInputPassword1")
    checkout = (By.ID, "exampleCheck1")
    gender = (By.ID, "exampleFormControlSelect1")
    radio = (By.ID, "inlineRadio1")
    botton = (By.CSS_SELECTOR, "input[type='submit']")
    text = (By.CSS_SELECTOR, ".alert-success")
    shop = (By.CSS_SELECTOR, "a[href*='shop']")


    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getPassword(self):
        return self.driver.find_element(*HomePage.password)

    def getCheckout(self):
        return self.driver.find_element(*HomePage.checkout)

    def getGender(self):
        return self.driver.find_element(*HomePage.gender)

    def getRadio(self):
        return self.driver.find_element(*HomePage.radio)

    def getBotton(self):
        return self.driver.find_element(*HomePage.botton)

    def getText(self):
        return self.driver.find_element(*HomePage.text)

    def shopItem(self):
        self.driver.find_element(*HomePage.shop).click()
        checokoutPage = CheckoutPage(self.driver)
        return checokoutPage
        #driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()