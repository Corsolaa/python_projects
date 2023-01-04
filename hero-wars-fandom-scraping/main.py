import json
import operator

import fandom


def start():
    fandom.set_wiki("hero-wars")
    heroes_info = get_hero_info(get_hero_page_info())
    # heroes_info = [{'name': 'Chabba', 'role': ['Tank', 'Control'], 'faction': 'Way of Nature', 'main_stat': 'Strength',
    #                 'attack_type': ['Physical', 'Pure'], 'arti_team_buff': 'Armor'},
    #                {'name': 'Aurora', 'role': ['Tank'],
    #                 'faction': 'Way of Nature', 'main_stat': 'Strength', 'attack_type': ['Magic'],
    #                 'arti_team_buff': 'Dodge'},
    #                {'name': 'Cleaver', 'role': ['Tank', 'Control'], 'faction': 'Way of Chaos', 'main_stat': 'Strength',
    #                 'attack_type': ['Physical', 'Pure'], 'arti_team_buff': 'Armor'}]
    for hero in heroes_info:
        hero["skins"] = get_hero_skin_info(hero["name"], hero["main_stat"])
        print(hero)
    with open("hero.json", "w") as write_file:
        json.dump(heroes_info, write_file)


def get_hero_page_info():
    heroes_html = fandom.page("Heroes").plain_text
    mobile_section = heroes_html.split("available in the mobile version")[1].split("History and introduction")[0]
    mobile_clean = mobile_section.split("Order Rank")[1]
    return mobile_clean.splitlines()


def split_upper_case(string):
    new_string = ""
    for x in range(len(string)):
        if string[x].isupper() and x != 0:
            new_string += " "
            new_string += string[x]
        else:
            new_string += string[x]
    return new_string.split()


def get_hero_info(hero_info):
    return_info = []
    counter = 1
    while counter < len(hero_info):
        if ".png" in hero_info[counter]:
            hero_info[counter] = hero_info[counter].split(".png")[1]
        name = hero_info[counter]
        counter += 1
        role = split_upper_case(hero_info[counter])
        counter += 1
        faction = hero_info[counter]
        counter += 1
        main_stat = hero_info[counter]
        counter += 1
        attack_type = split_upper_case(hero_info[counter])
        counter += 1
        arti_team_buff = hero_info[counter]
        counter += 3
        return_info.append(
            {"name": name,
             "role": role,
             "faction": faction,
             "main_stat": main_stat,
             "attack_type": attack_type,
             "arti_team_buff": arti_team_buff})
    return_info.sort(key=operator.itemgetter("name"))
    return return_info


def get_hero_skin_info(hero_name, main_stat):
    skins = {}
    skins_app = []
    effects = []
    hero = fandom.page("Heroes/" + hero_name.replace(" ", "_") + "#Mobile")

    mobile_section = hero.html.split("aside")
    mobile_index = 3
    if hero_name == "Mushy and Shroom":
        mobile_index = 1
    skin_section = mobile_section[mobile_index].split('title="Skins/')
    i = 2
    while i < len(skin_section):
        skins_app.append(skin_section[i].split(" ")[0])
        effect_section = skin_section[i].split('right">')[1]
        effects.append(effect_section.split("</td>")[0])
        i += 1
    x = 0
    skins["Default"] = main_stat
    while x < len(skins_app):
        skins[skins_app[x]] = effects[x]
        x += 1
    return skins


if __name__ == "__main__":
    start()
