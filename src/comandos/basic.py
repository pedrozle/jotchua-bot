from discord import Member
from discord.ext import commands
from discord import app_commands, Interaction
from discord.ext.commands import Bot, Cog
from discord.ext.commands import Context
from src.methods import embed_msg
from datetime import datetime
import random


class BasicComands(Cog, name="Comandos Básicos"):
    def __init__(self, client: Bot):
        self.client = client  # sets the client variable so we can use it in cogs

    @commands.Cog.listener()
    async def on_ready(self) -> None:
        pass

    @app_commands.command()
    async def ping(self, interaction: Interaction):
        await interaction.response.send_message(
            f"Pong! In {round(self.client.latency * 1000)}ms"
        )

    @app_commands.command()
    async def membros(self, interaction: Interaction):
        """Exibe uma listagem dos membros deste servidor."""

        string_member = ""
        bot: commands.Bot = interaction.client
        id = interaction.guild.id
        for guild in bot.guilds:
            if guild.id == id:
                title_header = guild.name
                icon_header = guild.icon
                title_content = "Membros deste servidor: "
                for member in guild.members:
                    string_member += f"\n{member}"

        desc_content = string_member
        footer = f"Perguntado por {interaction.user.name}"

        await interaction.response.send_message(
            embed=embed_msg(
                icon_header=icon_header,
                title_header=title_header,
                title_content=title_content,
                desc_content=desc_content,
                footer=footer,
            )
        )

    @app_commands.command()
    async def info(self, interaction: Interaction, user: Member = None):
        """Exibe informações sobre você ou sobre um usuário especificado

        uso: info <nada | apelido>

        Argumentos:
            - nada: Exibe informações sobre o seu usuário
            - apelido: Exibe informações sobre o usuário com aquele apelido
        """

        if user is None:
            user = interaction.user

        title_header = f"Informações sobre {user.name}"
        title_content = user.nick
        avatar = user.display_avatar.url
        joined_at = user.joined_at.replace(tzinfo=None)
        diff = datetime.now() - joined_at
        desc = f"Entrou no servidor há {diff.days} dias!"
        footer = f"Perguntado por {interaction.user.name}"
        await interaction.response.send_message(
            embed=embed_msg(
                title_header=title_header,
                title_content=title_content,
                desc_content=desc,
                img_content=avatar,
                footer=footer,
            )
        )

    @app_commands.command()
    async def decida(self, interaction: Interaction, choices: str):
        """Pede ao cão para decidir entre várias opções

        uso: decida <arg1> ou <arg2> ou ... ou <argN>

        Argumentos:
            - args: as opções a qual o Jotchua deve escolher
        """

        if not choices:
            await interaction.response.send_message(
                "Que?!? :confused:\nNão dá pra decidir entre nada e nada, temq colocar algo ne"
            )
            return

        choices_list = []
        frase = ""
        for c in choices.split():
            if c != "ou":
                frase += f"{c} "
            else:
                choices_list.append(frase.strip())
                frase = ""
        choices_list.append(frase)

        result = f"Eu escolho acho que\n"
        result += f"**{random.choice(choices_list)}**"
        await interaction.response.send_message(result)

    # @app_commands.command()
    # async def repita(self, interaction: Interaction, times: int, content: str):
    #     """Repete uma mensagem várias vezes, max 10 vezes
    #     uso: repita <nro de vezes> <mensagem>
    #     Argumentos:
    #         - nro de vezes: Total de vezes que a mensagem será repetida
    #         - mensagem: a mensagem a ser repetida
    #     """

    #     try:
    #         times = int(times)
    #         if times > 10:
    #             times = 10
    #     except Exception:
    #         response = "nro vezes inválido :dizzy_face:\nO número de vezes deve ser um valor inteiro maior que 0\n\n EX:`repita 2 quero caféééé`"
    #         await interaction.response.send_message(response)

    #     if times is None or times < 1:
    #         response = "Não dá pra repetir 0 ou menos vezes! :rage:\nBote um valor pra eu repetir\n\n EX:`repita 2 quero caféééé`"
    #         await interaction.response.send_message(response)

    #     if not content:
    #         response = "Não sei o que é para repetir! :face_with_raised_eyebrow:\nDiga o que é pra repetir\n\n EX:`repita 2 quero caféééé`"
    #         await interaction.response.send_message(response)

    #     for i in range(times):
    #         await interaction.response.send_message(frase)
    #     await interaction.response.send_message(f"Disse: <@{ctx.message.author.id}>")

    @app_commands.command()
    async def dado(self, interaction: Interaction, dice: str = None):
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
            rolls, size = map(int, dice.split("d"))
            result = f"{result} {rolls}d{size} :game_die:\n"
        else:
            result = f"{result} 1d6 :game_die:\n"

        for i in range(rolls):
            result += f"Lançamento {i+1}: **{str(random.randint(1, size))}**.\n"
        await interaction.response.send_message(result)


async def setup(bot: Bot):
    # Every extension should have this function
    await bot.add_cog(BasicComands(bot))
