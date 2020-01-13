from pygame import mixer
import os

mdir = input('Where is your music?: ')
play = True
songs = []

for root, dirs, files in os.walk(os.path.normpath(mdir)):
    for file in files:
        path = root + '/' + file
        songs.append(path)

for song in songs:
    print(songs.index(song), song),




while play:
    inp = input('Input: ')
    try:
        inp = int(inp)
        inp = songs[inp]
        mixer.init()
        mixer.music.load(inp)
        mixer.music.play()
    except:
        if inp == 'pause':
            try:
                mixer.music.pause()
            except:
                print('No music playing')
        elif inp == 'play':
            try:
                mixer.music.unpause()
            except:
                print('No music choosen')
        elif inp == 'stop':
            break
        elif inp == 'list':
            try:
                for song in songs:
                    print(songs.index(song), song)
            except:
                print('Error')
        elif inp == 'help':
            print('\n---Try one of these---\n')
            print('pause - pauses music')
            print('play - continue playing/unpause')
            print('stop - Exits the program')
            print('list - lists all music')
            print('\n')
        else:
            print('Not a inp')
