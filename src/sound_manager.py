import json
import pyttsx3
import random

SOUNDS_DIR = "assets/sounds/"
SOUNDS_DICT_NAME = "dict.json"
TTS_DIR = "assets/TTSSound/"
TTS_FILENAME = "tts.mp3"

class Sounder:
  sounds : dict = {}
  tts_engine : pyttsx3.Engine = None
  #TODO: implement real init
  def __init__(self):
    self._init_tts()
    self._read_json()

  def _read_json(self):
    with open(SOUNDS_DIR + SOUNDS_DICT_NAME, "rb") as file:
      sounds = json.load(file)
    for entry in sounds:
      self.sounds[entry] = SOUNDS_DIR + sounds[entry]
    print(self.sounds)

  def _init_tts(self):
    self.tts_engine = pyttsx3.init()

    self.tts_engine.setProperty('rate', 150)
    self.tts_engine.setProperty('voice', 'ru') 

  def GetSound(self, name: str):
    return self.sounds[name]

  def GetRandomSound(self):
    return self.GetSound(random.choice([_ for _ in self.sounds.keys()]))
  
  def Contains(self, name: str):
    return name in self.sounds.keys()
  
  def CreateTTS(self, string: str):
    self.tts_engine.save_to_file(string, TTS_DIR + TTS_FILENAME)
    self.tts_engine.runAndWait()
    return TTS_DIR + TTS_FILENAME
  
  def GetEleven(self):
    return self.GetSound('eleven')
  