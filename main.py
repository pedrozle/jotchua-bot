import discord
import os
from discord.ext import commands
from discord.utils import find

from dotenv import load_dotenv

from methods import getUser_list, verifica_usuario_lista, buscar_lista_usuarios_banco ,get_command_cooldown , set_new_cooldown

load_dotenv()
description = """Jotchua - Bot é o seu mais novo bot que você vai amar ter em seu servidor, auauau caralho"""

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot_prefrix = ["jot!", "j!"]

bot = commands.Bot(
    command_prefix=bot_prefrix, description=description, intents=intents
)

cogs = ["commands.rp", "commands.basic"]


def updateData(ctx):
    name = ctx.name
    user_id = str(ctx.id)
    display_name = ctx.display_name
    if ctx.id != bot.user.id:
        guild_members = getUser_list(str(ctx.guild.id))
        #print(guild_members)
        if user_id in guild_members:
            if guild_members[user_id].apelido.lower() != display_name.lower():
                guild_members[user_id].apelido = display_name.lower()

@bot.event
async def on_guild_join(guild):
    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
            await channel.send(f'Olá, {guild.name}, eu sou Jotchua!')
            await on_ready()
        break


@bot.event
async def on_message(message):
    if message.author.id == bot.user.id:
        return
    updateData(message.author)
    guild_members = getUser_list(str(message.guild.id))
    user = guild_members[str(message.author.id)]
    user.add_xp(str(message.guild.id), 5)
    message.content = message.content.lower()
    
    processMessage = True
    if message.content.find('jot!') != -1 or message.content.find('j!') != -1:
        command = list((message.content).split("!"))[1]
        processMessage = True
        if get_command_cooldown(command) != None:
            processMessage = await set_new_cooldown(channel=str(message.guild.id),user=str(message.author.id),command=command,ctx=message)
   
    if(processMessage):
        await bot.process_commands(message)


@bot.event
async def on_ready():
    print("------")
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    print("------")
    for guild in bot.guilds:
        print(guild.name)
        buscar_lista_usuarios_banco(str(guild.id))
        for member in guild.members:
            if member.id == bot.user.id:
                continue
            verifica_usuario_lista(member, str(guild.id))
    print("------")
    for cog in cogs:
        await bot.load_extension(cog)
    print('--- Ready ---')


bot.run(os.getenv("BOT_TOKEN"))
