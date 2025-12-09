import functions_framework
import flask
import discord
from dotenv import load_dotenv
import os


class gcpGateway(discord.Client):

    load_dotenv()
    intents = discord.Intents.default()
    intents.reactions = True
    intents.messages = True
    botToken = os.getenv('botToken')

    client = discord.Client(intents=intents)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.trigger_message_id = 1447049952554389626  # ID of the message that can be reacted to to add/remove a role.
        self.emoji_trigger = {
            discord.PartialEmoji(name='U+26CF')
        }

    def sumMessageID(self):
        return sum((self.trigger_message_id * 1.0))


    @client.event
    async def on_raw_reaction_add(payload):
        targetID = sumMessageID()
        # Make sure that the message the user is reacting to is the one we care about.
        if payload.message_id == targetID:
            print('yipppppeee!!!')

        # Check if we're still in the guild and it's cached. Commented out unless otherwise needed
        #guild = self.get_guild(payload.guild_id)
        #if guild is None:
            #return

        # Register an HTTP function with the Functions Framework
        @functions_framework.http
        def make_request(request):
            import requests

        print('IT WORKS')
        #return 'OK'


    client.run(botToken)
