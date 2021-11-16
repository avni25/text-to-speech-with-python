from gtts import gTTS
from playsound import playsound
from texts import texts


# etxt speech icin pip install gTTS   
# pip install playsound==1.2.2 sonrasinda kodu yaz
# playsound son versiyonunda hata veriyor. kod calismiyor.


text = texts[1]

tts = gTTS(text, tld='co.uk')
tts.save("hi.mp3")

playsound('hi.mp3')





