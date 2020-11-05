import pyautogui
import time
from lyrics_extractor import SongLyrics
import glob
import os

print(os.getcwd())

l = open('./genius api.key', 'r')
p = open('./engine id.key', 'r')
extract_lyrics = SongLyrics(l.read(), p.read())

def list_files():
    os.chdir('./text_files')
    print('-----------------TEXT FILES-----------------')
    for file in glob.glob('*.txt'):
        print('\n' + file)
    print('\n')
    print('--------------------------------------------')
    print('\n')

def get_lyrics(song):
    temp = extract_lyrics.get_lyrics(song)
    res = temp['lyrics']
    f = open('./text_files/' + song + '.txt', 'w+')
    f.write(res)

while True:

    files = '''\n\n\nType 'search song' to find song lyrics\nor\nType 'text files' to view the available text files that has been pre searches or added\n'''
    print(files)
    text = str(input('''Enter 'search song' or 'text files' >>'''))
    if text == 'search song':
        song = str(input('Enter a song title>>'))
        get_lyrics(song)
        time.sleep(1)
        i = int(input('How many seconds do you want before the spam starts? >>'))

        while i > 0:
            print(i)
            i -= 1
            time.sleep(1)

        f = open('./text_files/' + song, 'r')
        for word in f:
            pyautogui.typewrite(word)
            pyautogui.press('enter')

        continue

    elif text == 'text files':

        list_files()

        next = str(input('''Type the file name you wish to spam\nor\nType 'back' to go back to the start\n\n>>'''))

        if next == 'back':
            continue
        else:

            time.sleep(1)
            i = int(input('How many seconds do you want before the spam starts? >>'))

            while i > 0:
                print(i)
                i -= 1
                time.sleep(1)

            f = open('./text_files/' + next, 'r')
            for word in f:
                pyautogui.typewrite(word)
                pyautogui.press('enter')

            continue
