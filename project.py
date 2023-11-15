from data_loader import DataLoader
from my_module import Plotting
from my_module import StadiumAnalysis
from my_module import TabularAnalysis

def main():
    file_path = "t20-world-cup-22.csv"
    data_loader = DataLoader(file_path)
    
    plotting = Plotting(data_loader.data)
    stadium_plotting=StadiumAnalysis(data_loader.data)
    Table=TabularAnalysis(data_loader.data)
    
    while True:
        print("\nChoose an option:")
        print("1. Plot Team Wins")
        print("2. Plot Matches Won by Runs or Wickets")
        print("3. Plot Top Scorers")
        print("4. Plot Player of the Match")
        print("5. Plot Best Bowlers")
        print("6. Plot Stadiums to Bat or Chase")
        print("7. Plot Stadiums to Bowl or Defend")
        print("8. Display Relevant Data Tables")
        print("0. Exit")

        choice = input("Enter your choice (0-8): ")

        if choice == "0":
            print("Exiting the program. Goodbye!")
            break
        elif choice == "1":
            plotting.plot_team_wins()
        elif choice == "2":
            plotting.plot_matches_won_by_runs_or_wickets()
        elif choice == "3":
            num_players = int(input("Enter the number of top scorers to display: "))
            plotting.plot_top_scorers(num_players)
        elif choice == "4":
            
            plotting.plot_player_of_the_match()
        elif choice == "5":
            
            plotting.plot_best_bowlers()
        elif choice == "6":
            stadium_plotting.plot_best_stadiums_batting()
    
        elif choice == "7":
            stadium_plotting.plot_stadiums_to_bowl_or_defend()
        elif choice == '8':
            print("\nChoose an option:")
            print("1. Team Wins")
            
            print("2. Top Scorers")
            print("3. Player of the Match")
           
            print("4. Stadiums ")
            
            print("0. Exit")
            choice = input("Enter your choice (0-4): ")

            if choice == "0":
                print("Exiting the program. Goodbye!")
                break
            elif choice == "1":
                 Table.display_team_wins_table()
            
            elif choice == "2":
                
                Table.display_top_scorers_table()
            elif choice == "3":
                
                Table.display_player_of_the_match_table()
           
            elif choice == "4":
               Table.display_stadiums_table()
            
            else:
                print("Invalid choice. Please enter a number between 0 and 4.")
            
        else:
            print("Invalid choice. Please enter a number between 0 and 8.")

if __name__ == "__main__":
    main()