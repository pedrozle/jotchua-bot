import json
import random
import discord
import db.mongo as mongo
from discord.ui import View, Button
from classes.bank import BankView
from classes.user import User
from datetime import timedelta , datetime

user_list = {}
user_cooldown_list = {}
coomand_cooldown = {'roubar':'00:10:00', 
                    'trabalhar':'01:00:00'}


def get_command_cooldown(command):
    if command in coomand_cooldown.keys():
        return coomand_cooldown[command]
    else:
        return None

async def set_new_cooldown(channel,user,command,ctx):
    _cooldown = datetime.strptime(coomand_cooldown[command], '%H:%M:%S').time()
    
    time = datetime.now()
    _cooldown = datetime(time.year,time.month,time.day,_cooldown.hour,_cooldown.minute)
    _new_cool_down = (time + timedelta(hours=_cooldown.hour,minutes=_cooldown.minute))
    
    if(channel not in user_cooldown_list):
        user_cooldown_list.update({channel:{}})
    if(user not in user_cooldown_list[channel]):
        user_cooldown_list[channel].update({user:{command:_new_cool_down}})
    else:
        _temp = user_cooldown_list[channel][user]
        
        DATEDIFF = _temp[command] - time
        
        if(DATEDIFF < timedelta(seconds=0)):
             _temp.update({command:_new_cool_down})
        else:
            
            test = str(DATEDIFF).split(":")
            test[2] = test[2][:2]
            _ = ["Hora(s)","Minuto(s)","Segundo(s)"]
            time_remain = ''.join([f' {t} {_[i]}' for i,t in enumerate(test) if '0'not in t ])
            await ctx.reply(f"\"{command}\" Ainda esta em cooldown , Tempo restante : {time_remain}")
            return False
    return True


def buscar_lista_usuarios_banco(nome_colecao: str):
    dados = mongo.buscar_varios_na_colecao(nome_colecao)
    """
    [
        {'commanders': [pedrozle, calor, paoKentin, sunnay]}
    ]
    """
    _tempList = {}
    if len(dados) > 0:
        for dado in dados:
            usuario = User(dado)
            _tempList.update({str(usuario.id): usuario})
        user_list.update({nome_colecao: _tempList})


def getUser_list(guild_id: str):
    return user_list[guild_id]


def verifica_usuario_lista(user, nome_colecao: str):
    user_id = user.id
    username = user.name
    apelido = user.display_name

    guild_members = []

    if nome_colecao in user_list:
        if len(user_list[nome_colecao]) > 0:
            if(str(user_id) in user_list[nome_colecao]):
                return
            guild_members = [user.id for user in user_list[str(nome_colecao)].values()]

    
    if user_id not in guild_members:
        userdict = {
            "id": str(user_id),
            "name": username,
            "apelido": apelido,
            "balance": 0,
            "bank": 0,
            "lvl": 0,
            "xp": 0,
        }
        usuario = User(userdict)

        _tempList = {}
        
        if nome_colecao in user_list:
            if len(user_list[nome_colecao]) > 0:
                _tempList = user_list[nome_colecao]
            _tempList.update({str(usuario.id): usuario})
        else:
            _tempList.update({str(usuario.id): usuario})

        user_list.update({nome_colecao: _tempList})
        mongo.inserir_na_colecao(nome_colecao, usuario.__dict__)


def tavazio(content):
    if not content:
        return True
    else:
        return False


def find_user(user_id: str, guild_id: str):
    return user_list[guild_id][user_id]


async def transacao(ctx, tipo: str, valor: str | int = None):
    user_id = str(ctx.author.id)
    saldo = 0
    user = user_list[str(ctx.guild.id)][user_id]
    # user = find_user(user_id, str(ctx.guild.id))
    if tipo == "Deposito":
        saldo = user.getsaldo()
    else:
        saldo = user.getpoup()

    if valor == None:
        await ctx.send(f":no_entry_sign: Necessario Especificar valor de {tipo}")
        return
    else:
        if valor.isdigit() == False and valor not in ["all", "tudo"]:
            await ctx.send(f":no_entry_sign: Necessario Especificar valor de {tipo}")
            return

    quantidade = saldo if valor in ["all", "tudo"] else int(valor)
    if saldo <= 0 or quantidade > saldo:
        await ctx.send(
            f":no_entry_sign: Você não possui **{valor}** :dollar: Para {tipo}"
        )
        return
    view = BankView(ctx, tipo, quantidade, user_id, user_list)
    await ctx.send(f"Comfirme que deseja {tipo} {quantidade}:dollar: ", view=view)


async def transacao2(ctx, tipo: str, valor: str | int = None):
    colecao = str(ctx.guild.id)
    user_id = ctx.author.id
    saldo = 0
    user = user_list[user_id]
    if tipo == "Deposito":
        saldo = user_list[user_id].getsaldo()
    else:
        saldo = user_list[user_id].getpoup()

    if valor == None:
        await ctx.send(f":no_entry_sign: Necessario Especificar valor 1")
        return
    else:
        if valor.isdigit() == False and valor not in ["all", "tudo"]:
            await ctx.send(f":no_entry_sign: Necessario Especificar valor 2")
            return

    quantidade = saldo if valor in ["all", "tudo"] else int(valor)
    if saldo <= 0 or quantidade > saldo:
        await ctx.send(
            f":no_entry_sign: Você não possui **{valor}** :dollar: Para {tipo}"
        )
        return

    button1 = Button(label="Sim", style=discord.ButtonStyle.green, emoji="💰")
    button2 = Button(label="No", style=discord.ButtonStyle.red, emoji="🙅‍♂️")

    async def button1_action(interaction):
        if interaction.user.id == user_id:
            if tipo == "Deposito":
                user_list[user_id].deposito(colecao, quantidade)
            else:
                user_list[user_id].saque(colecao, quantidade)
            await interaction.response.send_message(content=f"{tipo} Com sucesso")

    async def button2_action(interaction):
        if interaction.user.id == user_id:
            await interaction.response.send_message(content=f"{tipo} Cancelado")

    button1.callback = button1_action
    button2.callback = button2_action

    view = View()
    view.add_item(button1)
    view.add_item(button2)

    await ctx.send(f"Comfirme que deseja {tipo} {quantidade}:dollar: ", view=view)


def getid(guildID, name):
    user = None
    guild = str(guildID)
    for _user in user_list[guild].values():
        userID = str(_user.id)
        if _user.name.lower() == name.lower():
            user = user_list[guild][userID]
        else:
            if _user.apelido.lower() == name.lower():
                user = user_list[guild][userID]
    return user


def embed_msg(
    ctx,
    icon_header: str = None,
    title_header: str = None,
    title_content: str = None,
    desc_content: str = None,
    img_content: str = None,
    footer: str = None,
):
    # color = 0x4fff4d #cor da barra lateral
    color = pick_color()
    embed_box = discord.Embed(
        title=title_content, description=desc_content, color=color
    )

    embed_box.set_author(name=title_header, icon_url=icon_header)
    embed_box.set_footer(text=footer)
    embed_box.set_image(url=img_content)

    return embed_box


def pick_color():
    colors = [
        0x4FFF4D,
        0x07A6EB,
        0x843AF2,
        0xAB163E,
        0xF05716,
        0xF5FF33,
        0x520808,
        0xFF00EE,
    ]
    return random.choice(colors)
