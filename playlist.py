from itunes import MUSIC_PATH, MUSICS_LIST
from os import listdir
from pprint import pprint


def readPlaylists():

    playlists = {}

    for playlist in listdir(PLAYLIST_PATH + "fromPlaylistBackup"):

        with open(PLAYLIST_PATH + "fromPlaylistBackup\\" + playlist, 'r') as fd:
            musics = fd.readlines()

        newMusics = [ music if "/storage" not in music else "\\".join(music.split('/')[4:]) for music in musics ]
        playlists[playlist.split('.')[0]] = newMusics

        if musics != newMusics:
            with open(PLAYLIST_PATH + "fromPlaylistBackup\\" + playlist, 'w') as fd:
                fd.writelines(newMusics)

    return playlists


def associateMusicsByName(playlists):

    extensions = [".mp3", ".ogg", ".wav"]

    playlistsWithMusicInfos = {}
    for playlist in playlists.keys():
        playlistsWithMusicInfos[playlist] = []

    for playlist, musics in playlists.items():
        for toFind in musics:
            for music in MUSICS_LIST:
                if music['file_name'] == toFind[:-1]:

                    music_name = music['file_name'].split("\\")[1]
                    for extension in extensions:
                        music_name = music_name.replace(extension, "")

                    playlistsWithMusicInfos[playlist].append({
                        'name': music_name,
                        'path': music['path'],
                        'playlist': playlist
                    })
    return playlistsWithMusicInfos


def toM3U():

    return ""


PLAYLIST_PATH = r"C:\Users\Benjamin\Documents\Flask\static\playlists\\"

if __name__ == '__main__':

    pprint(associateMusicsByName(readPlaylists()))
