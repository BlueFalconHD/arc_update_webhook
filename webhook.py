from discord_webhook import DiscordWebhook
from tokenenv import get_token

username = "Arc Update Bot"
avatar = "https://media.discordapp.net/attachments/1125148347523674154/1134300007885983885/PFP-240.png?width=431&height=431"

def SendWebhook(contents: str):
    dw = DiscordWebhook(url=get_token(), content=contents, username=username, avatar_url=avatar)
    dw.execute(remove_embeds=True)
