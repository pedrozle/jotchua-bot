import discord
from discord.ui import View

import sys
sys.path.insert(1, '/path/to/application/app/folder')


class BankView(View):
    def __init__(self,ctx,tipo,valor,user_id,userlist):
        super().__init__(timeout=3)
        self.ctx = ctx
        self.tipo = tipo
        self.valor = valor
        self.user_id = user_id
        self.userlist = userlist

    @discord.ui.button(label="Sim",style=discord.ButtonStyle.green , emoji='💰',custom_id="deposit_sim")
    async def deposit_approved_callback(self,interaction,button):
        userlist = self.userlist
        if(self.tipo == "Deposito"):
            userlist[str(self.ctx.guild.id)][self.user_id].deposito(str(self.ctx.guild.id),self.valor)
        else:
            userlist[str(self.ctx.guild.id)][self.user_id].saque(str(self.ctx.guild.id),self.valor)

        button1 = [x for x in self.children if x.custom_id == "deposit_no"][0]
        self.stop()
        self.clear_items()
        await interaction.response.edit_message(view=self)
        #await interaction.response.followup(f"{self.tipo} Com sucesso")

    @discord.ui.button(label="Nao",style=discord.ButtonStyle.red , emoji='🙅‍♂️',custom_id="deposit_no")
    async def deposit_cancel_callback(self,interaction,button):
        self.stop()
        self.clear_items()
        await interaction.response.edit_message(view=self)
        #await interaction.response.followup(content=f"Operacao Cancelada")

    async def on_timeout(self):
        self.stop()
        self.clear_items()
        return

    async def on_error(self,interaction,error,item,):
        await interaction.response.followup(str(error))

    async def interaction_check(self,interaction) -> bool:
        return interaction.user == self.ctx.author

    async def on_success(self,interaction):
        await interaction.response("Sucesso")