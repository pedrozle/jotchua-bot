from discord import Member
from discord.ext import commands
from discord import app_commands, Interaction
from discord.ext.commands import Bot, Cog
from src.methods import embed_msg
from datetime import datetime
import random


class RPCommands(Cog, name="Role Play"):
    def __init__(self, client: Bot):
        self.client = client  # sets the client variable so we can use it in cogs

    @commands.Cog.listener()
    async def on_ready(self) -> None:
        pass

    # @app_commands.command()
    # async def abracar(self, interaction: Interaction, user: Member = None):
    #     """Você abraça o usuário. Que Fofo <3."""