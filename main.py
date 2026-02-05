import json
import random
import sys
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt

console = Console()


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
    """
    Affiche le menu principal
    """
    console.print("[bold yellow]Bienvenue au jeu de l'Epopée des Cités Perdues[/bold yellow]\n")
    
    while True:        
        console.print("[bold green]Menu de démarrage :[/bold green]")
        console.print("     [cyan]1[cyan] - Afficher les règles du jeu")
        console.print("     [cyan]2[cyan] - Commencer une partie")
        console.print("     [cyan]3[cyan] - Quitter")
        
        choice = ask_user_for_numeric_value(1, 3)
        
        if choice == 3:
            console.print("[bold blue]Au revoir![/bold blue]")
            break
            
        elif choice == 1:
            display_game_rules()
        
        elif choice == 2:
            start_game()
        

def ask_user_for_numeric_value(min_value: int, max_value: int) -> int:
    """
    Demander à l'utilisateur d'entrer une valeur numérique entre dans une plage donnée.
    """
    while True:
        entered_value = Prompt.ask(f"\n[bold green]Votre choix[/bold green]")
        
        try:
            value = int(entered_value)
            
            if min_value <= value <= max_value:
                return value
            
            console.print(f"\n[red]Veuillez entrer un nombre entre {min_value} et {max_value}.[/red]")

        except ValueError:
            console.print(f"\n[red]Veuillez entrer une valeur numérique valide.[/red]")
            
            
def display_game_rules() -> None:
    """
    Affiche les règles du jeu.
    """
    console.print(f"Voici les règles du jeu...")


def start_game() -> None:
    """
    Commence une nouvelle partie du jeu.
    """
    pass
    
    


if __name__ == "__main__":
    main()