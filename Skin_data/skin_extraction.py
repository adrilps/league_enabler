import json
from bs4 import BeautifulSoup

# Load your HTML file
file_path = r"C:\Users\paulo\OneDrive\Documentos\Discord Bot\Skin_data\Raw_skin_data.html"
with open(file_path, "r", encoding="utf-8") as f:
    html_content = f.read()

def extract_by_universe(html):
    soup = BeautifulSoup(html, 'html.parser')
    skin_dict = {}

    # We use this to "remember" the Universe across rows without it
    current_universe = "Unknown Universe"

    for tr in soup.find_all('tr'):
        headers = tr.find_all('th')
        
        # If there are 2 headers, the first one is the Universe (Ages of Runeterra)
        if len(headers) >= 2:
            current_universe = headers[0].get_text(strip=True)
        
        # Find the skins in the <td> cell
        td = tr.find('td')
        if td:
            for li in td.find_all('li'):
                skin_span = li.find('span', class_='skin-icon')
                if skin_span:
                    champion = skin_span.get('data-champion')
                    skin_name = li.get_text(strip=True)
                    
                    if champion not in skin_dict:
                        skin_dict[champion] = []
                    
                    # Store as [Skin Name, Universe Name]
                    skin_dict[champion].append([skin_name, current_universe])
    
    return skin_dict

# Execute
broad_skins_dict = extract_by_universe(html_content)

# Save to your dictionary file
output_path = r"C:\Users\paulo\OneDrive\Documentos\Discord Bot\Skin_data\skins_dict.json"
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(broad_skins_dict, f, indent=4, ensure_ascii=False)

print("Dictionary updated using broad Universes.")