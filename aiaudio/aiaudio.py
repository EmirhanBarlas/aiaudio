from gtts import gTTS
import os
from os import path
ses = "aises"

def dosyaokey(dosya):
    return path.exists(dosya)

dosya = open(f"{ses}.txt", encoding="utf-8")
yaz = dosya.read()
out = gTTS(text=yaz, lang='tr',slow=False)
if dosyaokey(f"{ses}.mp3"):
    print("Seslendiriliyor...")
    os.system(f"{ses}.mp3")
else:
    print("Dosyanız oluşturuluyor")
    out.save(f"{ses}.mp3")
    print("Seslendiriliyor...")
    os.system(f"{ses}.mp3")
dosya.close()