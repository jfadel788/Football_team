def validate_and_correct_players_data(players_data):
    corrected_data = []
    for player in players_data:
        first_name, last_name, apt, set_val, position, national_association = player
        
        # Validate 'apt' field
        while True:
            try:
                apt = int(apt)
                break
            except ValueError:
                apt = input(f"The APT value for {first_name} {last_name} is invalid ({apt}). Please enter a valid integer: ")
        
        # Validate 'set' field
        while True:
            try:
                set_val = int(set_val)
                break
            except ValueError:
                set_val = input(f"The SET value for {first_name} {last_name} is invalid ({set_val}). Please enter a valid integer: ")
        
        corrected_data.append((first_name, last_name, apt, set_val, position, national_association))
    
    return corrected_data
