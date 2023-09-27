import discord
from discord.ext import commands
from discord.ext.commands import Context
from src.methods import embed_msg


@commands.command()
async def membros(ctx: Context):
    """Exibe uma listagem dos membros deste servidor."""

    string_member = ""
    bot: commands.Bot = ctx.bot
    id = ctx.message.guild.id
    for guild in bot.guilds:
        if guild.id == id:
            title_header = guild.name
            icon_header = guild.icon
            title_content = "Membros deste servidor: "
            for member in guild.members:
                string_member += f"\n{member}"

    desc_content = string_member
    footer = f"Perguntado por {ctx.author}"

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

async def setup(bot: commands.Bot):
    # Every extension should have this function
    bot.add_command(membros)