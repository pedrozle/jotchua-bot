# Jotchua-Bot

Jotchua é um cachorrinho muito feio porém ele chega a ser fofo. Pensando nisso ele é o rosto do Jotchua-Bot, um bot para o [Discord](https://discord.com).

<img src="assets/jot.svg" style="border-radius: 50%; width: 100px"/>

Feio e Fofo!

### Preparação

Este projeto utiliza como base a biblioteca [Discord](https://discord.com) como base para o servidor. Utiliza também as bibliotecas [Pymongo](https://google.com) para abrir conexões com o banco de dados.

#### Documentação
É possível encontrar a documentação a seguir:
- [Documentação](https://github.com/) do DiscordPy
- [Documentação](https://github.com/) do Pymongo

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

# Testes

Utilizando a biblioteca [pytest](https://github.com) é possível implementar o sistema orientado à [TDD](https://github.com), escrever funções de teste antes de escrever as funções reais garantindo que as novas implementações não venham quebrar o sistema.

Para executar as funções de teste, abra o terminal e execute a função

```
pytest
```