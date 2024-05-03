import discord
from config import get_settings
from discord.ext import commands
from discord import Message, Guild
from src.models.user_model import UserModel

from src.db.database import db_instance

BOT_TOKEN = get_settings().BOT_TOKEN


class MyClient(commands.Bot):
    async def on_ready(self):
        try:
            synced = await self.tree.sync()
            print(f"Synced {len(synced)} command(s)")
            for command in synced:
                print(f"Command: {command}")
        except Exception as e:
            print(e)
            exit()
        print("------")
        print(f"Logged in as {self.user} (ID: {self.user.id})")
        print("------")
        for guild in self.guilds:
            collection = db_instance.get_collection(str(guild.id))
            print(f"--- {guild.name} ---")
            totalMembers = 0
            for member in guild.members:
                find = collection.find_one({"id": str(member.id)})
                if find is None and not member.bot:
                    user = UserModel(member.name, str(member.id))
                    collection.insert_one(user.__dict__)
                totalMembers += 1
            print(f"{totalMembers} membros")
            print(f"--- end ---\n\n")
        print("--- Ready ---")

    async def setup_hook(self):
        for extension in cogs:
            await self.load_extension(extension)

    async def on_guild_join(self, guild: Guild):
        for channel in guild.text_channels:
            print(channel.name)
            if channel.permissions_for(guild.me).send_messages:
                await channel.send(f"Olá, {guild.name}, eu sou Jotchua!")
            break

    async def on_message(self, message: Message):
        author = message.author
        if not author.bot:
            collection = db_instance.get_collection(str(message.guild.id))
            user = collection.find_one({"id": str(author.id)})
            if user is None:
                user = UserModel(author.name, str(author.id))
                collection.insert_one(user.__dict__)
            else:
                del user["_id"]
                user = UserModel(**user)
                user.add_xp(5)
                collection.update_one({"id": str(author.id)}, {"$set": user.__dict__})
        await self.process_commands(message)


intents = discord.Intents.default()
intents.members = True
intents.message_content = True
command_prefix = ["jot!", "j!"]

cogs = ["src.comandos.basic", "src.comandos.social", "src.comandos.rp","src.comandos.programming"]

client = MyClient(intents=intents, command_prefix=command_prefix)
client.run(BOT_TOKEN)
