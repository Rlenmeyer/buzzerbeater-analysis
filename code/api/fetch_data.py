import os
from dotenv import load_dotenv
import requests
import uuid
from datetime import datetime

# Charger les variables d'environnement depuis le fichier .env
load_dotenv()

def fetch_roster(team_id):
    api_key = os.getenv('BUZZERBEATER_API_KEY')

    if not api_key:
        raise ValueError("La clé API est manquante. Veuillez la définir dans un fichier .env ou comme variable d'environnement.")
    
    # URL de base de l'API
    BASE_URL = "http://bbapi.buzzerbeater.com"

    # Utiliser une session HTTP
    with requests.Session() as session:
        # Requête de login
        login_url = f"{BASE_URL}/login.aspx?login=Treex&code={api_key}"
        response = session.get(login_url)
        if response.status_code != 200:
            raise Exception(f"Erreur lors de la connexion : {response.status_code}, réponse : {response.text}")

        # Générer un UUID pour le fichier
        unique_id = uuid.uuid4()
        # Obtenir la date actuelle au format YYYYMMDD
        current_date = datetime.now().strftime('%Y%m%d')
        # Créer un nom de fichier unique avec UUID, team_id, et date
        file_name = f"{unique_id}_roster_{team_id}_{current_date}.xml"
        file_path = f'data/xml/{file_name}'
        # Requête pour récupérer le roster
        roster_url = f"{BASE_URL}/roster.aspx?teamid={team_id}"
        response = session.get(roster_url)
        if response.status_code == 200:
            with open(file_path, 'wb') as file:
                file.write(response.content)
            print(f"Données du roster récupérées avec succès dans {file_name}.")
        else:
            print(f"Erreur lors de la récupération des données : {response.status_code}, réponse : {response.text}")

        # Requête de logout
        logout_url = f"{BASE_URL}/logout.aspx?login=Treex&code={api_key}"
        response = session.get(logout_url)
        if response.status_code == 200:
            print("Déconnexion réussie.")
        else:
            print(f"Erreur lors de la déconnexion : {response.status_code}, réponse : {response.text}")
            
        return file_path

# test fetch_roster
if __name__ == '__main__':
    team_id = '259167'
    fetch_roster(team_id)
    
def fetch_schedule(team_id):
    api_key = os.getenv('BUZZERBEATER_API_KEY')

    if not api_key:
        raise ValueError("La clé API est manquante. Veuillez la définir dans un fichier .env ou comme variable d'environnement.")
    
    # URL de base de l'API
    BASE_URL = "http://bbapi.buzzerbeater.com"

    # Utiliser une session HTTP
    with requests.Session() as session:
        # Requête de login
        login_url = f"{BASE_URL}/login.aspx?login=Treex&code={api_key}"
        response = session.get(login_url)
        if response.status_code != 200:
            raise Exception(f"Erreur lors de la connexion : {response.status_code}, réponse : {response.text}")

        # Générer un UUID pour le fichier
        unique_id = uuid.uuid4()
        
        # Obtenir la date actuelle au format YYYYMMDD
        current_date = datetime.now().strftime('%Y%m%d')
        
        # Créer un nom de fichier unique avec UUID, team_id, et date
        file_name = f"{unique_id}_schedule_{team_id}_{current_date}.xml"
        file_path = f'data/xml/{file_name}'
        
        # Requête pour récupérer le calendrier
        schedule_url = f"{BASE_URL}/schedule.aspx?teamid={team_id}"
        response = session.get(schedule_url)
        if response.status_code == 200:
            with open(file_path, 'wb') as file:
                file.write(response.content)
            print(f"Données du roster récupérées avec succès dans {file_name}.")
        else:
            print(f"Erreur lors de la récupération des données : {response.status_code}, réponse : {response.text}")

        # Requête de logout
        logout_url = f"{BASE_URL}/logout.aspx?login=Treex&code={api_key}"
        response = session.get(logout_url)
        if response.status_code == 200:
            print("Déconnexion réussie.")
        else:
            print(f"Erreur lors de la déconnexion : {response.status_code}, réponse : {response.text}")
            
        return file_path

# test fetch_schedule
if __name__ == '__main__':
    team_id = '259167'
    fetch_schedule(team_id)
    
def fetch_standings(team_id):
    api_key = os.getenv('BUZZERBEATER_API_KEY')

    if not api_key:
        raise ValueError("La clé API est manquante. Veuillez la définir dans un fichier .env ou comme variable d'environnement.")
    
    # URL de base de l'API
    BASE_URL = "http://bbapi.buzzerbeater.com"

    # Utiliser une session HTTP
    with requests.Session() as session:
        # Requête de login
        login_url = f"{BASE_URL}/login.aspx?login=Treex&code={api_key}"
        response = session.get(login_url)
        if response.status_code != 200:
            raise Exception(f"Erreur lors de la connexion : {response.status_code}, réponse : {response.text}")

        # Générer un UUID pour le fichier
        unique_id = uuid.uuid4()
        
        # Obtenir la date actuelle au format YYYYMMDD
        current_date = datetime.now().strftime('%Y%m%d')
        
        # Créer un nom de fichier unique avec UUID, team_id, et date
        file_name = f"{unique_id}_standings_{team_id}_{current_date}.xml"
        file_path = f'data/xml/{file_name}'
        
        # Requête pour récupérer le classement
        standings_url = f"{BASE_URL}/standings.aspx?teamid={team_id}"
        response = session.get(standings_url)
        if response.status_code == 200:
            with open(file_path, 'wb') as file:
                file.write(response.content)
            print(f"Données du roster récupérées avec succès dans {file_name}.")
        else:
            print(f"Erreur lors de la récupération des données : {response.status_code}, réponse : {response.text}")

        # Requête de logout
        logout_url = f"{BASE_URL}/logout.aspx?login=Treex&code={api_key}"
        response = session.get(logout_url)
        if response.status_code == 200:
            print("Déconnexion réussie.")
        else:
            print(f"Erreur lors de la déconnexion : {response.status_code}, réponse : {response.text}")
            
        return file_path

# test fetch_standings
if __name__ == '__main__':
    team_id = '259167'
    fetch_standings(team_id)
    
def fetch_arena(team_id):
    api_key = os.getenv('BUZZERBEATER_API_KEY')

    if not api_key:
        raise ValueError("La clé API est manquante. Veuillez la définir dans un fichier .env ou comme variable d'environnement.")
    
    # URL de base de l'API
    BASE_URL = "http://bbapi.buzzerbeater.com"

    # Utiliser une session HTTP
    with requests.Session() as session:
        # Requête de login
        login_url = f"{BASE_URL}/login.aspx?login=Treex&code={api_key}"
        response = session.get(login_url)
        if response.status_code != 200:
            raise Exception(f"Erreur lors de la connexion : {response.status_code}, réponse : {response.text}")

        # Générer un UUID pour le fichier
        unique_id = uuid.uuid4()
        
        # Obtenir la date actuelle au format YYYYMMDD
        current_date = datetime.now().strftime('%Y%m%d')
        
        # Créer un nom de fichier unique avec UUID, team_id, et date
        file_name = f"{unique_id}_arena_{team_id}_{current_date}.xml"
        file_path = f'data/xml/{file_name}'
        
        # Requête pour récupérer le classement
        arena_url = f"{BASE_URL}/arena.aspx?teamid={team_id}"
        response = session.get(arena_url)
        if response.status_code == 200:
            with open(file_path, 'wb') as file:
                file.write(response.content)
            print(f"Données de l'arena récupérées avec succès dans {file_name}.")
        else:
            print(f"Erreur lors de la récupération des données : {response.status_code}, réponse : {response.text}")

        # Requête de logout
        logout_url = f"{BASE_URL}/logout.aspx?login=Treex&code={api_key}"
        response = session.get(logout_url)
        if response.status_code == 200:
            print("Déconnexion réussie.")
        else:
            print(f"Erreur lors de la déconnexion : {response.status_code}, réponse : {response.text}")
            
        return file_path

# test fetch_arena
if __name__ == '__main__':
    team_id = '259167'
    fetch_arena(team_id)

def fetch_teaminfo(team_id):
    api_key = os.getenv('BUZZERBEATER_API_KEY')

    if not api_key:
        raise ValueError("La clé API est manquante. Veuillez la définir dans un fichier .env ou comme variable d'environnement.")
    
    # URL de base de l'API
    BASE_URL = "http://bbapi.buzzerbeater.com"

    # Utiliser une session HTTP
    with requests.Session() as session:
        # Requête de login
        login_url = f"{BASE_URL}/login.aspx?login=Treex&code={api_key}"
        response = session.get(login_url)
        if response.status_code != 200:
            raise Exception(f"Erreur lors de la connexion : {response.status_code}, réponse : {response.text}")

        # Générer un UUID pour le fichier
        unique_id = uuid.uuid4()
        
        # Obtenir la date actuelle au format YYYYMMDD
        current_date = datetime.now().strftime('%Y%m%d')
        
        # Créer un nom de fichier unique avec UUID, team_id, et date
        file_name = f"{unique_id}_teaminfo_{team_id}_{current_date}.xml"
        file_path = f'data/xml/{file_name}'
        
        # Requête pour récupérer le classement
        teaminfo_url = f"{BASE_URL}/teaminfo.aspx?teamid={team_id}"
        response = session.get(teaminfo_url)
        if response.status_code == 200:
            with open(file_path, 'wb') as file:
                file.write(response.content)
            print(f"Données de teaminfo récupérées avec succès dans {file_name}.")
        else:
            print(f"Erreur lors de la récupération des données : {response.status_code}, réponse : {response.text}")

        # Requête de logout
        logout_url = f"{BASE_URL}/logout.aspx?login=Treex&code={api_key}"
        response = session.get(logout_url)
        if response.status_code == 200:
            print("Déconnexion réussie.")
        else:
            print(f"Erreur lors de la déconnexion : {response.status_code}, réponse : {response.text}")
            
        return file_path

# test fetch_teaminfo
if __name__ == '__main__':
    team_id = '259167'
    fetch_teaminfo(team_id)
    

def fetch_boxscore(match_id):
    api_key = os.getenv('BUZZERBEATER_API_KEY')

    if not api_key:
        raise ValueError("La clé API est manquante. Veuillez la définir dans un fichier .env ou comme variable d'environnement.")
    
    # URL de base de l'API
    BASE_URL = "http://bbapi.buzzerbeater.com"

    # Utiliser une session HTTP
    with requests.Session() as session:
        # Requête de login
        login_url = f"{BASE_URL}/login.aspx?login=Treex&code={api_key}"
        response = session.get(login_url)
        if response.status_code != 200:
            raise Exception(f"Erreur lors de la connexion : {response.status_code}, réponse : {response.text}")

        # Générer un UUID pour le fichier
        unique_id = uuid.uuid4()
        
        # Obtenir la date actuelle au format YYYYMMDD
        current_date = datetime.now().strftime('%Y%m%d')
        
        # Créer un nom de fichier unique avec UUID, team_id, et date
        file_name = f"boxscore_{match_id}_{current_date}_{unique_id}.xml"
        file_path = f'data/xml/{file_name}'
        
        # Requête pour récupérer le classement
        boxscore_url = f"{BASE_URL}/boxscore.aspx?matchid={match_id}"
        response = session.get(boxscore_url)
        if response.status_code == 200:
            with open(file_path, 'wb') as file:
                file.write(response.content)
            print(f"Données de la boxscore récupérées avec succès dans {file_name}.")
        else:
            print(f"Erreur lors de la récupération des données : {response.status_code}, réponse : {response.text}")

        # Requête de logout
        logout_url = f"{BASE_URL}/logout.aspx?login=Treex&code={api_key}"
        response = session.get(logout_url)
        if response.status_code == 200:
            print("Déconnexion réussie.")
        else:
            print(f"Erreur lors de la déconnexion : {response.status_code}, réponse : {response.text}")
            
        return file_path

# test fetch_boxscore
if __name__ == '__main__':
    match_id = '131319577'
    fetch_boxscore(match_id)

def fetch_teamstats(team_id):
    api_key = os.getenv('BUZZERBEATER_API_KEY')

    if not api_key:
        raise ValueError("La clé API est manquante. Veuillez la définir dans un fichier .env ou comme variable d'environnement.")
    
    # URL de base de l'API
    BASE_URL = "http://bbapi.buzzerbeater.com"

    # Utiliser une session HTTP
    with requests.Session() as session:
        # Requête de login
        login_url = f"{BASE_URL}/login.aspx?login=Treex&code={api_key}"
        response = session.get(login_url)
        if response.status_code != 200:
            raise Exception(f"Erreur lors de la connexion : {response.status_code}, réponse : {response.text}")

        # Générer un UUID pour le fichier
        unique_id = uuid.uuid4()
        
        # Obtenir la date actuelle au format YYYYMMDD
        current_date = datetime.now().strftime('%Y%m%d')
        
        # Créer un nom de fichier unique avec UUID, team_id, et date
        file_name = f"teamstats_{team_id}_{current_date}_{unique_id}.xml"
        file_path = f'data/xml/{file_name}'
        
        # Requête pour récupérer le classement
        teamstats_url = f"{BASE_URL}/teamstats.aspx?teamid={team_id}"
        response = session.get(teamstats_url)
        if response.status_code == 200:
            with open(file_path, 'wb') as file:
                file.write(response.content)
            print(f"Données de teamstats récupérées avec succès dans {file_name}.")
        else:
            print(f"Erreur lors de la récupération des données : {response.status_code}, réponse : {response.text}")

        # Requête de logout
        logout_url = f"{BASE_URL}/logout.aspx?login=Treex&code={api_key}"
        response = session.get(logout_url)
        if response.status_code == 200:
            print("Déconnexion réussie.")
        else:
            print(f"Erreur lors de la déconnexion : {response.status_code}, réponse : {response.text}")
            
        return file_path

# test fetch_teamstats
if __name__ == '__main__':
    team_id = '259167'
    fetch_teamstats(team_id)