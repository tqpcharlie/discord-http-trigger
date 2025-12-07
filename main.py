import functions_framework
import flask
import discord
import dotenv
import os


class gcpGateway(discord.Client):
    # Suppress error on the User attribute being None since it fills up later
    user: discord.ClientUser

    botToken = os.getenv('botToken')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.trigger_message_id = 1447049952554389626  # ID of the message that can be reacted to to add/remove a role.
        self.emoji_trigger = {
            discord.PartialEmoji(name='U+26CF')
        }

    async def on_reaction_add(self, payload: discord.MessageReactionAddEvent):
        # Make sure that the message the user is reacting to is the one we care about.
        if payload.message_id != self.trigger_message_id:
            return

        # Check if we're still in the guild and it's cached. Commented out unless otherwise needed
        #guild = self.get_guild(payload.guild_id)
        #if guild is None:
            #return

        try:
            role_id = self.emoji_trigger[payload.emoji]
        except KeyError:
            # If the emoji isn't the one we care about then exit as well.
            return



        # Register an HTTP function with the Functions Framework
        @functions_framework.http
        def make_request(request):
            import requests

            print('f')
            # Return an HTTP response
        return 'OK'

intents.Reactions = True
# Runs client (w/gateway)
client = gcpGateway(intents=intents)
client.run(botToken)