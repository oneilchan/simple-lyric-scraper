# imports
from bs4 import BeautifulSoup
import requests 

def scraper(artist, title):
	try:
		artist = artist.replace(" ", "")
		title = title.replace(" ", "")

		# get page and parse html data 
		lyric_page = requests.get(f"https://www.azlyrics.com/lyrics/{artist}/{title}.html")

	    # access html as objects 
		page_soup = BeautifulSoup(lyric_page.text, "html.parser")

	    # access lyrics
		lyric_container_div = page_soup.find('div', class_='col-xs-12 col-lg-8 text-center').find_all('div')[5] # the lyrics are stored in the 6th div in the parent div
	
	    # return lyrics
		return lyric_container_div.text

    # in case lyrics not found
	except AttributeError:
		return "Lyrics not found"

