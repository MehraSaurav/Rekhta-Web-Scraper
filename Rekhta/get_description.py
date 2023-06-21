import xlwings as xw
from artist_using_chat_gpt import get_artist_name
import requests
from bs4 import BeautifulSoup

api_key = 'AIzaSyCYVmth3Qne2D6yLuZSjdjWChkCmrnNDGQ'

def get_artist(video_id):
    link = f"https://www.googleapis.com/youtube/v3/videos?part=snippet&id={video_id}%2C+Xxsdw6zG1bg&key={api_key}"
    req = requests.get(link)
    req = req.json()["items"][0]["snippet"]
    title = req["title"]
    description = req["description"]
    return get_artist_name(title, description), title, description

def get_artist_excel():
    excel_file = "Ghazals.xlsx"
    wb = xw.Book(excel_file)
    ws = wb.sheets['Sheet1']
    for i in range(2, 15):
        video = ws[f'B{i}'].value
        if video == None or "spotify" in video:
            continue
        video_id = video.split("watch?v=")[1]
        artist, title, description = get_artist(video_id)
        ws[f'C{i}'].value = artist
        ws[f'D{i}'].value = title
        ws[f'E{i}'].value = description
        print(i)

get_artist_excel()