# pip install requests
from turtle import title
import requests
# pip install beautifulsoup4
from bs4 import BeautifulSoup

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

def get_video_links(url):

    soup = get_soup(url)

    # get soup of Vidoza

    a_tag_soup = soup.find_all("a", title="Vidoza")

    # check if array is empty

    if not a_tag_soup:
        a_tag_soup = soup.find_all("a", title="Streamtape")

    # get all href of Vidoza Videos

    video_links = [base_url + link.get("href") for link in a_tag_soup]

    return video_links

def write_txt_File(arr):

    f = open("bluemountainstate_links.txt", "w")

    for link in arr:
        f.write(link + "\n")

    f.close()

if __name__ == "__main__":

    video_links = []

    soup = get_soup(str(input("\nPlease enter URL of a series: \n")))
    # get all seasons href
    season_links = get_season_links(soup)

    # getting all video links from all season
    for link in season_links:
        video_links.extend(get_video_links(link))

    write_txt_File(video_links)