from discord import Member
from discord.ext import commands
from discord.ext.commands import Bot, Cog
from discord.ext.commands import Context
from src.methods import embed_msg
from datetime import datetime
import random


class SocialComands(Cog, name="Social"):
    def __init__(self, client: Bot):
        self.client = client  # sets the client variable so we can use it in cogs

    @commands.Cog.listener()
    async def on_ready(self) -> None:
        pass

    @commands.command()
    async def abracar(self, ctx: Context, user: Member = None):
        """Você abraça o usuário. Que Fofo <3."""

        if not user:
            response = "Ei!!!! :angry: \nNão dá pra abraçar fanstasma :ghost: ! Você precisa informar o usuário.\n\n `ex: abracar fulano`"
            await ctx.send(response)
            return

        _guild_id = ctx.guild.id
        title_header = ""
        icon_header: any
        title_content = ""
        desc_content = ""
        footer = ""

        for guild in self.client.guilds:
            if guild.id == _guild_id:
                title_header = guild.name
                icon_header = guild.icon

        frases = [
            "acaba de dar um abraço em",
            "fez cosplay de urso e deu um abraço apertado em",
            "não se aguentou e teve que abraçar",
        ]

        title_content = "Temporada de Abraços!"

        desc_content = (
            f"<@{ctx.message.author.id}> {random.choice(frases)} <@{user.id}>"
        )
        footer = f"Abraçou em {datetime.now().strftime('%d-%m-%Y')}"

        await ctx.send(
            embed=embed_msg(
                ctx,
                icon_header=icon_header,
                title_header=title_header,
                title_content=title_content,
                desc_content=desc_content,
                footer=footer,
            )
        )

    @abracar.error
    async def info_error(
        self, ctx: Context, error
    ):
        if isinstance(error, commands.BadArgument):
            await ctx.send(
                "AHA! :face_with_monocle:\nEsse caba não está no servidor!!!!! :angry:"
            )

    @commands.command()
    async def tapa(self, ctx: Context, user: Member = None):
        """Você dá um tapa no usuário. Chama pra porrada."""

        if not user:
            response = "Ei!!!! :angry: \nPra quê bater no fantasma :ghost:, cara!? Você precisa informar o usuário.\n\n `ex: tapa fulano`"
            await ctx.send(response)
            return

        _guild_id = ctx.guild.id
        title_header = ""
        icon_header: any
        title_content = ""
        desc_content = ""
        footer = ""

        for guild in self.client.guilds:
            if guild.id == _guild_id:
                title_header = guild.name
                icon_header = guild.icon

        frases = [
            "estapeou com vontade",
            "tirou as luvas e bateu com elas na cara de",
            "tomou distância e sentou o tapão em",
        ]

        title_content = "CAI NA PORRADA!"

        desc_content = (
            f"<@{ctx.message.author.id}> {random.choice(frases)} <@{user.id}>"
        )
        footer = f"Porrada em {datetime.now().strftime('%d-%m-%Y')}"

        await ctx.send(
            embed=embed_msg(
                ctx,
                icon_header=icon_header,
                title_header=title_header,
                title_content=title_content,
                desc_content=desc_content,
                footer=footer,
            )
        )

    @tapa.error
    async def info_error(
        self, ctx: Context, error
    ):
        if isinstance(error, commands.BadArgument):
            await ctx.send(
                "AHA! :face_with_monocle:\nEsse caba não está no servidor!!!!! :angry:"
            )


async def setup(bot: Bot):
    # Every extension should have this function
    await bot.add_cog(SocialComands(bot))
