import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

class Plotting:
    def __init__(self, data):
        self.data = data

    
    def plot_print_data(self):
        print(self.data.head())
    def plot_team_wins(self):
        
        winner_counts = self.data['winner'].value_counts()

    # Set the style using seaborn
        sns.set(style="whitegrid")

        # Create a bar plot with seaborn
        plt.figure(figsize=(12, 6))
        bar_plot = sns.barplot(x=winner_counts.index, y=winner_counts.values, palette="viridis")

        # Add labels and title
        plt.xlabel('Teams', fontsize=14)
        plt.ylabel('Number of Matches Won', fontsize=14)
        plt.title('Number of Matches Won by Teams in T20 World Cup 2022', fontsize=16)

        # Rotate x-axis labels for better readability
        bar_plot.set_xticklabels(bar_plot.get_xticklabels(), rotation=45, horizontalalignment='right')

        # Add data labels on top of the bars
        for p in bar_plot.patches:
            bar_plot.annotate(f'{p.get_height()}', (p.get_x() + p.get_width() / 2., p.get_height()),
                            ha='center', va='center', fontsize=12, color='black', xytext=(0, 5),
                            textcoords='offset points')

        # Show the plot
        plt.show()

    def plot_matches_won_by_runs_or_wickets(self):
       
        won_by = self.data["won by"].value_counts()
        labels = won_by.index
        counts = won_by.values
        colors = ['gold', 'lightgreen']
       
        fig, ax = plt.subplots()
        wedges, texts, autotexts = ax.pie(counts, labels=labels, autopct='%1.1f%%',
                                      colors=colors, startangle=90, wedgeprops=dict(width=0.3))


        ax.axis('equal')

        # Add a legend with count and percentage
        legend_labels = [f'{label} ({count})' for label, count in zip(labels, counts)]
        ax.legend(wedges, legend_labels, title="Counts", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

        plt.title('Number of Matches Won By Runs Or Wickets')
        plt.show()


    def plot_toss_decisions(self):
       
        toss = self.data["toss decision"].value_counts()
        labels = toss.index
        counts = toss.values
        colors = ['skyblue', 'yellow']

        fig, ax = plt.subplots()
        wedges, texts, autotexts = ax.pie(counts, labels=labels, autopct='%1.1f%%',colors=colors, startangle=90, wedgeprops=dict(width=0.3))


        ax.axis('equal')

        # Add a legend with count and percentage
        legend_labels = [f'{label} ({count})' for label, count in zip(labels, counts)]
        ax.legend(wedges, legend_labels, title="Counts", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

        plt.title('Toss Decisions in T20 World Cup 2022')
        plt.show()


    
    def plot_top_scorers(self, num_players=5):
       

        top_scorers = self.data.groupby('top scorer')['highest score'].max().nlargest(num_players)

        # Set the style using seaborn
        sns.set(style="whitegrid")

        # Create a bar plot with seaborn
        plt.figure(figsize=(12, 6))
        bar_plot = sns.barplot(x=top_scorers.index, y=top_scorers.values, palette="Blues_d")

        # Add labels and title
        plt.xlabel('Top Scorers', fontsize=14)
        plt.ylabel('Highest Score', fontsize=14)
        plt.title(f'Top {num_players} Scorers in T20 World Cup 2022', fontsize=16)

        # Rotate x-axis labels for better readability
        bar_plot.set_xticklabels(bar_plot.get_xticklabels(), rotation=45, horizontalalignment='right')

        # Add data labels on top of the bars
        for p in bar_plot.patches:
            bar_plot.annotate(f'{p.get_height()}', (p.get_x() + p.get_width() / 2., p.get_height()),
                            ha='center', va='center', fontsize=12, color='black', xytext=(0, 5),
                            textcoords='offset points')

        # Show the plot
        plt.show()
    def plot_player_of_the_match(self, num_players=10):
       
    
        player_of_match_counts = self.data['player of the match'].value_counts()

    # Set the style using seaborn
        sns.set(style="whitegrid")

        # Create a bar plot with seaborn
        plt.figure(figsize=(12, 6))
        bar_plot = sns.barplot(x=player_of_match_counts.index, y=player_of_match_counts.values, palette="Set2")

        # Add labels and title
        plt.xlabel('Players', fontsize=14)
        plt.ylabel('Number of Player of the Match Awards', fontsize=14)
        plt.title('Players with Player of the Match Awards', fontsize=16)

        # Rotate x-axis labels for better readability
        bar_plot.set_xticklabels(bar_plot.get_xticklabels(), rotation=45, horizontalalignment='right')

        # Add data labels on top of the bars
        for p in bar_plot.patches:
            bar_plot.annotate(f'{p.get_height()}', (p.get_x() + p.get_width() / 2., p.get_height()),
                            ha='center', va='center', fontsize=12, color='black', xytext=(0, 5),
                            textcoords='offset points')

        # Show the plot
        plt.show()
    def plot_best_bowlers(self):
       
        best_bowlers = self.data['best bowler'].value_counts()

    # Set the style using seaborn
        sns.set(style="whitegrid")

        # Create a bar plot with seaborn
        plt.figure(figsize=(12, 6))
        bar_plot = sns.barplot(x=best_bowlers.index, y=best_bowlers.values, palette="viridis")

        # Add labels and title
        plt.xlabel('Best Bowlers', fontsize=14)
        plt.ylabel('Number of Best Bowling Figures', fontsize=14)
        plt.title('Best Bowlers in T20 World Cup 2022', fontsize=16)

        # Rotate x-axis labels for better readability
        bar_plot.set_xticklabels(bar_plot.get_xticklabels(), rotation=45, horizontalalignment='right')

        # Add data labels on top of the bars
        for p in bar_plot.patches:
            bar_plot.annotate(f'{p.get_height()}', (p.get_x() + p.get_width() / 2., p.get_height()),
                            ha='center', va='center', fontsize=12, color='black', xytext=(0, 5),
                            textcoords='offset points')

        # Show the plot
        plt.show()
    

    
    
class StadiumAnalysis:
    def __init__(self, data):
        self.data = data
    def plot_best_stadiums_batting(self):
        fig, ax = plt.subplots()

        bar_width = 0.35
        index = np.arange(len(self.data["venue"]))

        first_innings_bar = ax.bar(index, self.data["first innings score"], bar_width, label='First Innings Runs', color='blue')
        second_innings_bar = ax.bar(index + bar_width, self.data["second innings score"], bar_width, label='Second Innings Runs', color='red')

        ax.set_xticks(index + bar_width / 2)
        ax.set_xticklabels(self.data["venue"], rotation=-70, ha='left')
        ax.set_title('Best Stadiums to Bat First or Chase')
        ax.legend()

        plt.tight_layout()
        plt.show()
    def plot_stadiums_to_bowl_or_defend(self):
        fig, ax = plt.subplots()
    
        bar_width = 0.35
        index = np.arange(len(self.data["venue"]))
    
        first_innings_bar = ax.bar(index, self.data["first innings wickets"], bar_width, label='First Innings Wickets', color='blue')
        second_innings_bar = ax.bar(index + bar_width, self.data["second innings wickets"], bar_width, label='Second Innings Wickets', color='red')
    
        ax.set_xticks(index + bar_width / 2)
        ax.set_xticklabels(self.data["venue"], rotation=-70, ha='left')
        ax.set_title('Best Stadiums to Bowl First or Defend')
        ax.legend()
    
        plt.tight_layout()
        plt.show()
class TabularAnalysis:
    def __init__(self, data):
        self.data = data
    
    def display_team_wins_table(self):
        team_wins_table = self.data['winner'].value_counts().reset_index()
        team_wins_table.columns = ['Team', 'Number of Matches Won']
        print("\nTeam Wins Table:")
        print(team_wins_table)

    def display_top_scorers_table(self, num_players=5):
        top_scorers_table = self.data.groupby('top scorer')['highest score'].max().nlargest(num_players).reset_index()
        top_scorers_table.columns = ['Player', 'Highest Score']
        print(f"\nTop {num_players} Scorers Table:")
        print(top_scorers_table)

    def display_player_of_the_match_table(self, num_players=5):
        player_of_match_table = self.data['player of the match'].value_counts().nlargest(num_players).reset_index()
        player_of_match_table.columns = ['Player', 'Number of Player of the Match Awards']
        print(f"\nTop {num_players} Players with Player of the Match Awards Table:")
        print(player_of_match_table)
    def display_stadiums_table(self):
        stadiums_table = self.data[['venue', 'first innings score', 'second innings score', 'first innings wickets', 'second innings wickets']]
        print("\nStadiums Data Table:")
        print(stadiums_table)    