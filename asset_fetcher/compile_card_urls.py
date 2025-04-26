"""
Fetch list of cards, and output a text file with all card URLs

NOT USED
"""

import os
import json
import time
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Base URL of the Yugipedia page
#BASE_URL = "https://yugipedia.com"
#LIST_URL = "https://yugipedia.com/wiki/List_of_Yu-Gi-Oh!_Dungeon_Dice_Monsters_(video_game)_cards"
BASE_URL = "https://yugioh.fandom.com/"
LIST_URL = "https://yugioh.fandom.com/wiki/List_of_Yu-Gi-Oh!_Dungeon_Dice_Monsters_(video_game)_cards"


# Directories for storing data
IMG_DIR = "dungeon_dice_monsters_cards"
os.makedirs(IMG_DIR, exist_ok=True)

# Fetch the main list page

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9"
}

response = requests.get(LIST_URL, headers=headers)
response.raise_for_status()
soup = BeautifulSoup(response.text, "html.parser")

# Find all card entries
cards = soup.select("table tr .Card a")

urls = []

for c in cards:
    card_url = urljoin(BASE_URL, c["href"])
    urls.append(card_url)
file_path = os.path.join(os.path.dirname(__file__), "card_urls.txt")
with open(file_path, "w") as file:
    file.write('\n'.join(urls))
