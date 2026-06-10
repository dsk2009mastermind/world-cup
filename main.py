import random
import numpy as np
import pandas as pd
from dataclasses import dataclass
from datetime import datetime

cup_groups = {
    "A": ["Mexico", "South Africa", "South Korea", "Czechia"],
    "B": ["Canada", "Bosnia and Herzegovina", "Qatar", "Switzerland"],
    "C": ["Brazil", "Morocco", "Haiti", "Scotland"],
    "D": ["USA", "Paraguay", "Turkiye", "Australia"],
    "E": ["Germany", "Curaçao", "Ivory Coast", "Ecuador"],
    "F": ["Netherlands", "Japan", "Sweden", "Tunisia"],
    "G": ["Belgium", "Egypt", "Iran", "New Zealand"],
    "H": ["Spain", "Cabo Verde", "Saudi Arabia", "Uruguay"],
    "I": ["France", "Senegal", "Iraq", "Norway"],
    "J": ["Argentina", "Algeria", "Austria", "Jordan"],
    "K": ["Portugal", "DR Congo", "Uzbekistan", "Colombia"],
    "L": ["England", "Croatia", "Ghana", "Panama"],
}

team_stats = {
    # Group A
    "Mexico": {"rating": 82},
    "South Africa": {"rating": 71},
    "South Korea": {"rating": 78},
    "Czechia": {"rating": 76},
    
    # Group B
    "Canada": {"rating": 79},
    "Bosnia and Herzegovina": {"rating": 74},
    "Qatar": {"rating": 65},
    "Switzerland": {"rating": 81},
    
    # Group C
    "Brazil": {"rating": 94},
    "Morocco": {"rating": 83},
    "Haiti": {"rating": 61},
    "Scotland": {"rating": 75},
    
    # Group D
    "USA": {"rating": 80},
    "Paraguay": {"rating": 72},
    "Turkiye": {"rating": 77},
    "Australia": {"rating": 76},
    
    # Group E
    "Germany": {"rating": 91},
    "Curaçao": {"rating": 68},
    "Ivory Coast": {"rating": 70},
    "Ecuador": {"rating": 73},
    
    # Group F
    "Netherlands": {"rating": 88},
    "Japan": {"rating": 79},
    "Sweden": {"rating": 82},
    "Tunisia": {"rating": 72},
    
    # Group G
    "Belgium": {"rating": 87},
    "Egypt": {"rating": 74},
    "Iran": {"rating": 69},
    "New Zealand": {"rating": 71},
    
    # Group H
    "Spain": {"rating": 90},
    "Cabo Verde": {"rating": 66},
    "Saudi Arabia": {"rating": 63},
    "Uruguay": {"rating": 85},
    
    # Group I
    "France": {"rating": 93},
    "Senegal": {"rating": 80},
    "Iraq": {"rating": 67},
    "Norway": {"rating": 77},
    
    # Group J
    "Argentina": {"rating": 92},
    "Algeria": {"rating": 75},
    "Austria": {"rating": 81},
    "Jordan": {"rating": 64},
    
    # Group K
    "Portugal": {"rating": 86},
    "DR Congo": {"rating": 68},
    "Uzbekistan": {"rating": 70},
    "Colombia": {"rating": 84},
    
    # Group L
    "England": {"rating": 89},
    "Croatia": {"rating": 83},
    "Ghana": {"rating": 73},
    "Panama": {"rating": 62},

    #all stats are AI-generated for hypothetical purposes
}

point_count = {
    # Group A
    "Mexico": 0,
    "South Africa": 0,
    "South Korea": 0,
    "Czechia": 0,
    
    # Group B
    "Canada": 0,
    "Bosnia and Herzegovina": 0,
    "Qatar": 0,
    "Switzerland": 0,
    
    # Group C
    "Brazil": 0,
    "Morocco": 0,
    "Haiti": 0,
    "Scotland": 0,
    
    # Group D
    "USA": 0,
    "Paraguay": 0,
    "Turkiye": 0,
    "Australia": 0,
    
    # Group E
    "Germany": 0,
    "Curaçao": 0,
    "Ivory Coast": 0,
    "Ecuador": 0,
    
    # Group F
    "Netherlands": 0,
    "Japan": 0,
    "Sweden": 0,
    "Tunisia": 0,
    
    # Group G
    "Belgium": 0,
    "Egypt": 0,
    "Iran": 0,
    "New Zealand": 0,
    
    # Group H
    "Spain": 0,
    "Cabo Verde": 0,
    "Saudi Arabia": 0,
    "Uruguay": 0,
    
    # Group I
    "France": 0,
    "Senegal": 0,
    "Iraq": 0,
    "Norway": 0,
    
    # Group J
    "Argentina": 0,
    "Algeria": 0,
    "Austria": 0,
    "Jordan": 0,
    
    # Group K
    "Portugal": 0,
    "DR Congo": 0,
    "Uzbekistan": 0,
    "Colombia": 0,
    
    # Group L
    "England": 0,
    "Croatia": 0,
    "Ghana": 0,
    "Panama": 0,
}

def simulate_match(team1, team2):
    #simulates a match and returns the winner based on rating probabilities
    total = team_stats[team1]["rating"] + team_stats[team2]["rating"]
    team1_probability = team_stats[team1]["rating"]/total
    team2_probability = team_stats[team2]["rating"]/total
    draw_prob = 0.1
    w1 = (team1_probability * (1 - draw_prob)) #decreases win prob for 1
    w2 = (team2_probability * (1 - draw_prob)) #decreases win prob for 2
    outcome = random.choices([team1, team2, "draw"], weights=[w1, w2, draw_prob], k=1)[0]
    return outcome

def simulate_points(winner, loser):
    #assigns points based on match outcome
    if winner == simulate_match(winner, loser):
        return 3
    elif winner == "draw":
        return 1
    else:
        return 0

def simulate_group_stage():
    #simulates the group stages
    # iterate over the groups' team lists (cup_groups is a dict)
    for teams in cup_groups.values():
        for j in range(len(teams)):
            for k in range(j+1, len(teams)):
                team1 = teams[j]
                team2 = teams[k]
                winner = simulate_match(team1, team2)
                if winner == team1:
                    point_count[team1] += 3
                elif winner == team2:
                    point_count[team2] += 3
                else:
                    point_count[team1] += 1
                    point_count[team2] += 1

def group_standings():
    #calculates total standings after group stage
    group_standings = {}

#gets the group and teams from cup_groups, then creates a list of tuples based on point count
    for group, teams in cup_groups.items():
        group_teams = [(team, point_count[team]) for team in teams]
        #sorts the tuples in descending order based on points
        sorted_group = sorted(group_teams, key=lambda x: x[1], reverse=True)
        group_standings[group] = sorted_group

    return group_standings

def find_knockout_teams(group_standings):
    top_teams = []
    third_places = []
    third_sorted = []
    for group, standings in group_standings.items():
        top_teams.append(standings[0][0])
        top_teams.append(standings[1][0])
        # collect third-place teams (team, points, group)
        third = standings[2]
        third_places.append((third[0], third[1], group))
        third_sorted = sorted(third_places, key=lambda x: (x[1], x[0]), reverse=True)
        best_thirds = [t for t, pts, g in third_sorted[:8]]
    # return flat list: 24 automatic qualifiers + 8 best third-placed teams = 32
    return top_teams + best_thirds

def simulate_knockout_stage(knockout_teams):
    #simulates the knockout stages
    next_round = []
    #round of 32
    for j in range(0, len(knockout_teams), 2):
        g1 = knockout_teams[j] # group of first team
        g2 = knockout_teams[j+1] # group of second team
        team1 = g1 # first team from group
        team2 = g2 # first team from next group
        winner = simulate_match(team1, team2)
        if winner == "draw":
            winner = random.choice([team1, team2]) # randomly select a winner in case of a draw
        #print(f"Round of 32: {team1} vs {team2} - Winner: {winner}")
        next_round.append(winner)
    
    #sets knockout_teams to the winners of the round of 32 for the next round
    knockout_teams = next_round
    next_round = []

    #round of 16
    for j in range(0, len(knockout_teams), 2):
        team1 = knockout_teams[j]
        team2 = knockout_teams[j+1]
        winner = simulate_match(team1, team2)
        if winner == "draw":
            winner = random.choice([team1, team2]) # randomly select a winner in case of a draw
        #print(f"Round of 16: {team1} vs {team2} - Winner: {winner}")
        next_round.append(winner)

    knockout_teams = next_round
    next_round = []

#quarters
    for j in range(0, len(knockout_teams), 2):
        team1 = knockout_teams[j]
        team2 = knockout_teams[j+1]
        winner = simulate_match(team1, team2)
        if winner == "draw":
            winner = random.choice([team1, team2]) # randomly select a winner in case of a draw
        #print(f"Quarterfinals: {team1} vs {team2} - Winner: {winner}")
        next_round.append(winner)

    knockout_teams = next_round
    next_round = []

#semis
    for j in range(0, len(knockout_teams), 2):
        team1 = knockout_teams[j]
        team2 = knockout_teams[j+1]
        winner = simulate_match(team1, team2)
        if winner == "draw":
            winner = random.choice([team1, team2]) # randomly select a winner in case of a draw
        #print(f"Semifinals: {team1} vs {team2} - Winner: {winner}")
        next_round.append(winner)

    knockout_teams = next_round
    next_round = []
#final
    team1 = knockout_teams[0]
    team2 = knockout_teams[1]
    winner = simulate_match(team1, team2)
    if winner == "draw":
        winner = random.choice([team1, team2]) # randomly select a winner in case of a draw
    #print(f"Final: {team1} vs {team2} - Winner: {winner}")
    #print(f"The winner of the World Cup is: {winner}")
    return winner


winners = []

for i in range(100):
    simulate_group_stage()
    standings = group_standings()
    teams = find_knockout_teams(standings)
    winner = simulate_knockout_stage(teams)
    winners.append(winner)

#count the number of wins for each team
winner_counts = pd.Series(winners).value_counts()

#print the top 10 common winners and their probabilities
winner_probabilities = (winner_counts / 100).head(10)
print("Top 10 Most Common Winners and Their Probabilities:")
print(winner_probabilities)

