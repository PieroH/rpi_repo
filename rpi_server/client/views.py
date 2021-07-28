import os
from gtts import gTTS

from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    something = request.GET.get('thisPT_description', 'no message recived')
    tts = gTTS(text=something, lang='en')
    tts.save("audio.mp3")
    os.system("mpg321 -q audio.mp3")
    return HttpResponse(something)
# Create your views here.
