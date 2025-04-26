import os
import json
from pathlib import Path
import requests
import shutil

"""
RUN THIS THIRD
"""

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9"
}

# make assets path
assets_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "assets")
Path(assets_path).mkdir(parents=True, exist_ok=True)

# download assets
with open(os.path.join(assets_path, "all_cards.json"), "r") as f:
    all_cards = json.load(f)
    for asset_type in all_cards["image_urls"]:
        asset_type_path = os.path.join(assets_path, asset_type)
        Path(asset_type_path).mkdir(parents=True, exist_ok=True)
        for asset_name in all_cards["image_urls"][asset_type]:
            asset_url = all_cards["image_urls"][asset_type][asset_name]
            r = requests.get(asset_url, headers=headers, stream=True)
            r.raise_for_status()
            file_path = os.path.join(asset_type_path, f"{asset_name}.gif")
            print(f"Downloading {asset_url} to {file_path}")
            with open(file_path, "wb") as file:
                shutil.copyfileobj(r.raw, file)
    cards_path = os.path.join(assets_path, "cards")
    Path(cards_path).mkdir(parents=True, exist_ok=True)
    for card in all_cards["cards"]:
        card_name = card["properties"]["name"]
        card_url = card["properties"]["img_url"]
        try:
            r = requests.get(card_url, headers=headers, stream=True)
            r.raise_for_status()
            file_path = os.path.join(cards_path, f"{card_name}.png")
            print(f"Downloading {card_url} to {file_path}")
            with open(file_path, "wb") as file:
                shutil.copyfileobj(r.raw, file)
        except Exception:
            file_path = os.path.join(cards_path, f"{card_name}.txt")
            print(f"Failed downloading {card_url} to {file_path}")
            with open(file_path, "w") as file:
                file.write(card_name)
