# bot.py
import os

import discord
import dotenv
import asyncio
import random

from collections.abc import Sequence

class Interacter:
  client : discord.Client = None
  online : bool = False
  master_id : int = None
  master_vc = None
  vc = None
  member_changed : discord.Member = None

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
      if (before.channel != after.channel and after.channel is not None and member.id != self.client.user.id):
        # print(after)
        print("__")
        print(member)
        print("--")
        self.member_changed = member

    await self.client.login(token)
    asyncio.create_task(self.client.connect(reconnect=False))
    while (not self.online):
      await asyncio.sleep(0.5)

  async def SendMessage(self):
    message = "hello"
    chat = await self.client.create_dm(self.client.get_user(self.master_id))
    await chat.send(message)
    return
  
  def FindFigula(self):
    for member in self.client.get_all_members():
      if (member.id == self.master_id and member.voice is not None):
        self.master_vc = member.voice.channel
        return

  async def ConnectToMaster(self):
    self.vc = await self.master_vc.connect()

  async def ConnectTo(self, member : discord.Member):
    self.vc = await member.voice.channel.connect()

  async def PlaySound(self, filename: str):
    if (self.vc.is_playing()):
      self.vc.stop()
    print(filename)
    self.vc.play(discord.FFmpegPCMAudio(filename, executable="C:\\Users\\egor\\Documents\\Essentials\\ffmpeg\\bin\\ffmpeg.exe"))
    while (self.vc.is_playing()):
      await asyncio.sleep(0.1)
  
  async def Disconnect(self):
    await self.vc.disconnect()

  async def ConnectToRandom(self):
    channels = set()
    for member in self.client.get_all_members():
      if (member.voice is not None):
        channels.add(member.voice.channel)
    if (len(channels) == 0):
      return False
    channel : discord.channel.VocalGuildChannel = random.choice([_ for _ in channels])
    self.vc = await channel.connect()
    return True