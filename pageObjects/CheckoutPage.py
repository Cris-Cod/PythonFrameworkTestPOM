from selenium.webdriver.common.by import By
from pageObjects.ConfirmPage import ConfirmPage


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    products = (By.XPATH, "//div[@class='card h-100']")
    buttonAdd = (By.XPATH, "div[2]/button")
    productName = (By.XPATH, "div/h4/a")
    btnCheckout = (By.CSS_SELECTOR, "a[class*='btn-primary']")

    def productsTitle(self):
        return self.driver.find_elements(*CheckoutPage.products)

    def getProductName(self, product):
        return product.find_element(*CheckoutPage.productName)
    def addButton(self, product):
        return product.find_element(*CheckoutPage.buttonAdd)

    def checkoutBtn(self):
        self.driver.find_element(*CheckoutPage.btnCheckout).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage

