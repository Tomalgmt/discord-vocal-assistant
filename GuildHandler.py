import discord
import speech_recognition as sr

class GuildHandler:
    
    def __init__(self, command_channel, voice_channel, guild, client):
        self.command_channel = command_channel
        self.voice_channel = voice_channel
        self.guild = guild
        self.client = client
    
    def listen_to_voice_channel(self):
        pass # boucle while probablement

    def send_message(self):
        pass