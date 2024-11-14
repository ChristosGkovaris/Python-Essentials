def find_winner(player_scores):
    # Calculate the average score for each player
    averages = {player: sum(scores) / len(scores) for player, scores in player_scores.items()}

    # Find the player with the highest average score
    winner = max(averages, key=averages.get)

    # Get the highest average score
    highest_avg_score = averages[winner]

    return winner, highest_avg_score

# players_score.keys ==> 100, 101, 102, 103, 104, 105
# players_score.values ==> Carrot, Chocolate, Strawberry, Spice, Vanilla
players_score = { 'Arthur': [85, 90, 92], 'Bela': [75, 80, 85], 'Carol': [90, 92, 95], 'Deepak': [87, 89, 91] }

# Call the function and start the action
results = find_winner(players_score)
print(f"Winner: {results[0]}\nAverage Score: {results[1]:.2f}")




# ====================================================
# Solution 2

# Starting average score is 0
# highest_average_score = 0

# Starting average player is NONE
# highest_average_player = ""

# Loop through the players and the scores
# for player, scores in players_score.items():
    
    # calculate the average scores
    # avg = sum(scores) / len(scores)
    
    # Check which is greater
    # if avg > highest_average:
        
        # Assign new values
        # highest_average_score = avg
        # highest_average_player = player

# Return the desired output, based on the data
# return [highest_average_player, highest_average_score]
# ====================================================