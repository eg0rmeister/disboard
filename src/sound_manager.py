import json

SOUNDS_DIR = "assets/sounds/"
SOUNDS_DICT_NAME = "dict.json"

class Sounder:
  sounds : dict = {}
  #TODO: implement real init
  def __init__(self):
    with open(SOUNDS_DIR + SOUNDS_DICT_NAME, "rb") as file:
      sounds = json.load(file)
    for entry in sounds:
      print(entry)
      self.sounds[entry] = SOUNDS_DIR + sounds[entry]
    print(self.sounds)
  

  def GetSound(self, name: str):
    return self.sounds[name]
  
  