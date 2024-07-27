from classes import Player

def input_player_data(players_data):
    players = []
    for data in players_data:
        first_name, last_name, apt, set, position, national_association = data

        player = Player(first_name, last_name, apt, set, position, national_association)
        players.append(player)
    return players

def main():
    data=[["jawad","fadel",67,78,"attacker","ll"],["jawad","fadel",67,78,"attacker","ll"]]
    player=input_player_data(data)
    print(player)
if __name__ == "__main__":
    main()
