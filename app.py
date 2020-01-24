from selenium import webdriver

#constants
url = 'http://linkedin.com'
username = 'chetankharel7@gmail.com'
password = ''
driver_path = 'D:\\chromedriver2\\chromedriver.exe'

#creates the instance of the chrome driver
driver = webdriver.Chrome(executable_path= driver_path)

#opens the website in the browser
driver.get(url)

driver.find_element_by_class_name('nav__button-secondary').click()
driver.find_element_by_id('username').send_keys(username)
driver.find_element_by_id('password').send_keys(password)
driver.find_element_by_class_name('btn__primary--large.from__button--floating').click()