import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from tqdm import tqdm

def get_ghazal(poet_name):
    poet_name = poet_name.lower()
    poet_name = poet_name.split()
    poet_name = "-".join(poet_name)
    rekhta_link = f"https://www.rekhta.org/poets/{poet_name}/ghazals"
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--incognito')
    options.add_argument('--headless')
    options.add_argument('--disable-popup-blocking')
    options.add_argument("--disable-notifications")
    driver = webdriver.Chrome(options=options)
    driver.get(rekhta_link)
    lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    match = False
    while not match:
        lastCount = lenOfPage
        time.sleep(3)
        lenOfPage = driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
        if lastCount == lenOfPage:
            match = True
    
    xpaths=["/html/body/div[@class='wrapper innerWrapper']/div[@id='content']/div[@class='container  clearfix']/div[@class='mainContentBody']/div[@id='content']/div[@class='contentListingWrap authorPt']/div[@class='contentListing poetGhazalListing']/div[@class='contentListBody contentLoadMoreSection rt_miriyaatSec rt_manageColumn']",
            "/html/body/div[@class='wrapper innerWrapper']/div[@id='content']/div[@class='container  clearfix']/div[@class='mainContentBody']/div[@id='content']/div[@class='contentListingWrap authorPt']/div[@class='contentListing poetGhazalListing']/div[@class='contentListBody contentLoadMoreSection rt_miriyaatSec']"]
    for i in xpaths:
        val = driver.find_elements(By.XPATH,i)
        if (len(val))!=0:break
    if (len(val))==0:
        print("Author not found please check if there is some typo or the author is available on rekhta")
        driver.close;driver.quit
        exit()

    ghazals={}

    for i in tqdm(val[0].find_elements(By.CSS_SELECTOR,"a")):
        title=i.text
        if len(title)<7:continue
        link = i.get_attribute("href")
        if link:
            ghazals[title]={"Rekhta Link":link}
    driver.close()
    driver.quit()
    return ghazals
    


if __name__ == "__main__":
    poet_name = input("Please Enter the name of the artist:")
    ghazals = get_ghazal(poet_name)
    for ghazal in ghazals:
        print(ghazal, ghazals[ghazal]["Rekhta Link"])
        print("\n\n")