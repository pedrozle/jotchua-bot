from discord import Member
from discord.ext import commands
from discord import app_commands, Interaction
from discord.ext.commands import Bot, Cog
from src.methods import embed_msg
from datetime import datetime
import random
import requests


class SocialComands(Cog, name="Social"):
    def __init__(self, client: Bot):
        self.client = client  # sets the client variable so we can use it in cogs

    @commands.Cog.listener()
    async def on_ready(self) -> None:
        pass

    @app_commands.command()
    async def abracar(self, interaction: Interaction, user: Member = None):
        """Você abraça o usuário. Que Fofo <3."""

        if not user:
            response = "Ei!!!! :angry: \nNão dá pra abraçar fanstasma :ghost: ! Você precisa informar o usuário.\n\n `ex: abracar fulano`"
            await interaction.response.send_message(response)
            return

        _guild = interaction.guild
        title_header = _guild.name
        icon_header = _guild.icon
        title_content = ""
        desc_content = ""
        footer = ""

        frases = [
            "acaba de dar um abraço em",
            "fez cosplay de urso e deu um abraço apertado em",
            "não se aguentou e teve que abraçar",
        ]

        title_content = "Temporada de Abraços!"

        desc_content = f"<@{interaction.user.id}> {random.choice(frases)} <@{user.id}>"
        footer = f"Abraçou em {datetime.now().strftime('%d-%m-%Y')}"

        req = requests.get("https://api.waifu.pics/sfw/hug")
        img_url = ""

        if req.status_code == 200:
            img_url = req.json()["url"]

        embed = embed_msg(
            icon_header=icon_header,
            title_header=title_header,
            title_content=title_content,
            desc_content=desc_content,
            footer=footer,
        )

        embed.set_image(url=img_url)

        await interaction.response.send_message(embed=embed)

    @app_commands.command()
    async def tapa(self, interaction: Interaction, user: Member = None):
        """Você dá um tapa no usuário. Chama pra porrada."""

        if not user:
            response = "Ei!!!! :angry: \nPra quê bater no fantasma :ghost:, cara!? Você precisa informar o usuário.\n\n `ex: tapa fulano`"
            await interaction.response.send_message(response)
            return

        _guild = interaction.guild
        title_header = _guild.name
        icon_header = _guild.icon
        title_content = ""
        desc_content = ""
        footer = ""

        frases = [
            "estapeou com vontade",
            "tirou as luvas e bateu com elas na cara de",
            "tomou distância e sentou o tapão em",
        ]

        title_content = "CAI NA PORRADA!"

        desc_content = f"<@{interaction.user.id}> {random.choice(frases)} <@{user.id}>"
        footer = f"Porrada em {datetime.now().strftime('%d-%m-%Y')}"

        req = requests.get("https://api.waifu.pics/sfw/slap")
        img_url = ""

        if req.status_code == 200:
            img_url = req.json()["url"]

        embed = embed_msg(
            icon_header=icon_header,
            title_header=title_header,
            title_content=title_content,
            desc_content=desc_content,
            footer=footer,
        )

        embed.set_image(url=img_url)

        await interaction.response.send_message(embed=embed)


async def setup(bot: Bot):
    # Every extension should have this function
    await bot.add_cog(SocialComands(bot))
