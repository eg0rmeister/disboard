# bot.py
import os

import discord
import dotenv
import asyncio

class Interacter:
  client = None
  online = False
  master_id = None
  main_task = None
  master_vc = None
  vc = None

  async def Connect(self):

    # Load and assign environment variables
    dotenv.load_dotenv()
    token = os.getenv("DISCORD_TOKEN")[1:-1]
    self.master_id = int(os.getenv("MY_MASTER_ID")[1:-1])

    # Create client objects with all intents
    intent = discord.Intents.all()
    self.client = discord.Client(intents=intent)
    
    # Start client and wait until it is started
    @self.client.event
    async def on_ready():
      self.online = True
    
    @self.client.event
    async def on_voice_state_update(member : discord.Member, before : discord.VoiceState, after : discord.VoiceState):
      print('\a')

    await self.client.login(token)
    self.main_task = asyncio.ensure_future(self.client.connect(reconnect=False))
    while (not self.online):
      await asyncio.sleep(0.5)

  async def SendMessage(self):
    message = "hello"
    chat = await self.client.create_dm(self.client.get_user(self.master_id))
    await chat.send(message)
    return
  
  def FindFigula(self):
    for guild in self.client.guilds:
      for member in guild.members:
        if (member.id == self.master_id and member.voice is not None):
          self.master_vc = member.voice
          return

  async def ConnectToFigula(self):
    self.vc = await self.master_vc.channel.connect()

  async def PlaySound(self, filename: str):
    
    if (not self.vc.is_connected()):
      await self.ConnectToFigula()
    if (self.vc.is_playing()):
      self.vc.stop()
    print(filename)
    self.vc.play(discord.FFmpegPCMAudio(filename, executable="C:\\Users\\egor\\Documents\\Essentials\\ffmpeg\\bin\\ffmpeg.exe"))
  
  async def Disconnect(self):
    await self.vc.disconnect()