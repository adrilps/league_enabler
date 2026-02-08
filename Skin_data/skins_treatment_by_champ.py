import json

# 1. Load the master list
input_path = r"C:\Users\paulo\OneDrive\Documentos\Discord Bot\Skin_data\skins_dict.json"
with open(input_path, "r", encoding="utf-8") as f:
    master_list = json.load(f)

champ_dict_clean = {}

# 2. Transform into: { "Champion": [ ["Skin Name", "Skin Line"], [...] ] }
skin_dict = {}

for champion, skins in master_list.items():
    # Criamos a entrada no champ_dict_clean
    champ_dict_clean[champion] = []
    
    for skin_name, universe in skins:
        champ_dict_clean[champion].append([skin_name, universe])


# 3. Save the clean dictionary
dict_path = r"C:\Users\paulo\OneDrive\Documentos\Discord Bot\Skin_data\champ_dict.json"
with open(dict_path, "w", encoding="utf-8") as f:
    json.dump(champ_dict_clean, f, indent=4, ensure_ascii=False)

print("Clean 2-string list dictionary created.")