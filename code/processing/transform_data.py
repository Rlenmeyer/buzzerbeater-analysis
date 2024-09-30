import xml.etree.ElementTree as ET
import pandas as pd

def transform_roster(xml_file_path, save_csv=False, csv_file_path='data/csv/roster_259167.csv'):
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
    df = transform_roster('data/xml/roster_259167.xml', save_csv=True)
    print(df)

def transform_schedule(xml_file_path, save_csv=False, csv_file_path='data/csv/schedule_259167.csv'):
    """
    Transforme le fichier XML du calendrier des matchs en DataFrame et en option, sauvegarde en CSV.
    
    :param xml_file_path: Chemin vers le fichier XML du calendrier des matchs.
    :param save_csv: Si True, enregistre les données en CSV (par défaut False).
    :param csv_file_path: Chemin du fichier CSV de sortie (utilisé si save_csv=True).
    :return: DataFrame des données des matchs.
    """
    
    # Charger le fichier XML
    tree = ET.parse(xml_file_path)
    root = tree.getroot()

    # Créer une liste vide pour stocker les données des matchs
    matches_data = []

    # Parcourir chaque match dans le fichier XML
    for match in root.findall(".//match"):
        match_info = {
            'match_id': match.attrib['id'],
            'start': match.attrib['start'],
            'type': match.attrib['type'],
            'away_team_id': match.find('awayTeam').attrib['id'],
            'away_team_name': match.find('awayTeam/teamName').text,
            'away_team_score': match.find('awayTeam/score').text if match.find('awayTeam/score') is not None else None,
            'home_team_id': match.find('homeTeam').attrib['id'],
            'home_team_name': match.find('homeTeam/teamName').text,
            'home_team_score': match.find('homeTeam/score').text if match.find('homeTeam/score') is not None else None
        }

        # Ajouter les informations du match à la liste
        matches_data.append(match_info)

    # Convertir la liste en DataFrame
    df = pd.DataFrame(matches_data)

    # Si save_csv est True, enregistrer le DataFrame dans un fichier CSV
    if save_csv:
        df.to_csv(csv_file_path, index=False)
        print(f"Données du calendrier enregistrées dans le fichier {csv_file_path}")

    return df

# Exemple d'utilisation
if __name__ == '__main__':
    df = transform_schedule('data/xml/schedule_259167.xml', save_csv=True)
    print(df)

def transform_standings(xml_file_path, save_csv=False, csv_file_path='data/csv/standings_259167.csv'):
    """
    Transforme le fichier XML des standings en DataFrame et en option, sauvegarde en CSV.
    
    :param xml_file_path: Chemin vers le fichier XML des standings.
    :param save_csv: Si True, enregistre les données en CSV (par défaut False).
    :param csv_file_path: Chemin du fichier CSV de sortie (utilisé si save_csv=True).
    :return: DataFrame des standings.
    """
    
    # Charger le fichier XML
    tree = ET.parse(xml_file_path)
    root = tree.getroot()

    # Créer une liste vide pour stocker les données des équipes
    standings_data = []

    # Parcourir chaque conférence dans le fichier XML
    for conference in root.findall(".//conference"):
        # Parcourir chaque équipe dans la conférence
        for team in conference.findall("team"):
            team_info = {
                'team_id': team.attrib['id'],
                'team_name': team.find('teamName').text,
                'wins': int(team.find('wins').text),
                'losses': int(team.find('losses').text),
                'pf': int(team.find('pf').text),  # points marqués
                'pa': int(team.find('pa').text),  # points encaissés
                'is_bot': int(team.find('isBot').text),
                'forfeits': int(team.find('forfeits').text)
            }

            # Ajouter les informations de l'équipe à la liste
            standings_data.append(team_info)

    # Convertir la liste en DataFrame
    df = pd.DataFrame(standings_data)

    # Si save_csv est True, enregistrer le DataFrame dans un fichier CSV
    if save_csv:
        df.to_csv(csv_file_path, index=False)
        print(f"Données des standings enregistrées dans le fichier {csv_file_path}")

    return df

# Exemple d'utilisation
if __name__ == '__main__':
    df = transform_standings('data/xml/standings_259167.xml', save_csv=True)
    print(df)
