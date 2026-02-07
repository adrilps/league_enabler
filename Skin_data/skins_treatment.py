import json

# 1. Load your existing data
input_path = r"C:\Users\paulo\OneDrive\Documentos\Discord Bot\Skin_data\skins_dict.json"
with open(input_path, "r", encoding="utf-8") as f:
    # This assumes your current data is { "Champ": [ ["Skin", "Universe"], ... ] }
    champ_based_data = json.load(f)

# 2. Transform into: { "Universe": [ ["Champion", "Skin Name"], [...] ] }
universe_dict = {}

for champion, skins in champ_based_data.items():
    for skin_name, universe in skins:
        # Normalize the universe name as the key
        # We keep the display name but use a lowercase version for the key if you want
        if universe not in universe_dict:
            universe_dict[universe] = []
        
        # Add the champion and their specific skin to this universe
        universe_dict[universe].append([champion, skin_name])

# 3. Save the new Universe-based dictionary
output_path = r"C:\Users\paulo\OneDrive\Documentos\Discord Bot\Skin_data\universe_dict.json"
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(universe_dict, f, indent=4, ensure_ascii=False)

print(f"Dictionary reorganized! Found {len(universe_dict)} unique universes.")