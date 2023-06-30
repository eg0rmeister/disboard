import src.bot_manager as bm
import src.sound_manager as sm
import asyncio

async def main():
  sound_manager = sm.Sounder()
  discord_manager = bm.Interacter()
  await discord_manager.Update()
  print("Established connection")
  await discord_manager.SendMessage()
  print("Sent message to Master")
  discord_manager.FindFigula()
  print("Found Master in", discord_manager.master_vc.channel.name)
  await discord_manager.ConnectToFigula()
  print("Connected to master")
  try:
    await discord_manager.PlaySound(sound_manager.GetSound('NumPad2'))
    while True:
      await asyncio.sleep(10)
  except Exception as traceback:
    print(traceback)
    await discord_manager.Disconnect()
  except:
    await discord_manager.Disconnect()

asyncio.run(main())