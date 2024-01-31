from gtts import gTTS
from playsound import playsound
# import Play_mp3
# import os
# import winsound
text = "LOL this is really funny"
output = gTTS(text=text,lang='en',slow=False)
output.save('output01.mp3')
# output.save('outputEnterText.mp3')

#without the following playing commands no sound will be heard implementing this file
# os.system('mpg123'+'output_01.mp3')
# os.system("afplay output_01.mp3")#Mac: use itunes to play #import os
playsound('output01.mp3')#would err,filename cannot have any char #from playsound import playsound #playsound module is a crossplatform lib using utf-16, not depending on other lib, just pip install.
# playsound('outputEnterText.mp3')#from playsound import playsound #playsound module is a crossplatform lib using utf-16, not depending on other lib, just pip install.
# Play_mp3.play('output_01.mp3')#import Play_mp3 #this lib released in Oct2020

# filename="output_01.mp3"
# winsound.PlaySound(filename, winsound.SND_FILENAME)