import message
import arc_update_utils
import webhook
import requests

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

def send_latest():
    # get the raw update xml string from https://releases.arc.net/updates.xml
    # use a web request to get the xml
    xmlfile = get_url_content("https://releases.arc.net/updates.xml")

    # parse the xml into a list of Item objects
    items = arc_update_utils.parse_xml(xmlfile)

    # get the latest item
    latest = items[0]

    # build the message
    messageText = message.BuildMessage(latest)

    # send the message
    webhook.SendWebhook(messageText)

send_latest()

# TODO: Implement auto update checking every set duration
