# https://realpython.com/how-to-make-a-discord-bot-python/
# https://github.com/vadimkantorov/discordspeechtotext/blob/master/discord_speech_to_text_bot.py
# https://github.com/orgs/community/discussions/23395
# pip install -U discord.py
# pip install -U python-dotenv
# pip install -U discord.py[voice]
# pip install -U SpeechRecognition


# TO DO :
# - Ajouter une commande help dans main.py
# - Si ya plus personne dans le channel il faut se déconnecter 
# - Si le bot est move, il faut changer self.voice_channel

import os
import discord
from dotenv import load_dotenv
import GuildHandler

# VARIABLES D'ENVIRONNEMENT
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
COMMAND_CHANNEL = os.getenv('COMMAND_CHANNEL')

# CONNECTION BOT TO DISCORD (NOT TO ONE GUILD)
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    
    if message.author == client.user:
        return
    
    if message.content.lower() == '!join' and message.channel.name == COMMAND_CHANNEL:
        
        command_channel = message.channel
        voice_channel = message.author.voice.channel
        guild = message.guild
    
        if voice_channel:
            voice_client = await voice_channel.connect()
            print(f'Bot connected to voice channel: {voice_channel.name}')

            # Handle connection in one guild
            Guild = GuildHandler(command_channel, voice_channel, guild, client)
            Guild.listen_to_voice_channel()

        else:
            print(f'Voice channel not found')

    if message.content.lower() == '!quit' and message.channel.name == COMMAND_CHANNEL:
        
        voice_client = discord.utils.get(client.voice_clients, guild=message.guild)

        if voice_client:
            await voice_client.disconnect()
            print(f'Bot disconnected from voice channel: {voice_client.channel.name}')
        else:
            print(f'Bot is not connected to a voice channel.')

client.run(TOKEN)