# first you need to install gtts by using (pip using gtts) command
from gtts import gTTS #i have imported this module for text to audio speech conversation
import os

text = "Hello, I am shawon. I am a python developer and also full stack web developer" #text that i want to convert
language = 'en' #en is for english language
obj = gTTS(text=text, lang=language, slow=False) #I have used slow=False because my converted audio will have a high speed
obj.save("sample.mp3")
'''
#if you want from file that you can change this to audio speech
abc = open("filename.txt")
text = abc.read()
language = 'en' #en is for english language
obj = gTTS(text=text, lang=language, slow=False) #I have used slow=False because my converted audio will have a high speed
obj.save("sample.mp3")
'''
#to open audio file automatically i have to import os
os.system("sample.mp3")