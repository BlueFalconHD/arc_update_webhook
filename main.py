import message
import arc_update_utils
import webhook
import requests
from time import sleep

last_version = ""

def get_url_content(url):
    try:
        response = requests.get(url)
        # Make sure the request was successful
        response.raise_for_status()
    except requests.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    else:
        return response.text

def get_items():
    xmlfile = get_url_content("https://releases.arc.net/updates.xml")
    items = arc_update_utils.parse_xml(xmlfile)

    return items

while True:
    latest = get_items()[0]
    if latest.version_id == last_version:
        pass
    else:
        last_version = latest.version_id
        messageText = message.BuildMessage(latest)
        webhook.SendWebhook(messageText)

    # wait 8 hours
    sleep(28800)


# [x] TODO: Implement auto update checking every set duration
