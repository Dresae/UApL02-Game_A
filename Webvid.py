import requests
from bs4 import BeautifulSoup

archive_url = "https://www.liberatta.es/"

def get_video_links():
    #create response objects
    r = requests.get(archive_url)
    #create BeautifulSoup object
    soup = BeautifulSoup(r.content, 'html5')