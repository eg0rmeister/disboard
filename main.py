import src.bot_manager as bm
import src.sound_manager as sm
import asyncio
from pynput import keyboard

class Callback:
  button = None
  def __call__(self, key):
    if (type(key) == keyboard.Key):
      print("\t", end='')
      key = key.value
    self.button = str(key.vk)

async def main():
  sound_manager = sm.Sounder()
  discord_manager = bm.Interacter()
  await discord_manager.Connect()
  print("Established connection")
  discord_manager.FindFigula()
  print("Found Master")
  await discord_manager.SendMessage()
  await discord_manager.ConnectToFigula()
  print("Connected to master")
  try:
    callback = Callback()
    # keyboard.hook(callback)
    # await discord_manager.PlaySound(sound_manager.GetSound('start'))

    listener = keyboard.Listener(on_press=callback)
    listener.start()
    while True:
      
      if (callback.button is not None):
        print(callback.button)
        if (sound_manager.Contains(callback.button)):
          await discord_manager.PlaySound(sound_manager.GetSound(callback.button))
        callback.button = None
      await asyncio.sleep(0.1)
  except Exception as traceback:
    print(type(traceback), traceback)
    await discord_manager.Disconnect()
  except:
    await discord_manager.Disconnect()
    
'''
  Keyboard Keys Lookup
  Numpad 1 = 97
  Numpad 2 = 98
  Numpad 3 = 99
  Numpad 4 = 100
  Numpad 5 = 101
  Numpad 6 = 102
  Numpad 7 = 103
  Numpad 8 = 104
  Numpad 9 = 105
'''


asyncio.run(main())