from discord_webhook import DiscordWebhook
from tokenenv import get_token

username = "Arc Updates"
avatar = "https://media.discordapp.net/attachments/1125148347523674154/1134358288083980308/PFP-240_2.png"

def SendWebhook(contents: str):
    dw = DiscordWebhook(url=get_token(), content=contents, username=username, avatar_url=avatar)
    dw.execute(remove_embeds=True)
    dw.remove_embeds()
