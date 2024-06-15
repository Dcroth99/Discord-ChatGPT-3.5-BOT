import openai
import os
import discord
import asyncio
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

intents = discord.Intents.default()
client = discord.Client(intents=intents)

# Set up OpenAI API key
openai.api_key = "x-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

# Create an instance of the GPT-3 language model
gpt3_model = openai.Completion.create(
  engine="text-davinci-002",
  prompt="",
  temperature=0.5,
  max_tokens=500,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

# Function that will run in the background
async def background_task():
  while True:
    # Perform any background tasks here
    print("Running background task...")

    # Sleep for 10 seconds before running the next iteration
    await asyncio.sleep(10)

@client.event
async def on_ready():
  guild = client.guilds[0]

  
  permission_number = xxxxxxxxxxxxx

  # Get the "Chloe" role
  role = discord.utils.get(guild.roles, name="Homies")

  # Check if the role exists
  if role is not None:
    # Create a Permissions object with the new permissions
    new_permissions = discord.Permissions(permission_number)
    
    # Update the role's permissions
    await role.edit(permissions=new_permissions)
  channel = client.get_channel("general")
  if channel is not None:
    await channel.send("Hello! I am a Discord bot.")
  
  print('We have logged in as {0.user}'.format(client))
@client.event
async def on_message(message):
  if message.author == client.user:
    return
    
  if message.content.startswith("//Spotify"):
    # Get the track name from the user's message
    track_name = message.content.split(" ")[1]

    # Play the track in the voice channel
    await play_spotify_track(track_name, message.author.voice.channel)
  
  if message.author == client.user:
    return
  if message.content.startswith("//YouTube"):
    video_name = message.content.split(" ")[1]
    if message.guild is not None:
      video = discord.utils.get(message.guild.voice_channels, name=video_name)
      if video is not None:
        await video.connect()
        await video.play(discord.FFmpegPCMAudio(video_name))
      else:
        await message.channel.send("I'm sorry, I couldn't find a video with that name.")
    else:
      print("Error: the bot is not part of any Discord server (guild).")
  if message.content.startswith("//"):
    # Generate a response using the GPT-3 model
    response = openai.Completion.create(
      engine="text-davinci-002",
      prompt=message.content,
      temperature=0.5,
      max_tokens=500,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )
    await message.channel.send(response["choices"][0]["text"])
@client.event
async def on_friend_request(request):
  await request.accept()
  print(f"Accepted friend request from {request.user.name}")


client.run("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

