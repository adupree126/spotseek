import json
import os
import webbrowser

import requests

CLIENT_ID = os.environ.get('SPOTIFY_CLIENT_ID')
CLIENT_SECRET = os.environ.get('SPOTIFY_CLIENT_SECRET')
AUTH_URL = 'https://accounts.spotify.com/api/token'
PLAYLIST_URL = 'https://api.spotify.com/v1/playlists/'
playlist_id = input()


# POST
auth_response = requests.post(AUTH_URL, {
    'grant_type': 'client_credentials',
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
})

# convert the response to JSON
auth_response_data = auth_response.json()

# save the access token
access_token = auth_response_data['access_token']
headers = {
    'Authorization': 'Bearer {token}'.format(token=access_token)
}


track_count = requests.get(
    PLAYLIST_URL + playlist_id + "?fields=tracks(total)", headers=headers).json()["tracks"]["total"]

soulseek_queries = []
out = open("track_list.txt", "w")
print("track count = {}".format(track_count))
next_tracks = 'https://api.spotify.com/v1/playlists/' + playlist_id + \
    '/tracks?fields=next,fields=items(track(name,artists(name),album(name))'


while next_tracks != None:
    response = requests.get(next_tracks, headers=headers).json()
    print(str(response))
    queries = [track["track"]["name"] + " | " + track["track"]["artists"][0]["name"] + " | "
               + track["track"]["album"]["name"] for track in response["items"]]
    for q in queries:
        out.write(q + "\n")

    next_tracks = response["next"]
    print(next_tracks)


out.close()
