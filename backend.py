import requests, json, random
from replit import db
from mlconjug3 import Conjugator


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


def _8ball():
    choices = [
        "It is certain.", "It is decidedly so.", "Without a doubt.",
        "Yes - definitely.", "You may rely on it.", "As I see it, yes.",
        "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.",
        "Reply hazy, try again.", "Ask again later.",
        "Better not tell you now.", "Cannot predict now.",
        "Concentrate and ask again.", "Don't count on it.", "My reply is no.",
        "My sources say no.", "Outlook not so good.", "Very doubtful."
    ]
    return random.choice(choices)
