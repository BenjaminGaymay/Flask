from itunes import *
from dofus import *
from media import *
from shutdown import *
from epitech import *
from playlist import *

from flask import Flask, request, render_template
from urllib.request import urlopen
from os.path import getmtime
from collections import OrderedDict
from datetime import datetime
from locale import setlocale, LC_TIME


app = Flask(__name__)
app.secret_key = 'antilope'


@app.route('/', methods=['POST', 'OPTIONS'])
def googleHomeControl():

    if request.json and "secret" in request.json:

        if "ghome" not in request.json and request.remote_addr != "192.168.0.11":
            return "Antilope"

        if "music" in request.json:
            startMusic(request.json['secret'], request.json['music'])
        if "map" in request.json:
            changeDMap(request.json['secret'], request.json['map'])
        if "media" in request.json:
            controlMedia(request.json['secret'], request.json['media'])
        if "shutdown" in request.json:
            shutdownComputer(request.json['secret'])
        if "standby" in request.json:
            standByComputer(request.json['secret'])
        if "epitech" in request.json:
            openEpitech(request.json['secret'])

    return "Antilope"


@app.route('/', methods=['GET'])
def getMusics():

    extensions = [".mp3", ".ogg", ".wav"]
    musics_by_alpha = {}
    musics_by_date = {}
    musics_by_playlist = associateMusicsByName(readPlaylists())

    for music in MUSICS_LIST:
        music_name = music['file_name'].split("\\")[1]
        for extension in extensions:
            music_name = music_name.replace(extension, "")

        music_name = ' '.join([w.title() if w.islower() else w for w in music_name.split()])

        index_alpha = music_name[0]
        index_date = datetime.fromtimestamp(getmtime(MUSIC_PATH + music["file_name"])).strftime("%Y-%m-%e")

        if index_alpha not in musics_by_alpha:
            musics_by_alpha[index_alpha] = []
        if index_date not in musics_by_date:
            musics_by_date[index_date] = []

        music = {'name': music_name,
                 'path': music["path"],
                 'date': datetime.fromtimestamp(getmtime(MUSIC_PATH + music["file_name"])).strftime("%A %e %B %Y").title()
                }
        musics_by_alpha[index_alpha].append(music)
        musics_by_date[index_date].append(music)

    return render_template("list_music.html", musics_by_date=OrderedDict(sorted(musics_by_date.items(), reverse=True)),
                                            musics_by_alpha=OrderedDict(sorted(musics_by_alpha.items())),
                                            musics_by_playlist=musics_by_playlist)


if __name__ == '__main__':

    setlocale(LC_TIME, '')
    app.run(host="0.0.0.0", port=9090, debug=True)
