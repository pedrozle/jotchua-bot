# Jotchua-Bot

Jotchua é um cachorrinho muito feio porém ele chega a ser fofo. Pensando nisso ele é o rosto do Jotchua-Bot, um bot para o [Discord](https://discord.com).

<img src="assets/jot.svg" style="border-radius: 50%; width: 100px"/>

Feio e Fofo!

### Preparação

Este projeto utiliza como base a biblioteca [Discord](https://discord.com) como base para o servidor. Utiliza também as bibliotecas [Pymongo](https://google.com) para abrir conexões com o banco de dados.

#### Documentação

É possível encontrar a documentação a seguir:

-   [Documentação](https://github.com/) do DiscordPy
-   [Documentação](https://github.com/) do Pymongo

## Instalação

> Para executar este projeto, verifique os requisitos de instalação presentes no arquivo `requirements.txt` se desejar optar por uma instalação limpa, instale e inicie um ambiente de desenvolvimento venv, conda, etc.

Para executar a instalação dos pacotes necessários para o funcionamento do sistema, execute o código

```
pip install -r requirements.txt
```

após executar a instalação, execute o código abaixo para iniciar o servidor

```
py main.py
```

# Documentação

A documentação do Jotchua-Bot poderá ser encontrada [neste link](https://github.com), mas abaixo é possível conhecer os comando básicos:

> [!NOTE]  
> Todos os comandos devem iniciar com `j!` ou `jot!` 😊

### Comandos básicos

| Ação                        | Comando                                 | Resultado                                                                                                     |
| --------------------------- | --------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| Listar membros              | `membros`                               | Exibe uma lista de todos os membros neste servidor                                                            |
| Informação sobre um usuário | `info <nada ou apelido >`               | Exibe informações sobre você (caso não envie nenhum apelido) ou sobre um usuário com aquele (apelido/nome/id) |
| Repetir                     | `repetir <nro de vezes> <mensagem>`     | Repete <nro de vezes> vezes a <mensagem> e informa quem disse                                                 |
| Jotchua Decide              | `decida arg_1 ou arg_2 ou ... ou arg_n` | Escolhe para você um dos dois argumentos que foram passados para ele (pode passar mais de 2 argumentos)       |
