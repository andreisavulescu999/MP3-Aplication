from pygame import mixer
from tkinter import *
import tkinter.font as font
from tkinter import filedialog

root=Tk()
root.title('Mp3 Player IOM')
mixer.init()

#creare lista care sa contina melodii
songs_list=Listbox(root,selectmode=SINGLE,bg="black",fg="green",font=('arial',15),height=12,width=47,selectbackground="gray",selectforeground="black")
songs_list.grid(columnspan=9)


def addsongs():
    #pentru a deschide fisierul  
    temp_song=filedialog.askopenfilenames(initialdir="Music/",title="Alege o melodie", filetypes=(("Fisiere mp3 ","*.mp3"),))
    ##bucla pentru a adauga toate melodiiile in lista
    for s in temp_song:
        s=s.replace("C:/Users/andac/Documents/Python Scripts/proiect_iom/music","")
        songs_list.insert(END,s)
     
def deletesong():
    curr_song=songs_list.curselection()
    songs_list.delete(curr_song[0])
    
    
def Play():
    song=songs_list.get(ACTIVE)
    mixer.music.load(song)
    mixer.music.play()

 
def Pause():
    mixer.music.pause()
 
def Stop():
    mixer.music.stop()
    #songs_list.selection_clear(ACTIVE)


def Resume():
    mixer.music.unpause()


def Previous():
    #pentru indexul melodiei selectate
    previous_one=songs_list.curselection()
    #pentru indexul melodiei de inainte
    previous_one=previous_one[0]-1
    #pentru a lua melodia anterioara
    temp2=songs_list.get(previous_one)
    mixer.music.load(temp2)
    mixer.music.play()
    songs_list.selection_clear(0,END)
    songs_list.activate(previous_one)
    songs_list.selection_set(previous_one)

def Next():
    #pentru indexul melodiei selectate
    next_one=songs_list.curselection()
    #pentru indexul umratoarei melodii
    next_one=next_one[0]+1
    #pentru urmatoarea melodie
    temp=songs_list.get(next_one)
    mixer.music.load(temp)
    mixer.music.play(loops=0)
    songs_list.selection_clear(0,END)
   
    songs_list.activate(next_one)
    songs_list.selection_set(next_one,last=None)

#font is defined which is to be used for the button font 
defined_font = font.Font(family='Verdana')

#play button
play_button=Button(root,text="Play",width =7,command= Play)
play_button['font']=defined_font
play_button.grid(row=1,column=0)

#pause button 
pause_button=Button(root,text="Pause",width =7,command=Pause)
pause_button['font']=defined_font
pause_button.grid(row=1,column=1)

#stop button
stop_button=Button(root,text="Stop",width =7,command=Stop)
stop_button['font']=defined_font
stop_button.grid(row=1,column=2)

#resume button
Resume_button=Button(root,text="Resume",width =7,command=Resume)
Resume_button['font']=defined_font
Resume_button.grid(row=1,column=3)

#previous button
previous_button=Button(root,text="Prev",width =7,command=Previous)
previous_button['font']=defined_font
previous_button.grid(row=1,column=4)

#nextbutton
next_button=Button(root,text="Next",width =7,command=Next)
next_button['font']=defined_font
next_button.grid(row=1,column=5)

#menu 
my_menu=Menu(root)
root.config(menu=my_menu)
add_song_menu=Menu(my_menu)
my_menu.add_cascade(label="Meniu",menu=add_song_menu)
add_song_menu.add_command(label="Adauga melodii",command=addsongs)
add_song_menu.add_command(label="Sterge melodia",command=deletesong)


mainloop()

