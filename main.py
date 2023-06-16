from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
#driver.get("http://www.python.org")
driver.get("https://twitter.com/iam_juhi")
time.sleep(3)
listt=[]


for i in range(50):
        element = driver.find_elements(By.CSS_SELECTOR, "[data-testid='tweetText']")
        for x in element:
            if x:
                listt.append(x.text)
        driver.execute_script("window.scrollBy(0,300)","")
        time.sleep(.01)
#print(listt)
#print(len(listt))

newList=[]
for p in listt:
    q=p.split()
    for r in q:
        newList.append(r)

print(newList)
print(len(newList))
driver.close()