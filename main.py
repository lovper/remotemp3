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
    print(songs.index(song), song)


while play:
    choice = input('Choose a song with corresponding number: ')
    try:
        choice = int(choice)
        choice = songs[choice]
        mixer.init()
        mixer.music.load(choice)
        mixer.music.play()
    except:
        if choice == 'pause':
            try:
                mixer.music.pause()
            except:
                print('No music playing')
        elif choice == 'play':
            try:
                mixer.music.unpause()
            except:
                print('No music choosen')
        elif choice == 'stop':
            break
        elif choice == 'list':
            try:
                for song in songs:
                    print(songs.index(song), song)
            except:
                print('Error')
        else:
            print('Not a choice')
