import discord, random
from discord.ext import commands
from classes.user import User
import sys

sys.path.insert(1, "/path/to/application/app/folder")
from methods import transacao, getid, embed_msg, user_list, find_user


@commands.command()
async def placar(ctx):
    """Exibe a lista de usuários no servidor e exibe o saldo total deles, ranqueados pelo saldo."""

    users = ""
    # sorted_list = [user_list[x.id] for x in ctx.guild.members]
    server_users = user_list[str(ctx.guild.id)]
    sorted_list = list(server_users.values())
    sorted_list.sort(key=lambda x: x.balance + x.bank, reverse=True)

    users += "\n".join(
        f"**{index+1}.** {user.name} - :dollar: {user.balance + user.bank}"
        for index, user in enumerate(sorted_list)
    )
    await ctx.send(
        embed=embed_msg(
            ctx, ctx.guild.icon.url, ctx.guild.name, "Placar dor Milionários", users
        )
    )


@commands.command()
async def saldo(ctx):
    """Exibe o seu saldo atual! Quanto você tem na mão e no banco."""

    user_id = str(ctx.message.author.id)

    user = find_user(user_id, str(ctx.guild.id))

    await ctx.send(
        embed=embed_msg(
            ctx,
            icon_header=ctx.author.display_avatar,
            title_header=ctx.author,
            title_content="Saldo",
            desc_content=user.saldo(),
        )
    )


@commands.command()
async def rank(ctx, member: discord.Member = None):
    """Exibe o seu status no servidor."""

    server_users = user_list[str(ctx.guild.id)]
    sorted_list = list(server_users.values())
    sorted_list.sort(key=lambda x: x.xp, reverse=True)

    if not member:
        member = ctx.author
    userAlvo = find_user(str(member.id), str(ctx.guild.id))
    await ctx.send(
        embed=embed_msg(
            ctx,
            icon_header=member.display_avatar,
            title_header=member,
            title_content=f"Rank #{sorted_list.index(userAlvo) + 1}",
            desc_content=f"Lvl: {userAlvo.get_lvl()}\nExp: {userAlvo.get_xp()}",
        )
    )


@commands.command()
async def trabalhar(ctx):
    """Você sai a trabalho e recebe um salário!."""

    user_id = str(ctx.message.author.id)
    username = ctx.message.author.name
    work_list = {
        "A": random.randint(20, 60) * -1,
        "B": random.randint(20, 60),
        "C": random.randint(30, 90),
        "D": random.randint(20, 30),
    }
    work_weight = (
        ["C"] * 15 + ["A"] * 25 + ["B"] * 80 + ["D"] * 30
    )  # atribui pessos as variaveis

    # string = f'{random.choice(worl_weight)}'
    choice = random.choice(work_weight)
    value = work_list[choice]
    emoji = ":money_with_wings:"
    resp = ""

    response_text = {
        "A": f"<@{user_id}> Jogou pastel no cliente e foi multado em {emoji}**{value}**",
        "B": f"<@{user_id}> Em mais um dia de trabalho arduo e ganhou {emoji}**{value}**",
        "C": f" <@{user_id}> No fim do expediente um cliente te deu gorjeta com isso ganhou {emoji}**{value}**",
        "D": f" <@{user_id}> Esqueceu de bater o ponto e recebeu apenas{emoji}**{value}**",
    }

    resp = response_text[choice]
    colecao = str(ctx.guild.id)
    user = find_user(user_id, colecao)

    user.work(colecao, value)

    await ctx.send(resp)


@commands.command()
async def saque(ctx, valor: str = None):
    """Saca o valor especificado

    uso: saque <valor | tudo>

    Argumentos:
        - valor: Um valor inteiro de dinheiro a ser sacado
        - tudo: Todo o dinheiro guardado
    """

    view = await transacao(ctx, "Saque", valor)


@commands.command()
async def depositar(ctx, valor: str = None):
    """Deposita o valor especificado

    uso: depositar <valor | tudo>

    Argumentos:
        - valor: Um valor inteiro de dinheiro a ser depositado
        - tudo: Guardar todo o dinheiro
    """

    view = await transacao(ctx, "Deposito", valor)


@commands.command()
async def roubar(ctx: commands.Context, member: discord.Member = None):

    """Você rouba um valor aleatório de algum membro, boa sorte!

    uso: roubar <apelido | nome>

    Argumentos:
        - apelido: O apelido daquele membro neste servidor
        - nome: O nome daquele usuário
    """

    ladrao = ctx.message.author
    #user = getid(ctx.guild.id, Username)
    user = find_user(str(member.id), str(ctx.guild.id))
    if user == None:
        await ctx.send(
            f":no_entry_sign:  Não da pra roubar fantasma , digite j!roubar <Usuario>"
        )
        return
    guildID = str(ctx.guild.id)
    userID = str(user.id)
    
    #saldo_da_vitima = user_list[guildID][userID].getsaldo()
    
    saldo_da_vitima = user.getsaldo()
    
    if saldo_da_vitima <= 0:
        await ctx.send(f"{user.name} Não tem 1 centavo na mao")
        return

    robb_weight = [1] * 80 + [2] * 20
    robb_odds = {
        1: random.randint(int(saldo_da_vitima * 0.2), int(saldo_da_vitima * 0.5)),
        2: random.randint(int(saldo_da_vitima * 0.2), int(saldo_da_vitima)),
    }
    resp = "?"
    choice = random.choice(robb_weight)
    value = robb_odds[choice]
    emoji = ":money_with_wings:"

    if user.getsaldo() > 1:
        if value > saldo_da_vitima * 0.80:
            resp = f"> {ladrao.name} Deu uma Rasteira em <@{userID}> e roubou quase tudo ({emoji}{value})"
        else:
            if value < saldo_da_vitima * 0.80:
                resp = f"> <@{userID}>  deixou cair ({emoji}{value}) da carteira e {ladrao.name} não deu mole "
            else:
                resp = f"> {ladrao.name} Roubou a pequena quantia de ({emoji}{value}) do <@{userID}>"
    else:
        resp = f"> {user.name} Não tem 1 centavo na mao"

    colecao = str(ctx.guild.id)
    user.work(colecao, value * -1)
    user_list[guildID][str(ladrao.id)].work(colecao, value)

    await ctx.channel.send(resp)


async def setup(bot):
    # Every extension should have this function
    bot.add_command(placar)
    bot.add_command(saldo)
    bot.add_command(trabalhar)
    bot.add_command(roubar)
    bot.add_command(saque)
    bot.add_command(rank)
    bot.add_command(depositar)
