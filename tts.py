from gtts import gTTS
import os
cwd = os.getcwd()

class Tts:
    def __init__(self, utctime,ttext,type,instanceid):
        tts = gTTS(ttext, lang='en',slow=False)
        tts.save(cwd+'/data/audio/'+instanceid+type+'.mp3')