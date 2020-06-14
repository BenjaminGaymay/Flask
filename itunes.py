from keyboard import *
from secret import *

from time import sleep
from subprocess import check_output
from os import listdir
from os.path import isdir
from time import sleep
from random import randint


def playMusicByName(music):

    try:
        command = "start \"%s\" \"%s\"" % (
            ITUNES_PATH, MUSIC_PATH + music['file_name'])
        check_output(command, shell=True)
        sleep(1)
        shortcut("alt", "esc")
    except:
        pass


def findMusicFiles(music_name):

    words = music_name.lower().split()
    words.sort(key=len, reverse=True)
    musics_found = MUSICS_LIST
    for word in words:
        musics_for_word = []
        for music in musics_found:
            if word in music['lower']:
                musics_for_word.append(music)
        if musics_for_word:
            musics_found = musics_for_word

    return musics_found


def startMusic(secret, music_name):

    if secret != getSecret("Itunes"):
        return

    musics_found = findMusicFiles(music_name)

    if len(musics_found) > 1:
        choosen_music = musics_found[randint(0, len(musics_found) - 1)]
        playMusicByName(choosen_music)
    elif musics_found:
        playMusicByName(musics_found[0])


ITUNES_PATH = r"C:\Program Files\iTunes\iTunes.exe"
MUSIC_PATH = r"C:\Users\Benjamin\Music\Musique" + "\\"
MUSICS_LIST = []
for artist in listdir(MUSIC_PATH):
    if isdir(MUSIC_PATH + artist):
        for file in listdir(MUSIC_PATH + artist):
            if file.endswith(".mp3") or file.endswith(".wav") or file.endswith(".ogg"):
                MUSICS_LIST.append({
                    'lower': file.lower(),
                    'file_name': artist + "\\" + file,
                    'path': "static/musics/" + artist + '/' + file
                    })
