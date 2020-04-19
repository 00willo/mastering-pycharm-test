import re
import typing
from collections import namedtuple
from xml.etree import ElementTree

import requests

Episode = namedtuple("Episode", "title link pubdate guid show_id")
episode_data = {}


def download_info():
    url = "https://talkpython.fm/episodes/rss"

    resp = requests.get(url)
    resp.raise_for_status()

    dom = ElementTree.fromstring(resp.text)
    items = dom.findall("channel/item")
    episode_count = len(items)

    for idx, item in enumerate(items):
        combined_show_id_title = item.find("title").text
        title = re.findall(r"^#\d+ (.*)", combined_show_id_title)[0]
        show_id = re.findall(r"^#(\d+) ", combined_show_id_title)[0]
        episode = Episode(
            title,
            item.find("link").text,
            item.find("pubDate").text,
            item.find("guid").text,
            int(show_id)
        )
        episode_data[episode.show_id] = episode


def get_episode(show_id: int) -> typing.Optional[Episode]:
    return episode_data.get(show_id)
