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

# add league id and conference in standings csv
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

def transform_arena(xml_file_path, save_csv=False, csv_file_path='data/csv/arena_259167.csv'):
    """
    Transforme le fichier XML de l'arène en DataFrame et en option, sauvegarde en CSV.
    
    :param xml_file_path: Chemin vers le fichier XML de l'arène.
    :param save_csv: Si True, enregistre les données en CSV (par défaut False).
    :param csv_file_path: Chemin du fichier CSV de sortie (utilisé si save_csv=True).
    :return: DataFrame des informations de l'arène.
    """
    
    # Charger le fichier XML
    tree = ET.parse(xml_file_path)
    root = tree.getroot()

    # Récupérer le nom de l'arène
    arena_name = root.find("arena/name").text

    # Créer une liste vide pour stocker les données des sièges
    seats_data = []

    # Parcourir chaque type de siège dans l'arène
    for seat in root.findall(".//seats/*"):
        seat_info = {
            'arena_name': arena_name,
            'seat_type': seat.tag,
            'capacity': int(seat.text),
            'current_price': float(seat.attrib['price']),
            'next_price': float(seat.attrib['nextPrice'])
        }

        # Ajouter les informations des sièges à la liste
        seats_data.append(seat_info)

    # Convertir la liste en DataFrame
    df = pd.DataFrame(seats_data)

    # Si save_csv est True, enregistrer le DataFrame dans un fichier CSV
    if save_csv:
        df.to_csv(csv_file_path, index=False)
        print(f"Données de l'arène enregistrées dans le fichier {csv_file_path}")

    return df

# Exemple d'utilisation
if __name__ == '__main__':
    df = transform_arena('data/xml/arena_259167.xml', save_csv=True)
    print(df)


def transform_team_info(xml_file_path, save_csv=False, csv_file_path='data/csv/teaminfo_259167.csv'):
    """
    Transforme le fichier XML des informations de l'équipe en DataFrame et en option, sauvegarde en CSV.
    
    :param xml_file_path: Chemin vers le fichier XML des informations de l'équipe.
    :param save_csv: Si True, enregistre les données en CSV (par défaut False).
    :param csv_file_path: Chemin du fichier CSV de sortie (utilisé si save_csv=True).
    :return: DataFrame des informations de l'équipe.
    """
    
    # Charger le fichier XML
    tree = ET.parse(xml_file_path)
    root = tree.getroot()
    team_element = root.find("team")

    # Extraire les informations de l'équipe
    team_info = {
        'team_id': root.find('team').attrib['id'],
        'team_name': team_element.find('teamName').text,
        'short_name': team_element.find('shortName').text,
        'owner': team_element.find('owner').text,
        'supporter': team_element.find('owner').attrib['supporter'],
        'create_date': team_element.find('createDate').text,
        'last_login_date': team_element.find('lastLoginDate').text,
        'league_id': team_element.find('league').attrib['id'],
        'league_name': team_element.find('league').text,
        'league_level': team_element.find('league').attrib['level'],
        'country': team_element.find('country').text,
        'country_id': team_element.find('country').attrib['id'],
        'rival_team_id': team_element.find('rival').attrib['id'],
        'rival_team_name': team_element.find('rival').text
    }

    # Convertir les informations de l'équipe en DataFrame
    df = pd.DataFrame([team_info])

    # Si save_csv est True, enregistrer le DataFrame dans un fichier CSV
    if save_csv:
        df.to_csv(csv_file_path, index=False)
        print(f"Données de l'équipe enregistrées dans le fichier {csv_file_path}")

    return df

# Exemple d'utilisation
if __name__ == '__main__':
    df = transform_team_info('data/xml/teaminfo_259167.xml', save_csv=True)
    print(df)

# add match id in boxscore csv
def transform_boxscore(xml_file_path, save_csv=False, csv_file_path='data/csv/boxscore_131319577.csv'):
    """
    Transforme le fichier XML de boxscore en DataFrame et en option, sauvegarde en CSV.
    
    :param xml_file_path: Chemin vers le fichier XML de boxscore.
    :param save_csv: Si True, enregistre les données en CSV (par défaut False).
    :param csv_file_path: Chemin du fichier CSV de sortie (utilisé si save_csv=True).
    :return: DataFrame des performances des joueurs.
    """
    
    # Charger le fichier XML
    tree = ET.parse(xml_file_path)
    root = tree.getroot()

    # Créer une liste vide pour stocker les données des joueurs
    player_data = []

    # Parcourir les équipes (homeTeam et awayTeam)
    for team in root.findall(".//teamName/.."):
        team_name = team.find('teamName').text
        team_id = team.attrib['id']

        # Parcourir chaque joueur dans le boxscore
        for player in team.findall(".//player"):
            player_info = {
                'team_id': team_id,
                'team_name': team_name,
                'player_id': player.attrib['id'],
                'first_name': player.find('firstName').text,
                'last_name': player.find('lastName').text,
                'is_starter': player.find('isStarter').text,
                'minutes_PG': player.find('minutes/PG').text if player.find('minutes/PG') is not None else 0,
                'minutes_SG': player.find('minutes/SG').text if player.find('minutes/SG') is not None else 0,
                'minutes_SF': player.find('minutes/SF').text if player.find('minutes/SF') is not None else 0,
                'minutes_PF': player.find('minutes/PF').text if player.find('minutes/PF') is not None else 0,
                'minutes_C': player.find('minutes/C').text if player.find('minutes/C') is not None else 0,
                'fgm': player.find('performance/fgm').text,
                'fga': player.find('performance/fga').text,
                'tpm': player.find('performance/tpm').text,
                'tpa': player.find('performance/tpa').text,
                'ftm': player.find('performance/ftm').text,
                'fta': player.find('performance/fta').text,
                'oreb': player.find('performance/oreb').text,
                'reb': player.find('performance/reb').text,
                'ast': player.find('performance/ast').text,
                'to': player.find('performance/to').text,
                'stl': player.find('performance/stl').text,
                'blk': player.find('performance/blk').text,
                'pf': player.find('performance/pf').text,
                'pts': player.find('performance/pts').text,
                'rating': player.find('performance/rating').text
            }

            # Ajouter les informations du joueur à la liste
            player_data.append(player_info)

    # Convertir la liste en DataFrame
    df = pd.DataFrame(player_data)

    # Si save_csv est True, enregistrer le DataFrame dans un fichier CSV
    if save_csv:
        df.to_csv(csv_file_path, index=False)
        print(f"Données de boxscore enregistrées dans le fichier {csv_file_path}")

    return df

# Exemple d'utilisation
if __name__ == '__main__':
    df = transform_boxscore('data/xml/boxscore.xml', save_csv=True)
    print(df)


def transform_team_stats(xml_file_path, save_csv=False, csv_file_path='data/csv/teamstats_259167.csv'):
    """
    Transforme le fichier XML des statistiques d'équipe en DataFrame et en option, sauvegarde en CSV.
    
    :param xml_file_path: Chemin vers le fichier XML des statistiques d'équipe.
    :param save_csv: Si True, enregistre les données en CSV (par défaut False).
    :param csv_file_path: Chemin du fichier CSV de sortie (utilisé si save_csv=True).
    :return: DataFrame des statistiques des joueurs.
    """
    
    # Charger le fichier XML
    tree = ET.parse(xml_file_path)
    root = tree.getroot()

    # Créer une liste vide pour stocker les données des joueurs
    player_stats_data = []

    # Parcourir les joueurs dans le fichier XML
    for player in root.findall(".//player"):
        player_info = {
            'player_id': player.attrib['id'],
            'first_name': player.find('firstName').text,
            'last_name': player.find('lastName').text,
            'games': int(player.find('stats/games').text),
            'mpg': float(player.find('stats/mpg').text),
            'fgPerc': float(player.find('stats/fgPerc').text),
            'tpPerc': float(player.find('stats/tpPerc').text),
            'ftPerc': float(player.find('stats/ftPerc').text),
            'orpg': float(player.find('stats/orpg').text),
            'rpg': float(player.find('stats/rpg').text),
            'apg': float(player.find('stats/apg').text),
            'topg': float(player.find('stats/topg').text),
            'spg': float(player.find('stats/spg').text),
            'bpg': float(player.find('stats/bpg').text),
            'ppg': float(player.find('stats/ppg').text),
            'fpg': float(player.find('stats/fpg').text),
            'rating': float(player.find('stats/rating').text)
        }

        # Ajouter les informations du joueur à la liste
        player_stats_data.append(player_info)

    # Convertir la liste en DataFrame
    df = pd.DataFrame(player_stats_data)

    # Si save_csv est True, enregistrer le DataFrame dans un fichier CSV
    if save_csv:
        df.to_csv(csv_file_path, index=False)
        print(f"Données des statistiques d'équipe enregistrées dans le fichier {csv_file_path}")

    return df

# Exemple d'utilisation
if __name__ == '__main__':
    df = transform_team_stats('data/xml/teamstats_259167.xml', save_csv=True)
    print(df)


def transform_economy(xml_file_path, save_csv=False, csv_file_path='data/csv/economy_259167.csv'):
    """
    Transforme le fichier XML de l'économie en DataFrame et en option, sauvegarde en CSV.
    
    :param xml_file_path: Chemin vers le fichier XML de l'économie.
    :param save_csv: Si True, enregistre les données en CSV (par défaut False).
    :param csv_file_path: Chemin du fichier CSV de sortie (utilisé si save_csv=True).
    :return: DataFrame des transactions économiques.
    """
    
    # Charger le fichier XML
    tree = ET.parse(xml_file_path)
    root = tree.getroot()

    # Créer une liste vide pour stocker les données économiques
    economy_data = []

    # Parcourir les informations de la semaine précédente et de la semaine en cours
    for week in root.findall(".//lastWeek") + root.findall(".//thisWeek"):
        week_info = {
            'week_type': 'lastWeek' if week.tag == 'lastWeek' else 'thisWeek',
            'start_date': week.attrib['start'],
            'initial_balance': int(week.find('initial').text),
            'player_salaries': int(week.find('playerSalaries').text),
            'staff_salaries': int(week.find('staffSalaries').text),
            'merchandise': int(week.find('merchandise').text),
            'scouting': int(week.find('scouting').text),
            'tv_money': int(week.find('tvMoney').text),
            'unknown': int(week.find('unknown').text),
            'final_balance': int(week.find('final').text) if week.find('final') is not None else None,
            'current_balance': int(week.find('current').text) if week.find('current') is not None else None
        }

        # Ajouter les revenus des matchs (il peut y avoir plusieurs éléments matchRevenue)
        match_revenues = week.findall('matchRevenue')
        total_match_revenue = sum(int(revenue.text) for revenue in match_revenues)
        week_info['match_revenue_total'] = total_match_revenue

        # Ajouter les informations de la semaine à la liste
        economy_data.append(week_info)

    # Convertir la liste en DataFrame
    df = pd.DataFrame(economy_data)

    # Si save_csv est True, enregistrer le DataFrame dans un fichier CSV
    if save_csv:
        df.to_csv(csv_file_path, index=False)
        print(f"Données économiques enregistrées dans le fichier {csv_file_path}")

    return df

# Exemple d'utilisation
if __name__ == '__main__':
    df = transform_economy('data/xml/economy_259167.xml', save_csv=True)
    print(df)


def transform_player(xml_file_path, save_csv=False, csv_file_path='data/csv/player_51041907.csv'):
    """
    Transforme le fichier XML du joueur en DataFrame et en option, sauvegarde en CSV.
    
    :param xml_file_path: Chemin vers le fichier XML du joueur.
    :param save_csv: Si True, enregistre les données en CSV (par défaut False).
    :param csv_file_path: Chemin du fichier CSV de sortie (utilisé si save_csv=True).
    :return: DataFrame des informations du joueur.
    """
    
    # Charger le fichier XML
    tree = ET.parse(xml_file_path)
    root = tree.getroot()
    player_element = root.find("player")
    # Extraire les informations du joueur
    player_info = {
        'player_id': player_element.attrib['id'],
        'owner_id': player_element.attrib['owner'],
        'retrieved_date': player_element.attrib['retrieved'],
        'first_name': player_element.find('firstName').text,
        'last_name': player_element.find('lastName').text,
        'nationality': player_element.find('nationality').text,
        'nationality_id': player_element.find('nationality').attrib['id'],
        'age': int(player_element.find('age').text),
        'height': int(player_element.find('height').text),
        'dmi': int(player_element.find('dmi').text),
        'jersey': int(player_element.find('jersey').text),
        'salary': int(player_element.find('salary').text),
        'best_position': player_element.find('bestPosition').text,
        'season_drafted': int(player_element.find('seasonDrafted').text),
        'league_drafted': int(player_element.find('leagueDrafted').text),
        'team_drafted': player_element.find('teamDrafted').text,
        'draft_pick': int(player_element.find('draftPick').text),
        'for_sale': int(player_element.find('forSale').text),
        'game_shape': int(player_element.find('skills/gameShape').text),
        'potential': int(player_element.find('skills/potential').text),
        'jump_shot': int(player_element.find('skills/jumpShot').text),
        'range': int(player_element.find('skills/range').text),
        'outside_defense': int(player_element.find('skills/outsideDef').text),
        'handling': int(player_element.find('skills/handling').text),
        'driving': int(player_element.find('skills/driving').text),
        'passing': int(player_element.find('skills/passing').text),
        'inside_shot': int(player_element.find('skills/insideShot').text),
        'inside_defense': int(player_element.find('skills/insideDef').text),
        'rebound': int(player_element.find('skills/rebound').text),
        'block': int(player_element.find('skills/block').text),
        'stamina': int(player_element.find('skills/stamina').text),
        'free_throw': int(player_element.find('skills/freeThrow').text),
        'experience': int(player_element.find('skills/experience').text)
    }

    # Convertir les informations du joueur en DataFrame
    df = pd.DataFrame([player_info])

    # Si save_csv est True, enregistrer le DataFrame dans un fichier CSV
    if save_csv:
        df.to_csv(csv_file_path, index=False)
        print(f"Données du joueur enregistrées dans le fichier {csv_file_path}")

    return df

# Exemple d'utilisation
if __name__ == '__main__':
    df = transform_player('data/xml/player_51041907.xml', save_csv=True)
    print(df)
