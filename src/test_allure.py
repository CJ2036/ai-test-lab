from venv import logger

import allure
import time
import logging

logger = logging.getLogger(__name__)

@allure.title("路由器管理页面测试")
@allure.description("测试路由器管理页面的登录功能")
@allure.tag("NewUI", "Essentials", "Authentication")
@allure.severity(allure.severity_level.NORMAL)
@allure.link("http://192.168.3.1/", name="Website")
@allure.issue("AUTH-123")
@allure.testcase("TEST-123")
def test_allure_1():
    with allure.step("Open login page"):
        # Code to open the login page goes here
        logger.info("Opening login page")
        time.sleep(1)  # Simulate the time taken to open the login page
        pass

    with allure.step("Enter login credentials"):
        # Code to enter login and password goes here
        logger.info("Entering login credentials")
        time.sleep(1)  # Simulate the time taken to enter login credentials
        pass

    with allure.step("Submit login form"):
        # Code to submit the login form goes here
        logger.info("Submitting login form")
        time.sleep(1)  # Simulate the time taken to submit the login form
        pass

    with allure.step("Verify login success"):
        # Code to verify successful login goes here
        logger.info("Verifying login success")
        time.sleep(1)  # Simulate the time taken to verify login success
        pass



@allure.epic("epic: allure demo")
@allure.feature("features: test allure organize tests")
@allure.story("story: behavior-based hierarchy")
def test_allure_2():
    logger.info("behavior-based hierarchy: Epic -> Feature -> Story")
    time.sleep(1)  # Simulate the time taken for the behavior-based hierarchy test



@allure.parent_suite("allure demo")
@allure.suite("features: test allure organize tests")
@allure.sub_suite("story: suite-based hierarchy:")
def test_allure_3():
    logger.info("suite-based hierarchy: Parent Suite -> Suite -> Sub Suite")
    time.sleep(1)  # Simulate the time taken for the suite-based hierarchy test9e-