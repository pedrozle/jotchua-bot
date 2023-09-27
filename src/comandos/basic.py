from discord import Member
from discord.ext import commands
from discord.ext.commands import Context
from src.methods import embed_msg
from datetime import datetime


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

@commands.command()
async def info(ctx: commands.Context, user: Member = None):
    """Exibe informações sobre você ou sobre um usuário especificado

    uso: info <nada | apelido>

    Argumentos:
        - nada: Exibe informações sobre o seu usuário
        - apelido: Exibe informações sobre o usuário com aquele apelido
    """

    if user is None:
        user = ctx.message.author

    title_header = f"Informações sobre {user.name}"
    title_content = user.name
    avatar = user.display_avatar.url
    joined_at = user.joined_at.replace(tzinfo=None)
    diff = datetime.now() - joined_at
    desc = f"Entrou no servidor há {diff.days} dias!"
    footer = f"Perguntado por {ctx.message.author}"
    await ctx.send(embed=embed_msg(ctx, title_header=title_header, title_content=title_content, desc_content=desc, img_content=avatar, footer=footer))


async def setup(bot: commands.Bot):
    # Every extension should have this function
    bot.add_command(membros)
    bot.add_command(info)