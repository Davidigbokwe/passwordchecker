from selenium import webdriver


chrome_browser = webdriver.Chrome('./chromedriver')

chrome_browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

show_message_button = chrome_browser.find_element_by_class_name('btn-default')

assert 'Show Message' in chrome_browser.page_source


user_message = chrome_browser.find_element_by_id('user-message')
user_button =chrome_browser.find_element_by_css_selector('#get-input > .btn')
#print(user_button)
user_message.clear()
user_message.send_keys('I AM EXTRA COOL')

show_message_button.click()

output_message = chrome_browser.find_element_by_class_name('display')

assert 'I AM EXTRA COOL' in output_message.text

chrome_browser.quit()