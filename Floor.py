from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import warnings
from datetime import date
import csv


warnings.filterwarnings("ignore", category=DeprecationWarning)
driver = webdriver.Chrome(ChromeDriverManager().install())

lista = []

driver.get('https://www.jpg.store/collection/claynation')
driver.maximize_window()
time.sleep(2)
floor_clay = driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[3]/div[1]/div/div[3]/div[1]').text

driver.get('https://www.jpg.store/collection/yummiuniverse')
time.sleep(2)
floor_yummi = driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[3]/div[1]/div/div[3]/div[1]').text

driver.get('https://www.jpg.store/collection/cardanobits')
time.sleep(2)
floor_cbits = driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[3]/div[1]/div/div[3]/div[1]').text

driver.get('https://www.jpg.store/collection/pavia')
time.sleep(2)
floor_pavia = driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[3]/div[1]/div/div[3]/div[1]').text

driver.get('https://www.jpg.store/collection/cardanowarriors')
time.sleep(2)
floor_warriors = driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[3]/div[1]/div/div[3]/div[1]').text

driver.get('https://www.jpg.store/collection/yummiuniversespoopy')
time.sleep(2)
floor_spoopy = driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[3]/div[1]/div/div[3]/div[1]').text

driver.get('https://www.jpg.store/collection/grandmasteradventurer')
time.sleep(2)
floor_GMA = driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[3]/div[1]/div/div[3]/div[1]').text

driver.get('https://www.jpg.store/collection/theapesociety')
time.sleep(2)
floor_ape = driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[3]/div[1]/div/div[3]/div[1]').text


driver.close()
data = date.today()

print(f'Floor Clay Nation: {floor_clay} ADA')
print(f'Floor Yummi Universe: {floor_yummi} ADA')
print(f'Floor CardanoBits: {floor_cbits} ADA')
print(f'Floor Pavia: {floor_pavia} ADA')
print(f'Floor Ape Society: {floor_ape} ADA')
print(f'Floor Cardano Warriors: {floor_warriors} ADA')
print(f'Floor Spoopy Naru: {floor_spoopy} ADA')
print(f'Floor GMA: {floor_GMA} ADA')


lista.append(data)
lista.append(floor_clay)
lista.append(floor_yummi)
lista.append(floor_cbits)
lista.append(floor_pavia)
lista.append(floor_warriors)
lista.append(floor_spoopy)
lista.append(floor_GMA)
lista.append(floor_ape)


with open(f'{data}.csv', 'w+') as f:
    write = csv.writer(f)
    write.writerow(lista)
