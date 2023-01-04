import fandom


def start():
    fandom.set_wiki("hero-wars")
    heroes_info = get_hero_info(get_hero_page_info())
    create_heroes(heroes_info)


def create_heroes(heroes_info):
    print(heroes_info)


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
    return return_info


# def getHeroInfo(hero_name):
#     hero = fandom.page("Heroes/" + hero_name + "#Mobile")
#     mobile_section = hero.html.split("aside")
#     skin = mobile_section[3].split('title="Category:')[2]
#     print(skin)


if __name__ == "__main__":
    start()
