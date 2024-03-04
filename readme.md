# Jotchua-Bot

Jotchua é um cachorrinho muito feio porém ele chega a ser fofo. Pensando nisso ele é o rosto do Jotchua-Bot, um bot para o [Discord](https://discord.com).

<img src="assets/jot.svg" style="border-radius: 50%; width: 100px"/>

Feio e Fofo!

### Preparação

Este projeto utiliza como base a biblioteca [Discord](https://discord.com) como base para o servidor. Utiliza também as bibliotecas [Pymongo](https://pypi.org/project/pymongo/) para abrir conexões com o banco de dados.

#### Documentação

É possível encontrar a documentação a seguir:

-   [Documentação](https://discordpy.readthedocs.io/en/stable/) do DiscordPy
-   [Documentação](https://pymongo.readthedocs.io/en/stable/) do Pymongo

## Instalação

> [!IMPORTANT]
> Para executar este projeto, verifique os requisitos de instalação presentes no arquivo `Pipfile`. Este projeto utiliza a instalação a partir do [Pipenv](https://github.com/pypa/pipenv?tab=readme-ov-file#installation).

Para executar a instalação dos pacotes necessários para o funcionamento do sistema, primeiro verifique se o `pipenv` está instalado.

```
pipenv --version
```

Caso esteja instalado em sua máquina poderá prosseguir com a instalação das dependências

```
pipenv install
```

após executar a instalação, execute o código abaixo para iniciar o servidor

```
py main.py
```

# Documentação

A documentação do Jotchua-Bot poderá ser encontrada [neste link](https://pedrozle.github.io/jotchua-bot/), mas abaixo é possível conhecer os comando básicos:

> [!NOTE]  
> Todos os comandos devem iniciar com `j!` ou `jot!` 😊

### Comandos básicos

| Ação                        | Comando                                 | Resultado                                                                                                     |
| --------------------------- | --------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| Listar membros              | `membros`                               | Exibe uma lista de todos os membros neste servidor                                                            |
| Informação sobre um usuário | `info <nada ou apelido >`               | Exibe informações sobre você (caso não envie nenhum apelido) ou sobre um usuário com aquele (apelido/nome/id) |                                               |
| Jotchua Decide              | `decida arg_1 ou arg_2 ou ... ou arg_n` | Escolhe para você um dos dois argumentos que foram passados para ele (pode passar mais de 2 argumentos)       |
