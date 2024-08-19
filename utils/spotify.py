import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="your-spotify-client-id",
                                               client_secret="your-spotify-client-secret",
                                               redirect_uri="your-redirect-uri",
                                               scope="user-modify-playback-state user-read-playback-state"))

def get_active_device():
    devices = sp.devices()
    if not devices['devices']:
        print("Nyra: No active devices found. Please start Spotify on one of your devices.")
        return None
    return devices['devices'][0]['id']

def play_song():
    song_name = input("Nyra: What song would you like to play on Spotify? ")
    device_id = get_active_device()
    if not device_id:
        return
    print(f"Nyra: Playing '{song_name}' on Spotify...")
    results = sp.search(q=song_name, limit=1, type='track')
    if results['tracks']['items']:
        track_uri = results['tracks']['items'][0]['uri']
        sp.start_playback(device_id=device_id, uris=[track_uri])
    else:
        print("Nyra: Sorry, I couldn't find that song on Spotify.")

def pause_music():
    device_id = get_active_device()
    if not device_id:
        return
    print("Nyra: Pausing the music...")
    sp.pause_playback(device_id=device_id)

def resume_music():
    device_id = get_active_device()
    if not device_id:
        return
    print("Nyra: Resuming the music...")
    sp.start_playback(device_id=device_id)

def next_track():
    device_id = get_active_device()
    if not device_id:
        return
    print("Nyra: Skipping to the next track...")
    sp.next_track(device_id=device_id)

def previous_track():
    device_id = get_active_device()
    if not device_id:
        return
    print("Nyra: Going back to the previous track...")
    sp.previous_track(device_id=device_id)

def play_playlist():
    playlist_name = input("Nyra: What playlist would you like to play on Spotify? ")
    device_id = get_active_device()
    if not device_id:
        return
    print(f"Nyra: Playing the playlist '{playlist_name}' on Spotify...")
    results = sp.search(q=playlist_name, limit=1, type='playlist')
    if results['playlists']['items']:
        playlist_uri = results['playlists']['items'][0]['uri']
        sp.start_playback(device_id=device_id, context_uri=playlist_uri)
    else:
        print("Nyra: Sorry, I couldn't find that playlist on Spotify.")
