import time
from selenium import webdriver

def getTheShoe():

    driver = webdriver.Chrome(executable_path=r"C:\Users\JC\OneDrive\Documents\SneakerBot\chromedriver.exe")
    driver.maximize_window()
    driver.get('https://www.hotboxtoronto.com/products/nike-sb-dunk-low-supreme-stars-barkroot-brown?variant=39484277096642')
    # Adds shoe to cart
    driver.find_element_by_xpath('/html/body/main/div[1]/div/div[1]/div/div/div[2]/div[2]/div/form/div[3]/button').click()
    time.sleep(2)
    # Takes you to the shopping cart page
    driver.find_element_by_xpath('/html/body/div[1]/div/header/div/div[1]/div[2]/ul/li[8]/a/span/span').click()
    # Takes you to checkout
    driver.find_element_by_xpath('/html/body/main/div/div/div/form/div[2]/div[2]/div/div[2]/div/span[2]/input').click() 
    time.sleep(2)
    # Inputs all shipping information
    driver.find_element_by_xpath('/html/body/div/div/div/main/div[1]/form/div[1]/div[1]/div[2]/div[1]/div/div/input').send_keys('youremail@gmail.com') 
    driver.find_element_by_xpath('/html/body/div/div/div/main/div[1]/form/div[1]/div[2]/div[2]/div/div[1]/div[1]/div/input').send_keys('FirstName')
    driver.find_element_by_xpath('/html/body/div/div/div/main/div[1]/form/div[1]/div[2]/div[2]/div/div[1]/div[2]/div/input').send_keys('LastName')
    driver.find_element_by_xpath('/html/body/div/div/div/main/div[1]/form/div[1]/div[2]/div[2]/div/div[1]/div[4]/div/input').send_keys('123 Appleby Lane')
    driver.find_element_by_xpath('/html/body/div/div/div/main/div[1]/form/div[1]/div[2]/div[2]/div/div[1]/div[6]/div/input').send_keys('Toronto')
    driver.find_element_by_xpath('/html/body/div/div/div/main/div[1]/form/div[1]/div[2]/div[2]/div/div[1]/div[9]/div/input').send_keys('M4M 3P1')
    driver.find_element_by_xpath('/html/body/div/div/div/main/div[1]/form/div[1]/div[2]/div[2]/div/div[1]/div[10]/div/input').send_keys('1234567890')
    driver.find_element_by_xpath('/html/body/div/div/div/main/div[1]/form/div[2]/button').click()
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div/div/div/main/div[1]/form/div[2]/button').click()
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div/div/div/main/div[1]/div/form/div[3]/div[1]/button').click()
    time.sleep(2)
    # Takes you to PayPal
    driver.find_element_by_xpath('/html/body/div[1]/section[2]/div/div/div[4]/button').click()
    time.sleep(3)
    # Inputs all payment information
    driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/main/div/form/section[2]/div[2]/div/div/div/input').send_keys('1234567890123456')
    driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/main/div/form/section[2]/div[3]/div[1]/input').send_keys('12/34')
    driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/main/div/form/section[2]/div[3]/div[2]/div/div/div[2]/input').send_keys('123')
    driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/main/div/form/section[3]/section/div[1]/div/div[2]/div/input').send_keys('1234567890')
    driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/main/div/form/section[3]/div[2]/div/label').click()
    driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/main/div/form/section[3]/div[2]/fieldset/div/div/label').click()
    driver.find_element_by_xpath('/html/body/div/div/div/main/div[1]/div/form/div[1]/div[2]/div[1]/fieldset/div[3]/div[1]/input').click()
    time.sleep(50) # Allows 50 seconds for user to override and take over to make the purchase

getTheShoe()

    
