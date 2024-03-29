from Get_Ghazals import get_ghazal
import requests
from bs4 import BeautifulSoup

def get_youtube_link(ghazal_link):
    req = requests.get(ghazal_link)
    soup = BeautifulSoup(req.content, "html.parser")
    tags = soup.find_all('div', class_="videoListItem clearfix")
    youtube_links = {}
    for tag in tags:
        youtube_links[f"https://www.youtube.com/watch?v={tag['data-id']}"] = tag['data-desc']
    return youtube_links

if __name__ == "__main__":
    print(get_youtube_link("https://www.rekhta.org/ghazals/saare-aalam-kaa-yahii-armaan-honaa-chaahiye-aadil-farhat-ghazals?sort=popularity-desc"))