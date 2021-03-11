from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


@given('I launch Chrome browser')
def step_impl(context):
    context.driver = webdriver.Chrome()


@when('I open VistaSoft Homepage')
def step_impl(context):
    context.driver.get("https://vistasoftmonitor.com/")


@when('User navigates to login page')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "[aria-label='Login']").click()


@when('Enter username "{email}" and password "{pwd}"')
def step_impl(context, email, pwd):
    context.driver.find_element(By.CSS_SELECTOR, "[aria-label='E-mail *']").send_keys(email)
    context.driver.find_element(By.CSS_SELECTOR, "[aria-label='Password *']").send_keys(pwd)


@when('Click on log-in button')
def step_impl(context):
    context.driver.find_element(By.CLASS_NAME, "q-btn-item").click()


@then('User must successfully login to the VistaSoft Monitor main page')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//button[@data-cy='user_menu_btn']").click()
    time.sleep(20)
    context.driver.close()
