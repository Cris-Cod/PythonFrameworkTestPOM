from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.ConfirmPage import ConfirmPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):

        log = self.getLogger()
        homePage = HomePage(self.driver)
        checokoutPage = homePage.shopItem()
        log.info(checokoutPage)
        log.info("getting all tje card titles")
        #checokoutPage = CheckoutPage(self.driver)
        products = checokoutPage.productsTitle()

        for product in products:
            textProduct = checokoutPage.getProductName(product).text
            log.info(textProduct)
            if textProduct == "Blackberry":
                checokoutPage.addButton(product).click()

        confirmPage = checokoutPage.checkoutBtn()

        #confirmPage = ConfirmPage(self.driver)
        confirmPage.btnCheckoutMethod().click()
        log.info("Entering country is Ind")
        confirmPage.countryMethod().send_keys("ind")
        self.verifyLinkPresence("India")
        confirmPage.selectCountryMethod().click()
        confirmPage.selectCheckBoxMethod().click()
        confirmPage.btnPurchaseMethod().click()
        succes_test = confirmPage.messageAlertMethod().text
        log.info(succes_test)
        log.info("Text recive the application")

        assert "Success! Thank you!" in succes_test
