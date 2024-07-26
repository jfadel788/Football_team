from player_data import input_player_data
def get_integer_input(prompt):
    while True:
        user_input = input(prompt)
        try:
            return int(user_input)
        except ValueError:
            print("That's not a valid integer. Please try again.")

def validate_and_correct_players_data(players_data):
    corrected_data = []
    for player in players_data:
        first_name, last_name, apt, set, position, national_association = player
        
        if not isinstance(apt, int):
            print(f"Invalid APT for player {first_name} {last_name}.")
            apt = get_integer_input("Enter a new integer for APT: ")
        if not isinstance(set, int):
            print(f"Invalid SET for player {first_name} {last_name}.")
            set = get_integer_input("Enter a new integer for SET: ")


        # Create a new player tuple with the corrected APT
        corrected_player = (first_name, last_name, apt, set, position, national_association)
        corrected_data.append(corrected_player)
    
    return corrected_data
