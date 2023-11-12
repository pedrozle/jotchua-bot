import random
import discord

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


def embed_msg(
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
