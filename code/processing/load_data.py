import sqlite3
from datetime import datetime
from api.fetch_data import fetch_player
from processing.transform_data import transform_player

# Connect to or create the SQLite database
conn = sqlite3.connect('data/sql/buzzerbeater_db.db')
c = conn.cursor()

def create_player_table():
    """Create the player history table if it doesn't exist."""
    c.execute('''
        CREATE TABLE IF NOT EXISTS player (
            snapshot_date TEXT,
            player_id TEXT,
            first_name TEXT,
            last_name TEXT,
            age INTEGER,
            height INTEGER,
            dmi INTEGER,
            salary INTEGER,
            best_position TEXT,
            game_shape INTEGER,
            jump_shot INTEGER,
            handling INTEGER,
            driving INTEGER,
            passing INTEGER,
            inside_shot INTEGER,
            inside_defense INTEGER,
            rebound INTEGER,
            block INTEGER,
            stamina INTEGER,
            free_throw INTEGER,
            experience INTEGER,
            PRIMARY KEY (snapshot_date, player_id)
        )
    ''')
    conn.commit()

def insert_or_update_player_stats(player_data):
    """Insert or update the player's data in the SQL database."""
    c.execute('''
        INSERT INTO player (
            snapshot_date, player_id, first_name, last_name, age, height, dmi, salary, best_position, game_shape, 
            jump_shot, handling, driving, passing, inside_shot, inside_defense, rebound, block, stamina, free_throw, 
            experience
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ON CONFLICT(snapshot_date, player_id) DO UPDATE SET
            first_name=excluded.first_name,
            last_name=excluded.last_name,
            age=excluded.age,
            height=excluded.height,
            dmi=excluded.dmi,
            salary=excluded.salary,
            best_position=excluded.best_position,
            game_shape=excluded.game_shape,
            jump_shot=excluded.jump_shot,
            handling=excluded.handling,
            driving=excluded.driving,
            passing=excluded.passing,
            inside_shot=excluded.inside_shot,
            inside_defense=excluded.inside_defense,
            rebound=excluded.rebound,
            block=excluded.block,
            stamina=excluded.stamina,
            free_throw=excluded.free_throw,
            experience=excluded.experience
    ''', (
        datetime.now().strftime('%Y-%m-%d'),
        player_data['player_id'],
        player_data['first_name'],
        player_data['last_name'],
        player_data['age'],
        player_data['height'],
        player_data['dmi'],
        player_data['salary'],
        player_data['best_position'],
        player_data['game_shape'],
        player_data['jump_shot'],
        player_data['handling'],
        player_data['driving'],
        player_data['passing'],
        player_data['inside_shot'],
        player_data['inside_defense'],
        player_data['rebound'],
        player_data['block'],
        player_data['stamina'],
        player_data['free_throw'],
        player_data['experience']
    ))
    conn.commit()

def update_player_history(player_id):
    """Fetch player data, transform it, and store it in the SQL database."""
    player_xml = fetch_player(player_id)
    player_data = transform_player(player_xml)
    insert_or_update_player_stats(player_data)

def main():
    """Main function to update player history with SQL database."""
    create_player_table()
    
    # List of player IDs to track
    players_to_track = ['51041907', 'another_player_id']
    
    # Update the history for each player
    for player_id in players_to_track:
        update_player_history(player_id)

if __name__ == '__main__':
    main()
