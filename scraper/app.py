import json
import os
import time

from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# start by defining the options
options = webdriver.ChromeOptions()
# options.headless = True # it's more scalable to work in headless mode
# normally, selenium waits for all resources to download
# we don't need it as the page also populated with the running javascript code.
options.page_load_strategy = 'none'
# this returns the path web driver downloaded
chrome_path = ChromeDriverManager().install()
chrome_service = Service(chrome_path)
# pass the defined options and service objects to initialize the web driver
driver = Chrome(options=options, service=chrome_service)
driver.implicitly_wait(5)

url = "https://projekt202-intranet--simpplr.vf.force.com/apex/simpplr__app?u=/site/a145f000000J9ikAAC/dashboard"

driver.get(url)
time.sleep(3)

uname = driver.find_element(By.ID, "username")
uname.send_keys(os.environ["HOMEBASE_CRAWLER_USERNAME"])
submit = driver.find_element(By.CSS_SELECTOR,
                             "#root > div > div > div.sc-dymIpo.izSiFn > div.withConditionalBorder.sc-bnXvFD.cQPnwe > div.sc-jzgbtB.bIuYUf > form > div > div:nth-child(3) > div > button")
submit.click()
time.sleep(1)
pw = driver.find_element(By.ID, "password")
pw.send_keys(os.environ["HOMEBASE_CRAWLER_PASSWORD"])
submit = driver.find_element(By.CSS_SELECTOR,
                             "#root > div > div > div.sc-dymIpo.izSiFn > div.withConditionalBorder.sc-bnXvFD.cQPnwe > div.sc-jzgbtB.bIuYUf > form > div > div:nth-child(4) > div > button")
submit.click()

time.sleep(10)

submit = driver.find_element(By.CSS_SELECTOR,
                             "#root > div > div > div.sc-dymIpo.izSiFn > div.withConditionalBorder.sc-bnXvFD.cQPnwe > div.sc-jzgbtB.bIuYUf > div > div.sc-bZQynM.QzQWh > div:nth-child(2) > button")

submit.click()

time.sleep(10)

strings = {}
urls = [
    "https://projekt202-intranet--simpplr.vf.force.com/apex/simpplr__app?u=/site/a145f000000J9ikAAC/dashboard",
    "https://projekt202-intranet--simpplr.vf.force.com/apex/simpplr__app?u=/site/a145f000000J9iiAAC/dashboard"
]


def grab_information_per_url(url):
    driver.get(url)
    time.sleep(3)
    sites = driver.find_elements(By.CSS_SELECTOR,
                                 "ul.TileList > li > h2 > a")
    for i in range(len(sites)):
        sites = driver.find_elements(By.CSS_SELECTOR,
                                     "ul.TileList > li > h2 > a")

        sites[i].click()
        time.sleep(5)
        articles = driver.find_elements(By.CSS_SELECTOR,
                                        "body > div.page > div.main > div:nth-child(2) > div > div.row > div > div.Page > div > div > div.Page-row > div > div:nth-child(2) > ul > li > div.ListingItem-inner > h2 > a")
        for j in range(len(articles)):
            articles = driver.find_elements(By.CSS_SELECTOR,
                                            "body > div.page > div.main > div:nth-child(2) > div > div.row > div > div.Page > div > div > div.Page-row > div > div:nth-child(2) > ul > li > div.ListingItem-inner > h2 > a")
            articles[j].click()
            time.sleep(5)
            content = driver.find_element(By.CSS_SELECTOR,
                                          "body > div.page > div.main > div:nth-child(2) > div > div.row > div > div")
            strings[driver.current_url] = content.text
            driver.execute_script("window.history.go(-1)")

        driver.execute_script("window.history.go(-1)")


for url in urls:
    grab_information_per_url(url)

json_str = json.dumps(strings)

with open("homebase_articles.json", "w") as fd:
    fd.write(json_str)
