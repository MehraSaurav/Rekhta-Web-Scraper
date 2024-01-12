from difflib import SequenceMatcher
import requests


def similar(a, b):
    a = a.lower()
    b = b.lower()
    # print(b)
    return SequenceMatcher(None, a, b).ratio()


def youtube_links(poet, ghazal, api_key):
    l = len(ghazal)
    query = ghazal.replace(" ", "+") + "+" + poet.replace(" ", "+")
    req = requests.get(
        f'https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=5&q={query}&key={api_key}&type=video')
    if req.status_code == 403:
        return ["Quote Exceeded"]
    else:
        req = req.json()['items']
        videos = []
        for video in req:
            try:
                video_id, title = video['id']['videoId'], video['snippet']['title']
                similarity = similar(ghazal, title)
                for i in range(l, len(title) + 1):
                    similarity = max(similarity, similar(ghazal, title[i - l: i + 1]))
                if similarity >= 0.6:
                    videos.append(f"https://www.youtube.com/watch?v={video_id}")
            except:
                print(video)
        return videos


def description(link, api_key):
    video_id = link.split("=")[-1]
    videodata = requests.get(
        f"https://www.googleapis.com/youtube/v3/videos?part=statistics&part=snippet&id={video_id}&key={api_key}")
    if videodata.status_code == 403:
        return "Quote Exceeded"
    return (videodata.json()['items'][0]['snippet']['title'], videodata.json()['items'][0]['statistics']['viewCount'])


if __name__ == "__main__":
    api_key = 'AIzaSyCYVmth3Qne2D6yLuZSjdjWChkCmrnNDGQ'
    ghazal = "din kuchh aise guzarta hai koi"
    poet = "gulzar"
    print(len(youtube_links(poet, ghazal,api_key)))

