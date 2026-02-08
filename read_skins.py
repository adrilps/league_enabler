import json

# Load once when the bot starts
with open("./Skin_data/champ_dict.json", "r", encoding="utf-8") as f:
    skins_data = json.load(f)

with open("./Skin_data/universe_dict.json", "r", encoding="utf-8") as f:
    universe_data = json.load(f)


champ_lookup = {name.lower(): name for name in skins_data.keys()}
universe_lookup = {name.lower(): name for name in universe_data.keys()}


def get_champion_skins(champ_name):
    #turns "nasus" into "Nasus"
    real_name = champ_lookup.get(champ_name.lower())

    if real_name:
        return skins_data.get(real_name)
    
    return []

def get_by_universe(universe_name):
    # turns "pharaoh" into "Pharaoh"
    real_name = universe_lookup.get(universe_name.lower())

    if real_name:
        return universe_data.get(real_name)
    
    return None


#uses the universe_dict for faster searching
def get_all_universes():
    if universe_data:
        return universe_data
    else: return "No universe found"
