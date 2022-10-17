from selenium import webdriver

browser = webdriver.Chrome()
browser.get("https://github.com")

signin_link = browser.find_element_by_link_text("Sign in")
signin_link.click()

password_box = browser.find_element_by_link_text("password")
password_box.send_keys("v@fal123")

password_box.submit()