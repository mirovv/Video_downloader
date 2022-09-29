# pip install requests
import re
from turtle import title
import requests
# pip install beautifulsoup4
from bs4 import BeautifulSoup
# pip install html5lib
import html5lib

base_url = "https://bs.to/"

def get_soup(url):

    # create response element
    response = requests.get(url)

    # create beautiful-soup object
    soup = BeautifulSoup(response.content, "html.parser")

    return soup

def get_season_links(soup):

    # get div with all seasons
    seasons_div = soup.find("div", id="seasons")

    # extract href from a
    season_links = [base_url + link.get("href") for link in seasons_div.find_all("a")]

    return season_links

def get_video_links(soup):

    # get all href of Vidoza Vide

    video_links = [base_url + link.get("href") for link in soup.find_all("a", title="Vidoza")]

    return video_links

if __name__ == "__main__":

    soup = get_soup(str(input("Please enter URL of a series: \n")))

    # get all seasons href
    season_links = get_season_links(soup)

    # getting all video links from a season
    video_links = get_video_links(soup)