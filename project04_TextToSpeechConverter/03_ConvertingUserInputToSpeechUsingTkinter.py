from gtts import gTTS
from playsound import playsound
from tkinter import *

root=Tk()
root.title("Converting Input Text to Speech")
canvas=Canvas(root,width=400,height=300)
canvas.pack()

def textToSpeech():
    text=entry.get()
    language='en'
    output=gTTS(text=text,lang=language,slow=False)
    output.save('output03.mp3')
    playsound('output03.mp3')

entry=Entry(root)
canvas.create_window(200,180,window=entry)

button=Button(text="Start Converting to Speech",command=textToSpeech)
canvas.create_window(200,230,window=button)

root.mainloop()#without this there'd be no window


# #the ver without button, window only
# from tkinter import *
#
# root=Tk()
# root.title("Converting Input Text to Speech")
# canvas=Canvas(root,width=400,height=300)
# canvas.pack()
#
# entry=Entry(root)
# canvas.create_window(200,180,window=entry)
#
# root.mainloop()#without this there'd be no window