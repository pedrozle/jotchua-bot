import os
import discord
from discord.ext import commands
from discord.ext.commands.context import Context
from discord import Message, Guild

from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")


class MyClient(commands.Bot):
    async def on_ready(self):
        print("------")
        print(f"Logged in as {self.user} (ID: {self.user.id})")
        print("------")
        for guild in self.guilds:
            print(f"--- {guild.name} ---")
            for member in guild.members:
                print(member)
            print(f"--- end ---\n\n")

        # TODO: Descomentar aqui quando configurar os comandos
        # for cog in cogs:
        #     await self.load_extension(cog)
        print("--- Ready ---")

    async def on_guild_join(self, guild: Guild):
        for channel in guild.text_channels:
            print(channel.name)
            if channel.permissions_for(guild.me).send_messages:
                await channel.send(f"Olá, {guild.name}, eu sou Jotchua!")
            break

    async def on_message(self, ctx: Context, message: Message):
        print(f"Message from {message.author}: {message.content}")


intents = discord.Intents.default()
intents.message_content = True
command_prefix = ["jot!", "j!"]

# TODO: Adicionar aqui o diretório dos comandos
# cogs = ["src.comandos.basic", "src.comandos.rp", "src.comandos.social"]

client = MyClient(intents=intents, command_prefix=command_prefix)
client.run(BOT_TOKEN)
