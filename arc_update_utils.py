from bs4 import BeautifulSoup
from datetime import datetime
from dateutil import tz
import time
from lxml import etree
from typing import List

class Item:
    def __init__(self, date: str, version_id: str, version_number: str, url: str, description: str):
        self.date = date
        self.version_id = version_id
        self.version_number = version_number
        self.url = url
        self.description = description

    def get_unix_date(self) -> int:
        # The format of the date string as specified
        date_format = "%b %d, %Y at %I:%M:%S %p"
        date_obj = datetime.strptime(self.date, date_format)

        # Convert the date to UTC and get the UNIX timestamp
        date_obj = date_obj.replace(tzinfo=tz.gettz('UTC'))
        unix_timestamp = int(time.mktime(date_obj.timetuple()))

        return unix_timestamp

    def get_description_items(self) -> list:
        soup = BeautifulSoup(self.description, 'html.parser')
        list_items = [li.text for li in soup.find_all('li')]
        return list_items

def parse_xml(xml: str | None) -> List[Item]:

    if xml is None:
        return []

    # fix odd error
    xml = xml.replace('<?xml version="1.0" encoding="utf-8"?>', '')

    # remove sparkle: namespace because it is unnecessary
    xml = xml.replace('sparkle:', '')

    root = etree.fromstring(xml)
    ns = {"sparkle": "http://www.andymatuschak.org/xml-namespaces/sparkle"}

    items = []
    for item in root.xpath('//channel/item'):
        date = item.findtext('pubdate')
        version_id = item.findtext('version', namespaces=ns)
        version_number = item.findtext('shortVersionString')
        version_number = version_number.replace(f" ({version_id})", "")
        url = item.find('enclosure').get('url')
        description = item.findtext('description')

        items.append(Item(date, version_id, version_number, url, description))

    return items
