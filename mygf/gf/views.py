from django.shortcuts import render
from playsound import playsound
from gtts import gTTS
import os
from django.contrib import messages
def girlfriend(request):
    if request.method == "POST":
        text=request.POST.get('text')
        mytext = text
        language = 'en'
        myobj = gTTS(text=mytext + "   Thanks for using me I love you . If you want to say anything else you can type here . ", lang=language, slow=False)
        myobj.save("text.mp3")
        playsound("text.mp3")
        os.remove("text.mp3")
        return render(request, 'index.html')
    else:
        pass
    return render(request, 'index.html')
