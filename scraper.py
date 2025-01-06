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

class Scraper:
    def __init__(self):
        self.artist = ""
        self.song_title = ""
        self.page_soup = None

    def set_song(self, artist, song_title):
        self.artist = artist.lower().replace(" ", "")
        self.song_title = song_title.lower().replace(" ", "")

    def fetch_lyrics(self):
        url = f"https://www.azlyrics.com/lyrics/{artist}/{title}.html"
        self.page_soup = BeautifulSoup(requests.get(url).text, "html.parser")

         # access lyrics
    	lyric_container_div = self.page_soup.find('div', class_='col-xs-12 col-lg-8 text-center').find_all('div')[5] # the lyrics are stored in the 6th div in the parent div

	    # return lyrics
    	return lyric_container_div.text

    def fetch_cover(self):
        image_address = self.page_soup.find('img', class="album-image").get('src')
        url = f"https://www.azlyrics.com{image_address}"
        image_response = requests.get(url, stream=True)

        # save image after fetching
        if image_response.status_code == 200:
            image_location = f"/covers/{self.artist}{self.song_title}.jpg"
            with open(image_location, "wb") as fh:
                for chunk in image_response.iter_content(chunk_size=128):
                    fh.write(chunk)
            return image_location
        else:
            return None

