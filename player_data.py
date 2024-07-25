from classes import Player

def input_player_data(players_data):
    players = []
    for data in players_data:
        first_name, last_name, apt, set, position, national_association = data
        player = Player(first_name, last_name, apt, set, position, national_association)
        players.append(player)
    return players
