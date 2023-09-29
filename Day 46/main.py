from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

SPOTIFY_CLIENT_ID = '9b02baf1cc0148158a7b1448c81566b3'
SPOTIFY_CLIENT_SECRET = '1b61f08cacc047f5a18179efbe84ff2e'
SPOTIFY_TOKEN = 'Day 46\\token.txt'
user_id = 'BQCqT9iz3aUHqNaBjk0jB_yVubVAgzmRpQFeFqSzOIrVq3uXaRS3fayeAgwhN41ZC_71JYueqh8PJRFHMQCYRoYi6iTX0DQLfJQQ7ciEIrn7itEp7R011BG2Mmfw3vrFOPXd9SeiSkSYdmKvcuslyVvLcE3vZmGD-ZCiYWEESUP-F-lex-CA7n_CFGbKuGi6_8dUtBRerXJNEBxZVDZ_vr3FOreWkwPTLvtc1A'

date = input("Give me the date you want to see the top 100, in the format YYYY-MM-DD:\n")

response = requests.get("https://www.billboard.com/charts/hot-100/" + date)
soup = BeautifulSoup(response.text, 'html.parser')

song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt",
        username='Matthew Schembri', 
    )
)

song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")
        
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)


sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)        