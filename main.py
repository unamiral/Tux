import discord, os, random, backend

from ping import keep_alive
from replit import db

client = discord.Client()
prefix = "?"


@client.event
async def on_ready():
    print(f"\a Bot have logged in as {client.user}")
    await client.change_presence(activity=discord.Game(name="?help"))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    elif message.content.startswith(f"{prefix}help"):
        f = open("help.txt", "r")
        await message.channel.send(f.read())
    elif message.content.startswith(f"{prefix}quote"):
        await message.channel.send(backend.get_quote())
    elif message.content.startswith(f"{prefix}nonsense"):
        if "custom" in db.keys():
            option = db["custom"]
            await message.channel.send(random.choice(option))
        else:
            await message.channel.send(":x: First you have to add nonsense!")

    elif message.content.startswith(f"{prefix}newns"):
        msg = message.content.split(f"{prefix}newns ", 1)[1]
        backend.update_custom_msg(msg)
        await message.channel.send(f"New message added. **{msg}**")

    elif message.content.startswith(f"{prefix}delns"):
        custom = []
        if "custom" in db.keys():
            index = int(message.content.split(f"{prefix}delns ", 1)[1])
            backend.delete_custom_msg(index)
            custom = db["custom"]
            x = [x for x in custom]
            await message.channel.send(f"New nonsense list => **{x}**")
        else:
            await message.channel.send(":x: First you have to add nonsense!")
    elif message.content.startswith(f"{prefix}listns"):
        custom = db["custom"]
        x = [x for x in custom]
        await message.channel.send(f"Nonsense list => **{x}**")

    elif message.content.startswith(f"{prefix}conj"):
        verbe = message.content.split(f"{prefix}conj ", 1)[1]
        await message.channel.send(backend.conjugation(verbe))


keep_alive()
client.run(os.getenv("TOKEN"))
