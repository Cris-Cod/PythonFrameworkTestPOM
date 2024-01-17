import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmition(self, getData):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        homePage.getName().send_keys(getData["firstname"])
        homePage.getEmail().send_keys(getData["email"])
        homePage.getPassword().send_keys(getData["password"])
        homePage.getCheckout().click()
        self.selectOptionByText(homePage.getGender(),getData["gender"])
        homePage.getRadio().click()
        homePage.getBotton().click()

        message = homePage.getText().text
        assert "Success!" in message
        self.driver.refresh()


    @pytest.fixture(params= HomePageData.getTestData("Testcase2"))
    def getData(self,request):
        return request.param


