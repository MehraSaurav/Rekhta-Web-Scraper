import requests
from bs4 import BeautifulSoup

def get_ghazal(poet_name):
    poet_name = poet_name.lower()
    poet_name = poet_name.split()
    poet_name = "-".join(poet_name)
    rekhta_link = f"https://www.rekhta.org/poets/{poet_name}/ghazals"
    req = requests.get(rekhta_link)
    soup = BeautifulSoup(req.content, "html.parser")
    # print(p)
    tags = soup.find_all('div', class_="rt_contentBodyListItems rt_GhazalItem")
    ghazals = {}
    for tag in tags:
        links = tag.find_all('a')
        for link in links:
            if link.find('i'):
                pass
            else:
                rekhta_link = link.get("href")
                ghazal = link.find('h3').text
                break
        ghazals[ghazal] = {"Rekhta Link": rekhta_link}
    return ghazals


if __name__ == "__main__":
    poet_name = input()
    ghazals = get_ghazal(poet_name)
    for ghazal in ghazals:
        print(ghazal, ghazals[ghazal]["Rekhta Link"])