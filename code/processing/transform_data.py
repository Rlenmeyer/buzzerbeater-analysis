import xml.etree.ElementTree as ET
import pandas as pd

def transform_roster(xml_file_path, save_csv=False, csv_file_path='data/csv/roster.csv'):
    """
    Transforme le fichier XML du roster en DataFrame et en option, sauvegarde en CSV.
    
    :param xml_file_path: Chemin vers le fichier XML du roster.
    :param save_csv: Si True, enregistre les données en CSV (par défaut False).
    :param csv_file_path: Chemin du fichier CSV de sortie (utilisé si save_csv=True).
    :return: DataFrame des données des joueurs.
    """
    
    # Charger le fichier XML
    tree = ET.parse(xml_file_path)
    root = tree.getroot()

    # Créer une liste vide pour stocker les données des joueurs
    players_data = []

    # Parcourir chaque joueur dans le fichier XML
    for player in root.findall(".//player"):
        player_info = {
            'id': player.attrib['id'],
            'firstName': player.find('firstName').text,
            'lastName': player.find('lastName').text,
            'nationality': player.find('nationality').text,
            'age': int(player.find('age').text),
            'height': int(player.find('height').text),
            'dmi': int(player.find('dmi').text),
            'salary': int(player.find('salary').text),
            'bestPosition': player.find('bestPosition').text,
            # Ajouter d'autres champs ici (comme les compétences)
        }

        # Extraire les compétences du joueur
        skills = player.find('skills')
        player_info['potential'] = int(skills.find('potential').text)
        player_info['gameShape'] = int(skills.find('gameShape').text)
        player_info['jumpShot'] = int(skills.find('jumpShot').text)
        player_info['range'] = int(skills.find('range').text)
        player_info['outsideDef'] = int(skills.find('outsideDef').text)
        player_info['handling'] = int(skills.find('handling').text)
        player_info['driving'] = int(skills.find('driving').text)
        player_info['passing'] = int(skills.find('passing').text)
        player_info['insideShot'] = int(skills.find('insideShot').text)
        player_info['insideDef'] = int(skills.find('insideDef').text)
        player_info['rebound'] = int(skills.find('rebound').text)
        player_info['block'] = int(skills.find('block').text)
        player_info['stamina'] = int(skills.find('stamina').text)
        player_info['freeThrow'] = int(skills.find('freeThrow').text)
        player_info['experience'] = int(skills.find('experience').text)
        # Ajouter d'autres compétences comme souhaité

        # Ajouter les données du joueur à la liste
        players_data.append(player_info)

    # Convertir la liste en DataFrame
    df = pd.DataFrame(players_data)

    # Si save_csv est True, enregistrer le DataFrame dans un fichier CSV
    if save_csv:
        df.to_csv(csv_file_path, index=False)
        print(f"Données enregistrées dans le fichier {csv_file_path}")

    return df

# Exemple d'utilisation
if __name__ == '__main__':
    df = transform_roster('data/xml/roster.xml', save_csv=True)
    print(df)
