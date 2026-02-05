import json
import random
import sys


def load_game_data(filepath: str) -> dict:
    """
    Charge les données du jeu.
    """
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            data = json.load(file)
            return data
        
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Fichier introuvable: {e}")
        
    except json.JSONDecodeError as e:
        raise ValueError(f"Fichier JSON invalide : {e}")
        
    except Exception as e:
        raise RuntimeError(f"Erreur inattendue : {e}")


class Player:
    """
    Represente le joueur explorateur et son état courant dans la partie.
    """
    
    def __init__(self, name: str, health_points: int=20):
        """
        Initialise un joueur avec ces caractéristiques de départ.
        """
        self.name = name
        self.health_points = health_points
        self.force = random.randint(1, 10)
        self.inventory = {}
    
    
def main():
    pass


if __name__ == "__main__":
    main()