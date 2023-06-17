from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os
import time
driver = webdriver.ChromeOptions()
driver.add_argument("--headless")
driver.add_argument('--blink-settings=imagesEnabled=false')
#driver.add_argument("--disable-dev-shm-usage")
#driver.add_argument("--no-sandbox")
#driver.add_argument(f'user-agent={user_agent}')
driver = webdriver.Chrome(options=driver)
#driver.get("http://www.python.org")
driver.get("https://twitter.com/ArpitBala")
time.sleep(3)
listt=[]


for i in range(5000):
    element = driver.find_elements(By.CSS_SELECTOR, "[data-testid='tweetText']")
    
    try:
        
            if len(listt) == 0 or listt[-1] != element[0].text : 
                print(len(element))
                listt.append(element[0].text)
    except:
        print()

    driver.execute_script("window.scrollBy(0,150)","")
    element.clear()

    time.sleep(.05)
#print(listt)
print(len(listt))

newList=[]
for p in listt:
    q=p.split()
    for r in q:
        newList.append(r)
newList.sort()
print(newList)
print(len(newList))
driver.close()