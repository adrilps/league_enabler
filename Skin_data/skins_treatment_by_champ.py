import json

# 1. Load the master list
input_path = r"C:\Users\paulo\OneDrive\Documentos\Discord Bot\Skin_data\skins.json"
with open(input_path, "r", encoding="utf-8") as f:
    master_list = json.load(f)

# 2. Transform into: { "Champion": [ ["Skin Name", "Skin Line"], [...] ] }
skin_dict = {}

for skin_line, champion, skin_name in master_list:
    if champion not in skin_dict:
        skin_dict[champion.lower()] = []
    
    # Each entry is now a simple 2-string list
    skin_dict[champion.lower()].append([skin_name, skin_line])

# 3. Save the clean dictionary
dict_path = r"C:\Users\paulo\OneDrive\Documentos\Discord Bot\Skin_data\skins_dict.json"
with open(dict_path, "w", encoding="utf-8") as f:
    json.dump(skin_dict, f, indent=4, ensure_ascii=False)

print("Clean 2-string list dictionary created.")