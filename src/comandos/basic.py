from discord import Member
from discord.ext import commands
from discord.ext.commands import Context
from src.methods import embed_msg
from datetime import datetime
import random


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

@commands.command()
async def decida(ctx: commands.Context, *choices: str):
    """Pede ao cão para decidir entre várias opções

    uso: decida <arg1> ou <arg2> ou ... ou <argN>

    Argumentos:
        - args: as opções a qual o Jotchua deve escolher
    """

    if not choices:
        await ctx.send("Temq colocar algo ne")
        return

    choices_list = []
    frase = ""
    for c in choices:
        if c != 'ou':
            frase += f"{c} "
        else:
            choices_list.append(frase)
            frase = ""

    print(frase)
    choices_list.append(frase)
    result = f"Eu escolho acho que\n**{random.choice(choices_list)}** "
    await ctx.send(result)

@commands.command()
async def repita(ctx: commands.Context, times, *content: str):
    """Repete uma mensagem várias vezes, max 10 vezes

    uso: repita <nro de vezes> <mensagem>

    Argumentos:
        - nro de vezes: Total de vezes que a mensagem será repetida
        - mensagem: a mensagem a ser repetida
    """

    try:
        times = int(times)
        if times > 10:
            times = 10
    except ValueError:
        response = "nro vezes inválido :dizzy_face:\nO número de vezes deve ser um valor inteiro maior que 0\n\n EX:`repita 2 quero caféééé`"
        await ctx.send(response)
        return

    if times is None or times < 1:
        response = "Não dá pra repetir 0 vezes! :rage:\nBote um valor pra eu repetir\n\n EX:`repita 2 quero caféééé`"
        await ctx.send(response)
        return
    
    if not content:
        response = "Não sei o que é para repetir! :face_with_raised_eyebrow:\nDiga o que é pra repetir\n\n EX:`repita 2 quero caféééé`"
        await ctx.send(response)
        return

    frase = ""
    for c in content:
        frase += f"{c} "

    for i in range(times):
        await ctx.send(frase)
    await ctx.send(f"Disse: <@{ctx.message.author.id}>")

@commands.command()
async def dado(ctx: commands.Context, dice: str = None):
    """Joga um dado dY, x vezes

    uso: dado <x>d<Y>
    ex: dado 2d10
        resultado: 2, 6

    Argumentos:
        - x: quantidade de dados
        - Y: valor do dado
    """
    
    rolls: int = 1
    size: int = 6
    result = "Eu lancei um dado"
    if dice is not None:
        rolls, size = map(int, dice.split('d'))
        result = f"{result} {rolls}d{size} :game_die:\n"
    else:
        result = f"{result} 1d6 :game_die:\n"

    print(result)
    for i in range(rolls):
        result += f"Lançamento {i}: **{str(random.randint(1, size))}**.\n"
    await ctx.send(result)

async def setup(bot: commands.Bot):
    # Every extension should have this function
    bot.add_command(membros)
    bot.add_command(info)
    bot.add_command(decida)
    bot.add_command(repita)
    bot.add_command(dado)