# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 20:52:04 2022

@author: andac
"""
#pip install mutagen
from tkinter import *
import pygame
import time
from mutagen.mp3 import MP3
from tkinter import filedialog

root = Tk()
root.title('Proiect IOM')
root.geometry('1500x600')

pygame.mixer.init()


#luam durata music
def play_time():
    current_time = pygame.mixer.music.get_pos() /1000
    
    converted_current_time = time.strftime('%M:%S',time.gmtime(current_time))
    

    #luam titlul muzicii
    song = song_box.get(ACTIVE) 
    
    song = f'E:/Facultate Poli/Anul IV/Sem I/IOM/Laburi/proiect_iom/{song}.mp3'    
    #luam durata muzicii mutagen   
    song_mut = MP3(song)
    song_lenght = song_mut.info.lenght

    
    converted_song_lenght = time.strftime('%M:%S',time.gmtime(song_lenght))
    status_bar.config(text=f'Time Elapsed:  {converted_current_time}   of   {converted_song_lenght}')
    #update time
    status_bar.after(1000, play_time)
#adaugare muzica
def add_song():
    song = filedialog.askopenfilename(intialdir='', title='choose a song',filetypes = (("mp3 Files","*.mp3")))
    #inlocuim numele fisierului 
    song = song.replace("E:/Facultate Poli/Anul IV/Sem I/IOM/Laburi/proiect_iom/music/","")
    song = song.replace(".mp3","")
    
    song_box.insert(END, song)
    
#add many songs    
def add_many_songs() :
    songs = filedialog.askopenfilenames(intialdir='', title='choose a song',filetypes = (("mp3 Files","*.mp3"),  ))
    
    for song in songs:
        #Loop pentru a inlocui path
        song = song.replace("E:/Facultate Poli/Anul IV/Sem I/IOM/Laburi/proiect_iom/music/","")
        song = song.replace(".mp3", "")
    
        song_box.insert(END, song)

#play muzica    
def play() :
    song = song_box.get(ACTIVE)
    song = f'E:/Facultate Poli/Anul IV/Sem I/IOM/Laburi/proiect_iom/music/{song}'.mp3
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)   
    #chemam play_time aici
    
#stop muzica 
def stop() :
     pygame.mixer.music.stop()
     song_box.selection_clear(ACTIVE)  #numai ramane muzica selectata cu gry
     
     #clear status bar
     status_bar.config(text='') 
     
#play next song
def next_song():
    next_song = song_box.curselection()  #returneaza indicele din lista a music curente
    #adaugam unu la muzica curenta
    next_song = next_one[0]+1 
    #luam titlul muzicii
    song = song_box.get(next_song) 
    
    song = f'E:/Facultate Poli/Anul IV/Sem I/IOM/Laburi/proiect_iom/music/{song}.mp3'

    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)   

    #le deselecteaza pe toate 
    song_box.selection_clear(0,END)
    #mutam active
    song_box.activate(next_one)
    #set activate bar to next song
    song_box.selection_set(next_one,last=None)
    
def previous_song():
    next_song = song_box.curselection()  #returneaza indicele din lista a music curente
    #adaugam unu la muzica curenta
    next_song = next_one[0]-1 
    #luam titlul muzicii
    song = song_box.get(next_song) 
    
    song = f'E:/Facultate Poli/Anul IV/Sem I/IOM/Laburi/proiect_iom/music/{song}.mp3'

    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)   

    #le deselecteaza pe toate 
    song_box.selection_clear(0,END)
    #mutam active
    song_box.activate(next_one)
    #set activate bar to next song
    song_box.selection_set(next_one,last=None)
#cream o variabila globala pentru a vedea daca muzica este oprita sau nu
global paused
paused = False

def pause(is_paused) :
     global paused
     paused = is_paused
     
     if paused:
         #unpause
         pygame.mixer.music.unpause()
         paused = False
     else:
         #pause
         pygame.mixer.music.pause()
         paused = True
     
     song_box.selection_clear(ACTIVE)  #numai ramane muzica selectata cu gry
def delete_song():
    song_box.delete(ANCHOR)
    pygame.mixer.music.stop()
    
def delete_all_songs():
    song_box.delete(0,END)
    pygame.mixer.music.stop()
    
def upload():
    pass
#creare playlist
song_box = Listbox(root, bg="black", fg='green', width=200, selectbackground="gray",selectforeground="black")
song_box.pack(pady=20)

#creare imagini butoane player
back_btn_img = PhotoImage(file='buttons/backward.png')
foward_btn_img = PhotoImage(file='buttons/forward.png')
play_btn_img = PhotoImage(file='buttons/play.png')
pause_btn_img = PhotoImage(file='buttons/pause.png')
stop_btn_img = PhotoImage(file='buttons/stop.png')
upload_img = PhotoImage(file='buttons/upload.png')

#creare frame
controls_frame = Frame(root)
controls_frame.pack()

#creare butone control player

back_button =Button(controls_frame,image=back_btn_img ,borderwidth =0,command = previous_song)
forward_button =Button(controls_frame,image=foward_btn_img ,borderwidth =0, command = next_song)
play_button = Button(controls_frame,image=play_btn_img ,borderwidth =0 ,command = play)
pause_button =Button(controls_frame,image=pause_btn_img ,borderwidth =0,command = lambda:pause(paused))
stop_button =Button(controls_frame,image=stop_btn_img ,borderwidth =0,command = stop)
upload_button =Button(controls_frame,image=upload_img ,borderwidth =0,command = upload)

back_button.grid(row=0, column=0 , padx=10)
forward_button.grid(row=0, column=1,padx=10)
play_button.grid(row=0, column=2 ,padx=10)
pause_button.grid(row=0, column=3 ,padx=10)
stop_button.grid(row=0, column=4,padx=10)
upload_button.grid(row=0, column=5,padx=10)

#creare meniu
my_menu = Menu(root)
root.config(menu=my_menu)


#adaugare muzica in meniu
add_song_menu=Menu(my_menu)
my_menu.add_cascade(label = "Add song",menu = add_song_menu)
add_song_menu.add_command(label='Add one song to playlist',command=add_song)

#add many songs
add_song_menu.add_command(label='Add many song to playlist',command=add_many_songs)

#create delete song menu
remove_song_menu = Menu(my_menu)
my_menu.add_cascade(label = "Remove song",menu = remove_song_menu)
remove_song_menu.add_command(label='Delete a song from playlist',command= delete_song)
remove_song_menu.add_command(label='Delete all songs from playlist',command= delete_all_songs)

#status bar
#status_bar = Label(root, text='',bd=1,relief=GROOVE,anchor=E)
#satus_bar_pack(fill=X,side=BOTTOM,ipady=2)

root.mainloop()
