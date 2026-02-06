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
        self.explored_locations = set()

            
def main():
    """
    Affiche le menu principal
    """
    console.print("[bold yellow]Bienvenue au jeu de l'Epopée des Cités Perdues[/bold yellow]")
    
    while True:        
        console.print("[bold green]\nMenu principal :[/bold green]")
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
    name = Prompt.ask("[bold green]\nEntrez votre nom[/bold green]")
    console.print(f"[yellow]Bonne change! {name}[/yellow]")
    
    data = load_game_data("data.json")
    player = Player(name)
    
    while True:
        console.print("[bold green]\nMenu du jeu :[/bold green]")
        console.print("     [cyan]1[cyan] - Explorer un lieu")
        console.print("     [cyan]2[cyan] - Interagir avec une personne")
        console.print("     [cyan]3[cyan] - Afficher l'état du joueur")
        console.print("     [cyan]4[cyan] - Retourner au menu principal")
        
        choice = ask_user_for_numeric_value(1, 4)
        
        if choice == 1:
            explore_location(player, data)
        
        elif choice == 2:
            speak_with()
        
        elif choice == 3:
            show_player_state()
        
        elif choice == 4:
            console.print("[yellow]Retour au menu principal[/yellow]")
            break
    

def explore_location(player: Player, data: dict):
    """
    Explore un lieu du jeu.
    """
    console.print("[yellow]Lieux à explorer :[/yellow]")
    i = 0
    unexplored_locations = []
    for location in data["lieux"]:
        if location["nom"] not in player.explored_locations:
            i += 1
            console.print(f"    [yellow]{i} - {location['nom']}[/yellow]")
            unexplored_locations.append(location)
    
    if not unexplored_locations:
        console.print("[bold yellow]\nBravo! Tu as exploré tous les lieux disponibles.[/bold yellow]")
        console.print("[yellow]Retour au menu du jeu[yellow]")
        return
    
    index = ask_user_for_numeric_value(1, len(unexplored_locations)) - 1
    location = unexplored_locations[index]
    console.print(f"[yellow]Nom : {location['nom']}[/yellow]")
    console.print(f"[yellow]Description : {location['description']}[/yellow]")


def speak_with():
    """
    Parler avec une personne.
    """
    pass


def show_player_state():
    """
    Afficher l'état du joueur.
    """
    pass


def combat(player: Player, force: int, choice: bool) -> str:
    """
    Gère le combat entre le joueur et son ennemi.
    """
    if choice:
        if player.force >= force:
            return "gagne"
        return "perdu"
    return "fuir"
    

if __name__ == "__main__":
    main()