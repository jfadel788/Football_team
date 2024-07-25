import unittest
from player_data import input_player_data
from selectTeam import select_team,random_select_players
from xx import format_table


class TestPlayerModule(unittest.TestCase):
    
    def setUp(self):
        # Initialize player data
        self.players_data = [
            ("Daniel", "Scott", 79, 92, "attacker", "Scotland"),
            ("Ali", "Aslam", 98, 94, "midfielder", "Northern Ireland"),
            ("Oliver", "Barker", 89, 95, "defender", "England"),
            ("Jordan", "Robinson", 45, 89, "attacker", "Wales"),
            ("Steven", "Walker", 88, 87, "midfielder", "Wales"),
            ("Alfie", "Loy", 85, 79, "attacker", "Wales"),
            ("Rashid", "Bhatti", 90, 86, "midfielder", "England"),
            ("Thomas", "Taylor", 97, 85, "defender", "England"),
            ("Theo", "Dolan", 87, 82, "attacker", "Scotland"),
            ("Finley", "Cross", 95, 83, "midfielder", "Northern Ireland"),
            ("Joshua", "Mills", 92, 71, "attacker", "Scotland"),
            ("Leander", "Moore", 91, 72, "midfielder", "Northern Ireland"),
            ("Isaac", "Johnson", 76, 77, "defender", "England"),
            ("William", "Adams", 78, 78, "midfielder", "England"),
            ("Jacob", "Stone", 77, 79, "midfielder", "Wales"),
            ("James", "Chaffey", 93, 70, "attacker", "Wales"),
            ("Lucas", "Saunders", 68, 69, "attacker", "Wales"),
            ("Alexander", "Daly", 43, 67, "midfielder", "England"),
            ("Arlo", "Gilchrist", 50, 65, "attacker", "England"),
        ]
        self.players = input_player_data(self.players_data)
        
            
    
    def test_player_data_content(self):
        # Test if the content of the Player objects matches the input data
        for i, player in enumerate(self.players):
            self.assertEqual(player.first_name, self.players_data[i][0])
            self.assertEqual(player.last_name, self.players_data[i][1])
            self.assertEqual(player.apt, self.players_data[i][2])
            self.assertEqual(player.set, self.players_data[i][3])
            self.assertEqual(player.position, self.players_data[i][4])
            self.assertEqual(player.national_association, self.players_data[i][5])

    def test_select_team(self):
        selected_team = select_team(self.players, 2, 3, 5)
        print("\nSelected Team:")
        print(format_table(selected_team))
        self.assertEqual(len(selected_team), 10)
        num_defenders = len([player for player in selected_team if player.position == 'defender'])
        num_midfielders = len([player for player in selected_team if player.position == 'midfielder'])
        num_attackers = len([player for player in selected_team if player.position == 'attacker'])
        self.assertEqual(num_defenders, 2)
        self.assertEqual(num_midfielders, 3)
        self.assertEqual(num_attackers, 5)
    def test_random_select_players(self):
        random_players = random_select_players(self.players, 5)
        print("\nRandomly Selected Players:")
        print(format_table(random_players))
        self.assertEqual(len(random_players), 5)

if __name__ == "__main__":
    unittest.main()
