from turtle import end_fill
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import warnings
    
def refresh():
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="app"]/div[2]/section[1]/div/div[2]/div[1]/div[2]/div[2]/img').click()
    time.sleep(2)
    driver.get(url_refresh)
    time.sleep(2)
    for i in range(3): 
       driver.execute_script("window.scrollBy(0, 250)")
       time.sleep(1)


print('Insert the url: ')
url_refresh = input()

warnings.filterwarnings("ignore", category=DeprecationWarning)
driver = webdriver.Chrome(ChromeDriverManager().install())


driver.get(url_refresh)
driver.maximize_window()
time.sleep(2)

for i in range(3): 
       driver.execute_script("window.scrollBy(0, 250)")
       time.sleep(1)

driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/section/div[2]/div/div[1]/a[1]/div/div[2]/div[1]/span').click()
refresh()
driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/section/div[2]/div/div[1]/a[2]/div/div[2]/div[1]/span').click()
refresh()
driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/section/div[2]/div/div[1]/a[3]/div/div[2]/div[1]/span').click()
refresh()
driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/section/div[2]/div/div[1]/a[4]/div/div[2]/div[1]/span').click()
refresh()
driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/section/div[2]/div/div[1]/a[5]/div/div[2]/div[1]/span').click()
refresh()
driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/section/div[2]/div/div[1]/a[6]/div/div[2]/div[1]/span').click()
refresh()
driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/section/div[2]/div/div[1]/a[7]/div/div[2]/div[1]/span').click()
refresh()
driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/section/div[2]/div/div[1]/a[8]/div/div[2]/div[1]/span').click()
refresh()
driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/section/div[2]/div/div[1]/a[9]/div/div[2]/div[1]/span').click()
refresh()
driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/section/div[2]/div/div[1]/a[10]/div/div[2]/div[1]/span').click()
driver.close()

print("Refresh done!")

