from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    btnCheckout = (By.XPATH, "//button[@class='btn btn-success']")
    fieldCountry = (By.ID, "country")
    selectCountry = (By.LINK_TEXT, "India")
    selectCheckBox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    btnPurchase = (By.CSS_SELECTOR, "input[type='submit']")
    messageAlert = (By.CLASS_NAME, "alert-success")

    def btnCheckoutMethod(self):
        return self.driver.find_element(*ConfirmPage.btnCheckout)

    def countryMethod(self):
        return self.driver.find_element(*ConfirmPage.fieldCountry)

    def selectCountryMethod(self):
        return self.driver.find_element(*ConfirmPage.selectCountry)

    def selectCheckBoxMethod(self):
        return self.driver.find_element(*ConfirmPage.selectCheckBox)

    def btnPurchaseMethod(self):
        return self.driver.find_element(*ConfirmPage.btnPurchase)

    def messageAlertMethod(self):
        return self.driver.find_element(*ConfirmPage.messageAlert)