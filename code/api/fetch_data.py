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

# Exemple d'utilisation
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
        file_name = f"{unique_id}_roster_{team_id}_{current_date}.xml"
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

# Exemple d'utilisation
if __name__ == '__main__':
    team_id = '259167'
    fetch_schedule(team_id)