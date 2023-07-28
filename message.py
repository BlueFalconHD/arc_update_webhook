from message_builder import *
from typing import List
import arc_update_utils
import random

changelogURL = "https://arc.net/e/D25B2EEA-7506-4850-A169-3B2A00802889"

updatePhrases = [
    "Beep boop. Hey look, a wild update appeared!",
    "Beep boop. An update has been spotted!",
    "Beep boop. An update has been detected!",
    "Beep boop. An update has been found!",
    "Mom get the camera! Arc just got updated!",
    "Mom get the camera! Arc just got updated again!",
    "Hey look! Arc has been updated",
    "*robot noises* Arc has been updated",
    "Arc updated! Also try Minecraft.."
]

def changelogBulletList(changelog: List) -> str:
    return "\n".join([f"> - {item}" for item in changelog])

def BuildMessage(updateitem: arc_update_utils.Item) -> str:

    # start with the title
    titleText = h1(emojibullet("arc", f"Arc {bold(f'v{updateitem.version_number}')}"))

    # changelog
    changelogText = changelogBulletList(updateitem.get_description_items())

    # timestamp
    timestampText = emojibullet("clock", timestamp(updateitem.get_unix_date()))

    # manual download link
    downloadText = emojibullet("folder", link("Manual download link", updateitem.url))

    # easel
    easelText = emojibullet("easel", link("Release notes", changelogURL))

    # combine
    final = f"""{random.choice(updatePhrases)}
{titleText}

{changelogText}

{timestampText}

{easelText}
{downloadText}"""

    return final
