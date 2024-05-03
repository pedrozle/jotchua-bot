from discord import Member
from discord.ext import commands
from discord import app_commands, Interaction
from discord.ext.commands import Bot, Cog
from src.methods import embed_msg
from datetime import datetime
import random

class ProgrammingComands(Cog, name="Comandos de Programação"):
    def __init__(self, client: Bot):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self) -> None:
        pass

    
    @app_commands.command()
    async def avl(self, interaction: Interaction):
        
        programa = """```c

            // TAD AVL e ED para implementação

            // Tipo de dado
            typedef struct{
                int chave;
            }tipo_elem;

            //Estrutura de dados
            typedef struct no{
                int fb; // fator de balanceamento
                tipo_elem info; 
                struct no *esq, *dir; // filhos da direita e da esquerda
            }No;

            typedef struct{
                No *raiz;
            }Arvore;

            //Operações principais feitas com o TAD, que serão chamadas no programa principal 
            void Criar(Arvore *T); // Cria uma árvore vazia
            int Vazia(Arvore *T);  // verifica se a árvore está vazia
            void Destruir(Arvore *T); // destrói a árvore
            int Inserir(Arvore *T, tipo_elem v); // Insere o elemento v na árvore
            int Remover(Arvore *T, int chave); // remove o elemento de chave "chave" da árvore, se existir
            void Exibir_pre_ordem(Arvore *T);
            void Exibir_in_ordem(Arvore *T);
            void Exibir_pos_ordem(Arvore *T);

            // Inserir aqui o protótipo das funções auxiliares que não serão chamadas no programa principal
            int Inserir_rec(No **t, tipo_elem *v, int *flag);
            int Remover_rec(No **t, int *chave, int *flag);
            void Exibir_pre_ordem_rec(Arvore *T);
            void Exibir_in_ordem_rec(Arvore *T);
            void Exibir_pos_ordem_rec(Arvore *T); 
            ```"""
        await interaction.response.send_message(programa)

async def setup(bot: Bot):
    # Every extension should have this function
    await bot.add_cog(ProgrammingComands(bot))