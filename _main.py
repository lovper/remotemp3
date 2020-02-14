from pygame import mixer
import os

songs = []


def play(inp):
    inp = int(inp)
    inp = songs[inp]
    mixer.init()
    mixer.music.load(inp)
    mixer.music.play()
    rtstr = 'Playing: '+inp
    return rtstr


def pause():
    try:
        mixer.music.pause()
        return 'Paused'
    except:
        return 'No music playing'


def resume():
    try:
        mixer.music.unpause()
        return 'Playing resumed'
    except:
        return 'No music playing'


def stop():
    try:
        mixer.music.stop()
        return 'Playback stopped'
    except:
        return 'Nothing playing'


def exit():
    return 'exit'


def slist():
    try:
        rstr = ''
        for song in songs:
            apstr = song
            rstr += str(songs.index(song)) + ': ' + apstr + '\n'
        rstr += 'Enter the number corresponding to the song of your choice'
        return rstr
    except:
        'Error listing sound files'


def help():
    return '\n-----Try one of these-----\n' \
           'pause   -   pauses music\n' \
           'resume  -   continue playing/unpause\n' \
           'stop    -   stops the music\n' \
           'slist   -   lists all music\n' \
           'exit    -   exits the program\n' \
           'help    -   this help list, duh\n'


funcs = ['resume', 'pause', 'stop', 'exit', 'slist', 'help']

class Main:
    def __init__(self, mdir):
        self.mdir = mdir
        for root, dirs, files in os.walk(os.path.normpath(mdir)):
            for file in files:
                path = root + '/' + file
                songs.append(path)

    def inp(self, inp):
        if inp.isnumeric():
            try:
                rt = play(inp)
                return rt
            except:
                return 'Error'
        else:
            if inp in funcs:
                e = inp+'()'
                exec('global i; i = %s' % e)
                global i
                return i
            else:
                return 'Not an input'
