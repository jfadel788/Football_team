from validate import validate_and_correct_players_data
from player_data import input_player_data
from selectTeam import select_team,random_select_players
from format import format_table
from reports import status_report,find_lowest_avg,find_highest_apt,sort_by_apt
def main():
    
    user_data=[]
  
    print("Enter the details in the format: first_name,last_name,apt,set,position,nationality")
    print("type done when you finish")
    while True:
        data=input("Enter data")
        if data.lower() =="done":
            break
        details=data.split(",")
        if len(details)==6 :
              
              set= details[2]
              
             
              apt=   details[3]
              print(apt)
              print(type(apt))
              user_data.append(
            [details[0].strip(),
            details[1].strip(),
             set,
             apt.strip(),
            details[4].strip(),
            details[5].strip()]
        )
     
        else:
               
            print("Invalid input. Please enter exactly 6 values separated by commas.")
   ##validate APT and SET
    correct_data=validate_and_correct_players_data(user_data)
    print(correct_data)
    
    Players=input_player_data(correct_data)
    print(Players)
    while True:
        request=input("Enter your request")
        if request=="Select team":
            nb_attackers=int(input("Enter the required number of attackers"))
            nb_defenders=int(input("Enter the required number of defenders"))
            nb_midfielders =int(input("Enter the required number of midfielders "))
            select_teamm=select_team(Players,nb_defenders,nb_midfielders,nb_attackers)
            print(format_table(select_teamm))
        elif request=="Slect randomly":
            nb_player=int(input("Enter the required number of player"))
            random_players = random_select_players(Players,nb_player)
            print("\nRandomly Selected Players:")
            print(format_table(random_players))
           
        elif request=="Team status":
            status=status_report(Players)
            print(status)
        elif request=="find the highest APT":
            player=find_highest_apt(Players)
            print(format_table([player]))
        elif request=="find the lowest AVG":
            player=find_lowest_avg(Players)
            print(format_table([player]))
        elif request=="Sort by APT":
            player=sort_by_apt(Players)
            print(format_table(player))
        elif request=="done":
            break

    

if __name__ =="__main__":
    main()
        
