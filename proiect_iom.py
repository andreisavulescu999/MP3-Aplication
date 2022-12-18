import pygame #used to create video games
import tkinter as tkr #used to develop GUI
from tkinter.filedialog import askdirectory #it permit to select dir
import os #it permits to interact with the operating system
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from tkinter import *
from tkinter import filedialog
import ntpath
from scipy.io import wavfile

music_player = tkr.Tk() 
music_player.title('Proiect IOM') 
music_player.geometry('650x450')

directory = askdirectory()
os.chdir(directory) #it permits to chenge the current dir
song_list = os.listdir() #it returns the list of files song

play_list = tkr.Listbox(music_player, font='Helvetica 12 bold', bg='yellow', selectmode=tkr.SINGLE)
for item in song_list:
    pos = 0
    play_list.insert(pos, item)
    pos += 1
    
pygame.init()
pygame.mixer.init()

def open_file():
    filepath = filedialog.askopenfilename(title='open')
    file = ntpath.basename(filepath)
    t1.delete('1.0', END)
    t2.delete('1.0', END)
    if file.endswith('.wav'):
        t1.insert(END, file)
        fs, _ = wavfile.read(filepath)
        t2.insert(END, str(fs))
    else:
        t1.insert(END, 'Fisierul nu are extensia ".wav"')



def forma_unda():
    cale=pygame.mixer.music.load(play_list.get(tkr.ACTIVE))
    
    
    fs,data = wavfile.read(cale)
    data = max(abs(data))

    plt.figure('semnal')
    plt.plot(data)
    plt.show()
    
    
    
    #for cale in song_list:
                            #pygame.mixer.music.load(play_list.get(tkr.ACTIVE))
      #                      pos = 0
       #                     
        #                    fs,data = wavfile.read(cale)
         #                   data = max(abs(data))
    
          #                  plt.figure('semnal')
           #                 plt.plot(data)
            #                plt.show()
def play():
    pygame.mixer.music.load(play_list.get(tkr.ACTIVE))
    var.set(play_list.get(tkr.ACTIVE))
    pygame.mixer.music.play()
    
def stop():
    pygame.mixer.music.stop()
def pause():
    pygame.mixer.music.pause()
def unpause():
    pygame.mixer.music.unpause()
    
Button1 = tkr.Button(music_player, width=5, height=3, font='Helvetica 12 bold', text='PLAY', command=play, bg='blue', fg='white')
Button2 = tkr.Button(music_player, width=5, height=3, font='Helvetica 12 bold', text='STOP', command=stop, bg='red', fg='white')
Button3 = tkr.Button(music_player, width=5, height=3, font='Helvetica 12 bold', text='PAUSE', command=pause, bg='purple', fg='white')
Button4 = tkr.Button(music_player, width=5, height=3, font='Helvetica 12 bold', text='UNPAUSE', command=unpause, bg='orange', fg='white')
Button5 = tkr.Button(music_player, width=5, height=3, font='Helvetica 12 bold', text='Arata forma de unda', command=forma_unda, bg='green', fg='white')
Button6 = tkr.Button(music_player, width=5, height=3, font='Helvetica 12 bold', text='Deschide fisierul dorit', command=open_file, bg='brown', fg='white')

var = tkr.StringVar() 
song_title = tkr.Label(music_player, font='Helvetica 12 bold', textvariable=var)


song_title.pack()
Button1.pack(fill='x')
Button2.pack(fill='x')
Button3.pack(fill='x')
Button4.pack(fill='x')
Button5.pack(fill='x')
Button6.pack(fill='x')
play_list.pack(fill='both', expand='yes')
music_player.mainloop()


