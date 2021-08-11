


import math
import csv
from operator import itemgetter
from pprint import pprint

def csv_to_list_of_dicts(csv_file_to_convert):
    

    list_of_dicts = []

    with open(csv_file_to_convert) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            list_of_dicts.append(line)

    return list_of_dicts



player_score = csv_to_list_of_dicts("game_scores.csv")


#for player in player_score:
    #player["score"] = int(player["score"])

# Sort 
players_by_scores = sorted(player_score, key=itemgetter("score"))

def score1(players_by_score):


    total=0
    count=0

    for scores in players_by_scores:
        score = int(scores["score"])
        total+= score
        count+=1
        #break
    average = total /count
    print(average)
    print(total)
    print(count)
score1(players_by_scores)

lowest_score_player = players_by_scores [0]
scorel = lowest_score_player["score"]
print(scorel)


highest_score_player = players_by_scores [-1]
scoreh = highest_score_player["score"]
print(scoreh)

#print(players_by_scores)

#average_score = players_by_scores (sum / len)
#sum1 = sum(players_by_scores)
#len1 =len(players_by_scores)

#print(average_score)


#max_score = max(players_by_scores)
#print(max_score)
#max_score = players_by_scores[-1]

#min_score = min(players_by_scores)
#print(min_score)


"""for player in players_by_scores:
   

    print(f"\nAverage score is {sum / count:.2f}")"""

    

    