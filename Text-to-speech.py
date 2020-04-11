#!/usr/bin/env python
# coding: utf-8

# In[78]:


#pip install gTTS




# It speech conversion is defined as Google-text-to-speech
from gtts import gTTS 

# os can play the converted audio 
import os 

# The text that you want to convert to audio by text

# mytext = 'Welcome to ext to speech converter in python'

# This function is used for read from text file

f = open("/home/100158/Python-Projects/Text-t0-speech/TextFile.txt","r")#world text file
string = f.read()
# it can convert into string
mytext = string.replace('\n', '')

#we can print function in output
print(mytext)

# Language in which you want to convert 
language = 'en'

# Passing the text and language to the engine, 
# here we have marked slow=False. Which tells 
# the module that the converted audio should 
# have a high speed 
myobj = gTTS(text=mytext, lang=language, slow=False) 

# Saving the converted audio in a mp3 file named 
# welcome 
myobj.save("/home/100158//Python-Projects/Text-t0-speech/output.mp3") 

# Playing the converted file 
os.system("output.mp3") 


# In[ ]:




