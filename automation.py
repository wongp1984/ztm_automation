from selenium import webdriver
chrome_browser = webdriver.Chrome('./chromedriver')

chrome_browser.maximize_window()
chrome_browser.get('https://demo.anhtester.com/basic-first-form-demo.html')

strtitle = 'Selenium Easy Demo - Simple Form to Automate using Selenium'

assert(strtitle in chrome_browser.title)

show_message_button = chrome_browser.find_element_by_class_name('btn-default')

# print(button_text.get_attribute('innerHTML'))

assert 'Show Message' in chrome_browser.page_source

user_message = chrome_browser.find_element_by_id('user-message')
user_message.clear()
user_message.send_keys('HelloWorld')
show_message_button.click()

output_message = chrome_browser.find_element_by_id('display')

assert 'HelloWorld' in output_message.text

# chrome_browser.close()
chrome_browser.quit()
chrome_browser.quit()