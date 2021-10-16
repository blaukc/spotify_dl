import os
import sys
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_dir, 'deezer_python_lib'))

import deezer_python

client = deezer_python.Client()                    #initialise deezer

def get_track_link(track_name, album, artist):
    search_tracks = client.search(track_name + ' ' + artist, relation='track')      #gets track search output from deezer

    for track in search_tracks:                                 #loops through search output for correct track
        if artist.lower() in track.get_artist().name.lower() and album.lower() in track.get_album().title.lower():      #if artist and album match, return url
            return track.link
    #"backup" method if cant find track
    for track in search_tracks:
        if artist.lower() in track.get_artist().name.lower() and track_name == album:      #if artist match and album = track name, return url
            return track.link
    #"backup backup" method if cant find track
    for track in search_tracks:
        if artist.lower() in track.get_artist().name.lower():      #if artist match, return url
            return track.link

def get_album_link(album, artist):
    search_albums = client.search(album, relation='album')      #gets album search output from deezer

    for album in search_albums:
        if artist.lower() in album.get_artist().name.lower():
            return album.link




# arl = '3dadffaa3ed08377420042cf0ede03f5f02fe54be0499fde032737b32b8c3632d08ddca191262e50a16ae8f001a6877141188a6692a8f2426d6af58036e74232e9502403c1c2db250326471544ffb97f8663fa79035e50b4425947e632d56ae0'
#
# track = input("Enter track: ")
# artist = input("Enter artist: ")
# album = input("Enter album: ")
# print(get_track_link(track, album, artist))
