import discord, os, requests, json, random
from replit import db
from mlconjug3 import Conjugator

client = discord.Client()


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = "> " + json_data[0]["q"] + "\n" + "**" + json_data[0]["a"] + "**"
    return quote


def update_custom_msg(custom_msg):
    if "custom" in db.keys():
        custom = db["custom"]
        custom.append(custom_msg)
        db["custom"] = custom
    else:
        db["custom"] = [custom_msg]


def delete_custom_msg(index):
    custom = db["custom"]
    if len(custom) >= index:
        del custom[index]
        db["custom"] = custom


def conjugation(verbe):
    cg = Conjugator(language="fr")
    verb = cg.conjugate(verbe)
    res = verb.conjug_info['Indicatif']
    # 'Présent', 'Imparfait', 'Futur', 'Passé Simple'
    return f"**Présent** => Je **{res['Présent']['1s']}** , Tu **{res['Présent']['2s']}** , Il/Elle/On **{res['Présent']['3s']}** , Nous **{res['Présent']['1p']}** , Vous **{res['Présent']['2p']}** , Ils/Elles **{res['Présent']['3p']}**\n**Imparfait** => Je **{res['Imparfait']['1s']}** , Tu **{res['Imparfait']['2s']}** , Il/Elle/On **{res['Imparfait']['3s']}** , Nous **{res['Imparfait']['1p']}** , Vous **{res['Imparfait']['2p']}** , Ils/Elles **{res['Imparfait']['3p']}**\n**Futur** => Je **{res['Futur']['1s']}** , Tu **{res['Futur']['2s']}** , Il/Elle/On **{res['Futur']['3s']}** , Nous **{res['Futur']['1p']}** , Vous **{res['Futur']['2p']}** , Ils/Elles **{res['Futur']['3p']}**\n**Passé Simple** => Je **{res['Passé Simple']['1s']}** , Tu **{res['Passé Simple']['2s']}** , Il/Elle/On **{res['Passé Simple']['3s']}** , Nous **{res['Passé Simple']['1p']}** , Vous **{res['Passé Simple']['2p']}** , Ils/Elles **{res['Passé Simple']['3p']}**\n> made with mlconjug3"


@client.event
async def on_ready():
    print(f"\a Bot have logged in as {client.user}")
    await client.change_presence(activity=discord.Game(name="$help"))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    elif message.content.startswith("$help"):
        f = open("help.txt", "r")
        await message.channel.send(f.read())
    elif message.content.startswith("$quote"):
        await message.channel.send(get_quote())
    elif message.content.startswith("$chert"):
        if "custom" in db.keys():
            option = db["custom"]
            await message.channel.send(random.choice(option))
        else:
            await message.channel.send(":x: First you have to add nonsense!")

    elif message.content.startswith("$newch"):
        msg = message.content.split("$newch ", 1)[1]
        update_custom_msg(msg)
        await message.channel.send(f"New message added. **{msg}**")

    elif message.content.startswith("$delch"):
        custom = []
        if "custom" in db.keys():
            index = int(message.content.split("$delch ", 1)[1])
            delete_custom_msg(index)
            custom = db["custom"]
            x = [x for x in custom]
            await message.channel.send(f"New nonsense list => **{x}**")
        else:
            await message.channel.send(":x: First you have to add nonsense!")
    elif message.content.startswith("$listch"):
        custom = db["custom"]
        x = [x for x in custom]
        await message.channel.send(f"Nonsense list => **{x}**")

    elif message.content.startswith("$conj"):
        verbe = message.content.split("$conj ", 1)[1]
        await message.channel.send(conjugation(verbe))


client.run(os.getenv("TOKEN"))
