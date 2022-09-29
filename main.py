# pip install requests
import requests
# pip install beautifulsoup4
from bs4 import BeautifulSoup

archive_url = str(input("Please enter URL of a series: \n"))

def get_video_link(url):

    # create response element
    response = requests.get(url)

    # create beautiful-soup object
    soup = BeautifulSoup(response.content, "html5lib")

    print(soup)


def openBrowser(url):
    pass


get_video_link(archive_url)