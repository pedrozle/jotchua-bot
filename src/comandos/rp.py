from discord import Member
from discord.ext import commands
from discord import app_commands, Interaction
from discord.ext.commands import Bot, Cog
from src.methods import embed_msg
from datetime import datetime
import random

from src.db.database import db_instance

class RPCommands(Cog, name="Role Play"):
    def __init__(self, client: Bot):
        self.client = client  # sets the client variable so we can use it in cogs

    @commands.Cog.listener()
    async def on_ready(self) -> None:
        pass

    @app_commands.command()
    async def rank(self, interaction: Interaction):
        """Exibe a lista de usuários no servidor e a pontuação de cada um."""

        collection = db_instance.get_collection(str(interaction.guild.id))
        users = collection.find()

        users = sorted(users, key=lambda k: k["xp"], reverse=True)

        title_header = interaction.guild.name
        icon_header = interaction.guild.icon
        title_content = ":crown: Placar de Líderes :crown:"
        desc_content = "Estes são os usuários que mais contribuíram para o servidor."
        footer = f"Perguntado por {interaction.user.name}"
        
        first = ":first_place:"
        second = ":second_place:"
        third = ":third_place:"
        
        desc_content += f"\n{first} {users[0]['username']} - {users[0]['xp']} pontos - lvl {users[0]['level']}"
        desc_content += f"\n{second} {users[1]['username']} - {users[1]['xp']} pontos - lvl {users[1]['level']}"  
        desc_content += f"\n{third} {users[2]['username']} - {users[2]['xp']} pontos - lvl {users[2]['level']}"
        for pos, user in enumerate(users):
            if pos > 2:
                desc_content += f"\n{user['username']} - {user['xp']} pontos - lvl {user['level']}"
        
        embed = embed_msg(
            icon_header=icon_header,
            title_header=title_header,
            title_content=title_content,
            desc_content=desc_content,
            footer=footer,
        )
        await interaction.response.send_message(embed=embed)

async def setup(bot: Bot):
    # Every extension should have this function
    await bot.add_cog(RPCommands(bot))
