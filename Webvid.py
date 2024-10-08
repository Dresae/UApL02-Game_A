import requests
from bs4 import BeautifulSoup

archive_url = "https://www.liberatta.es/"

def get_video_links():
    #create response objects
    r = requests.get(archive_url)
    #create BeautifulSoup object
    soup = BeautifulSoup(r.content, 'html5lib')
    #find all video links on web page
    links = soup.findAll('a')
    #filter the link ending in .mp4
    video_links = [archive_url + link['href'] for link in links if link['href'].endswith('mp4')]

    return video_links

def download_video_series(video_links):
    for link in video_links:

        #iterate through all links in video_links & dowload them one by one
        #obtain filename by splitting url and getting last string
        file_name = link.split('/')[-1]
        print("Downloading file:%s"%file_name)