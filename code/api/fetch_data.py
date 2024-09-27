import os
import requests

def fetch_roster(team_id):
    # Lire la clé API à partir de la variable d'environnement
    api_key = os.getenv('BUZZERBEATER_API_KEY')

    if not api_key:
        raise ValueError("La clé API est manquante. Veuillez la définir comme variable d'environnement.")

    url = f"http://bbapi.buzzerbeater.com/roster.aspx?teamid={team_id}&code={api_key}"
    response = requests.get(url)

    if response.status_code == 200:
        with open('data/roster.xml', 'wb') as file:
            file.write(response.content)
        print("Données du roster récupérées avec succès.")
    else:
        print(f"Erreur lors de la récupération des données : {response.status_code}")

# Exemple d'utilisation
if __name__ == '__main__':
    team_id = '259167'
    fetch_roster(team_id)
