import json

# Load once when the bot starts
with open("./Skin_data/skins_dict.json", "r", encoding="utf-8") as f:
    skins_data = json.load(f)

with open("./Skin_data/universe_dict.json", "r", encoding="utf-8") as f:
    universe_data = json.load(f)

def get_champion_skins(champ_name):
    # .get() prevents the bot from crashing if the champion isn't found
    champ_skins = skins_data.get(champ_name)
    
    if champ_skins:
        #I NEED TO FIX THIS I NEED TO FIX THISI NEED TO FIX THIS I NEED TO FIX THISI NEED TO FIX THIS I NEED TO FIX THIS
        return champ_skins
    else: return "Champion not found."

#uses the universe_dict for faster searching
def get_all_universes():
    
    if skins_data:
        return skins_data
    else: return "No universe found"
