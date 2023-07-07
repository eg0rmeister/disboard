import src.bot_manager as bm
import src.sound_manager as sm
import asyncio
from pynput import keyboard
import random

class Callback:
  button = None
  def __call__(self, key):
    if (type(key) == keyboard.Key):
      print("\t", end='')
      key = key.value
    self.button = str(key.vk)

async def PlayRandom(discord_manager : bm.Interacter, sound_manager : sm.Sounder):
  if (not await discord_manager.ConnectToRandom()):
    return
  await discord_manager.PlaySound(sound_manager.GetRandomSound())
  await discord_manager.Disconnect()

async def SayHello(discord_manager : bm.Interacter, sound_manager : sm.Sounder):
  if (discord_manager.member_changed is not None):
    filename = sound_manager.CreateTTS("Шалом, " + discord_manager.member_changed.display_name)
    print("Шалом, " + discord_manager.member_changed.display_name)
    await discord_manager.ConnectTo(discord_manager.member_changed)
    await discord_manager.PlaySound(filename)
    await discord_manager.Disconnect()
    discord_manager.member_changed = None

async def main():
  sound_manager = sm.Sounder()
  discord_manager = bm.Interacter()
  await discord_manager.Connect()
  print("DEBUG")
  print("Established connection")
  discord_manager.FindFigula()
  print("Found My Master")
  while True:
    time_until_sfx = random.randint(10, 1200)
    print("eleven :", sound_manager.GetEleven())
    await PlayRandom(discord_manager, sound_manager)
    for _ in range(time_until_sfx):
      await SayHello(discord_manager, sound_manager)
      await asyncio.sleep(1)
    
    



asyncio.run(main())