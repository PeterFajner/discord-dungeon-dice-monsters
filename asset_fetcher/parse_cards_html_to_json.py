import os
import json
import requests
from bs4 import BeautifulSoup
from pathlib import Path

"""
RUN THIS SECOND
"""

folder_path = os.path.join(os.path.dirname(__file__), "dungeon_dice_monsters_cards")

all_cards = []
image_urls = {"crest": {}, "type": {}, "movement": {}}
all_data = {"cards": all_cards, "image_urls": image_urls}

for filename in os.listdir(folder_path):
    if not filename.endswith(".html"):
        continue
    file_path = os.path.join(folder_path, filename)
    print(f"Processing: {file_path}")
    with open(file_path, "r", encoding="utf-8") as file:

        soup = BeautifulSoup(file, "html.parser")

        # Extract the title (monster name)
        title_tag = soup.find("title")
        name = title_tag.text.split("|")[0].strip() if title_tag else "Unknown"

        properties = {}
        all_cards.append({"name": name, "properties": properties})

        # Extract properties table (if exists)
        table = soup.find("table", class_="wikitable")
        if table:
            for row in table.find_all("tr"):
                cells = row.find_all("td")
                if len(cells) == 2:
                    key = cells[0].text.strip()
                    value = cells[1].text.strip()
                    properties[key] = value

        infobox = soup.select(".card-table")[0]
        properties["name"] = infobox.select(".heading")[0].text.strip()
        properties["img_url"] = (
            infobox.find("div", class_="cardtable-main_image-wrapper")
            .find("img")
            .attrs["src"]
        )

        # Extract Japanese name and Romaji
        properties["japanese"] = infobox.find("span", lang="ja").text.strip()
        try:
            properties["romaji"] = infobox.find(
                "span", lang="ja-Latn-Hepburn"
            ).text.strip()
        except AttributeError:
            pass

        # Extract basic info from table
        def get_table_value(label):
            element = infobox.find("th", string=label)
            if element:
                return element.find_next_sibling("td").text.strip()
            return None

        # type
        try:
            card_type_wrapper = infobox.find("th", string="Type\n").find_next_sibling(
                "td"
            )
            # card_type_wrapper = infobox.findAll('th');
            card_type = card_type_wrapper.text.strip()
            properties["type"] = card_type
            type_img_src = card_type_wrapper.find("a").find("img").attrs["src"]
            if type_img_src.startswith("http"):
                image_urls["type"][card_type] = type_img_src
            else:
                try:
                    type_img_data_src = (
                        card_type_wrapper.find("a").find("img").attrs["data-src"]
                    )
                    image_urls["type"][card_type] = type_img_data_src
                except AttributeError:
                    pass
        except AttributeError:
            pass

        # movement
        try:
            card_movement_wrapper = infobox.find(
                "a", title="Movement"
            ).parent.find_next_sibling("td")
            card_movement = card_movement_wrapper.text.strip()
            properties["movement"] = card_movement
            movement_img_src = card_movement_wrapper.find("a").find("img").attrs["src"]
            if movement_img_src.startswith("http"):
                image_urls["movement"][card_movement] = movement_img_src
            else:
                try:
                    movement_img_data_src = (
                        card_movement_wrapper.find("a").find("img").attrs["data-src"]
                    )
                    image_urls["movement"][card_movement] = movement_img_data_src
                except AttributeError:
                    pass
        except AttributeError:
            pass

        properties["level"] = get_table_value("Level")

        # hp, atk, def
        try:
            hp_atk_def = (
                infobox.find("a", title="HP")
                .parent.find_next_sibling("td")
                .text.strip()
            )
            properties["hp"], properties["atk"], properties["defense"] = [
                int(x) for x in hp_atk_def.split("/")
            ]
        except Exception:
            pass

        properties["number"] = get_table_value("Number")

        try:
            properties["lore"] = infobox.find("div", class_="lore").text.strip()
        except AttributeError:
            pass

        try:
            properties["crests"] = []
            crests_title_section = infobox.find(
                "a", href="/wiki/Crest_(Dungeon_Dice_Monsters)"
            ).parent
            crests_links = crests_title_section.find_next_sibling("td").select("a")
            for link in crests_links:
                crest_name = link.attrs["title"]
                properties["crests"].append(crest_name)
                crest_img_src = link.find("img").attrs["src"]
                if crest_img_src.startswith("http"):
                    image_urls["crest"][crest_name] = crest_img_src
                else:
                    try:
                        crest_img_data_src = link.find("img").attrs["data-src"]
                        image_urls["crest"][crest_name] = crest_img_data_src
                    except AttributeError:
                        pass
        except AttributeError:
            pass

        if not properties.get("crests"):
            if properties.get("lore"):
                print("###### no crests for", properties["name"], "but has lore")
            else:
                print("###### no crests for", properties["name"])

# Save data to a JSON file
assets_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "assets")
Path(assets_path).mkdir(parents=True, exist_ok=True)
with open(
    os.path.join(
        assets_path, "all_cards.json"
    ),
    "w",
    encoding="utf-8",
) as f:
    json.dump(all_data, f, indent=4, ensure_ascii=False)
