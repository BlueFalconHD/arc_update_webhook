emoji = {
    "arc": "<:arc:1016899655616954458>",
    "clock": "<:time:1022128056917299302>",
    "folder": "<:_:1134276393522430022>",
    "easel": "<:_:1134276391458832514>"
}

def timestamp(time: int) -> str:
    return f"<t:{str(time)}:f>"

def bold(title: str) -> str:
    return f"**{title}**"

def link(text: str, url: str) -> str:
    return f"[{text}]({url})"

def h1(text: str) -> str:
    return f"# {text}"

def emojibullet(emojiname: str, text: str) -> str:
    return f"{emoji[emojiname]} {text}"
