from flask import Flask, request, jsonify
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

app = Flask(__name__)

client_id = "58359343c27240ac9df7338477111e8d"
client_secret = "889b29e34e154cd9956319a52f8dcd4f"

@app.route('/fetch_tracks', methods=['Post'])
def fetch_tracks():
    data = request.json 
    playlist_id = data.get('playlist_id')

    client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    results = sp.playlist_tracks(playlist_id)
    tracks = []

    for item in results['items']:
        track_info = {
            'name': item['track']['name']
        }
        tracks.append(track_info)

    return jsonify({'tracks': tracks})


if __name__ == '__main__':
    app.run(debug=True, port=3000)