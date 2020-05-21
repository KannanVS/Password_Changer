from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import getpass 
import json
import time


def main():
    f = open("details.JSON", "r")
    data = json.load(f)

    # Fetching details from user

    userName = input('Enter the username: ')
    password = getpass.getpass('Enter the password: ')
    newPassword = getpass.getpass('Enter the new password: ')

    # driver initialisation and navigating to instagram

    driver = webdriver.Firefox()
    driver.get('https://www.instagram.com')
    uid = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, data["username"]))) # sending username
    uid.click()
    uid.send_keys(userName)


    uid = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, data["password"]))) # sending password
    uid.click()
    uid.send_keys(password)
    time.sleep(2)


    btn = driver.find_element_by_css_selector(data['logIn']) # login to instagram
    btn.click()
    time.sleep(5)


    prf = driver.find_element_by_css_selector(data['profile']) # navigating to profile
    prf.click()
    time.sleep(5)


    setting = driver.find_element_by_css_selector(data['setting']) # navigating to setting
    setting.click()
    time.sleep(5)


    changePassword = driver.find_element_by_css_selector(data['change_password']) # selecting change password
    changePassword.click()
    time.sleep(5)


    oldPassword = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, data["old_password"]))) # entering old password in text box
    oldPassword.click()
    oldPassword.send_keys(password)
    time.sleep(2)


    newPass = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, data["new_password"]))) # entering new password in text box
    newPass.click()
    newPass.send_keys(newPassword)


    confirmPassword = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, data["confirm_password"]))) # confirmation of new password
    confirmPassword.click()
    confirmPassword.send_keys(newPassword)


    change = driver.find_element_by_css_selector(data['change']) # changing password
    change.click()
    time.sleep(5)

    print('Password changed Successfully')
    


if __name__ == '__main__':
    main()
