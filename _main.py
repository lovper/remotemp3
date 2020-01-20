from pygame import mixer
import os

songs = []


class Main:
    def __init__(self, mdir):
        self.mdir = mdir
        for root, dirs, files in os.walk(os.path.normpath(mdir)):
            for file in files:
                path = root + '/' + file
                songs.append(path)

    def slist(self):
        rstr = ''
        for song in songs:
            apstr = song
            rstr += str(songs.index(song)) + ': ' + apstr + '\n'
        return rstr

    def inp(self, inp):
        try:
            inp = int(inp)
            inp = songs[inp]
            mixer.init()
            mixer.music.load(inp)
            mixer.music.play()
            return 'Playing...'
        except:
            if inp == 'pause':
                try:
                    mixer.music.pause()
                    return 'Paused'
                except:
                    return 'No music playing'
            elif inp == 'play':
                try:
                    mixer.music.unpause()
                    return 'Playback started'
                except:
                    return 'No music choosen'
            elif inp == 'stop':
                try:
                    mixer.music.stop()
                    return 'Playback stopped'
                except:
                    return 'No music playing'
            elif inp == 'exit':
                return "exit"
            elif inp == 'list':
                try:
                    p = self.slist()
                    print(p)
                    return p
                except:
                    return 'Unknown error'
            elif inp == 'help':
                return '\n---Try one of these---\n' \
                       'pause - pauses music\n' \
                       'play - continue playing/unpause\n' \
                       'stop - stops the music\n' \
                       'list - lists all music\n' \
                       'exit - exits the program\n'
            else:
                return 'Not an input'
