from bs4 import BeautifulSoup
import requests


running = True
while running:
	# get song from user (artist name and song title have to be lowered and spaces to remove to work with azlyrics)
	artist = input("Artist: ").lower().replace(" ", "")
	song_title = input("song title: ").lower().replace(" ", "")

	# get page and parse html data 
	lyric_page = requests.get(f"https://www.azlyrics.com/lyrics/{artist}/{song_title}.html")

	# access html as objects 
	page_soup = BeautifulSoup(lyric_page.text, "html.parser")

	# access lyrics
	lyric_container_div = page_soup.find('div', class_='col-xs-12 col-lg-8 text-center').find_all('div')[5] # the lyrics are stored in the 6th div in the parent div
	
	# print lyrics
	print(lyric_container_div.text)

