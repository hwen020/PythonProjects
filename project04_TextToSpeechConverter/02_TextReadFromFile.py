from gtts import gTTS
from playsound import playsound
text = open('file02.txt','r').read()
language = 'en'#search'google speech language codes'
output = gTTS(text=text,lang=language,slow=False)
output.save('output02.mp3')
playsound('output02.mp3')#if named'fileoutput02'would err #from playsound import playsound #playsound module is a crossplatform lib, not depending on other lib, just pip install.
# play_mp3.play('output.mp3')#import Play_mp3 #this lib released in Oct2020
# os.system("afplay output.mp3")#Mac: use itunes to play #import os

# #it went wrong when I tried another language
# text = open('file02ch.txt', 'rb').read()
# # language = 'zh (cmn-Hans-CN)'
# language = 'zh'
# output = gTTS(text=text, lang=language, slow=False)
# output.save('output02ch.mp3')
# playsound('output02ch.mp3')