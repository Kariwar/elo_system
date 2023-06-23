import math
from app import member_1_t2, member_1_t1, member_2_t2, member_2_t1


def expected_score(rating_winner, rating_looser):
    """
    Calculates the expected score of player 1 against player 2 using the Elo rating system.

    Args:
        rating1 (float): The rating of player 1.
        rating2 (float): The rating of player 2.
        k_factor (int, optional): The K-factor used to adjust the amount the rating changes. Defaults to 32.

    Returns:
        float: The expected score of player 1.
    """
    return round((36 / (1 + math.exp((rating_winner - rating_looser) / 400))) + 2, 0)

def update_score(player1_rating, player2_rating, player3_rating, player4_rating, winner):
  team1_rating = player1_rating + player2_rating
  team2_rating = player3_rating + player4_rating
  if(winner == 1) :
    won_score = expected_score(team1_rating, team2_rating)
    player1_rating += won_score
    player2_rating += won_score
    player3_rating -= won_score
    player4_rating -= won_score
  else :
    won_score = expected_score(team2_rating, team1_rating)
    player3_rating += won_score
    player4_rating += won_score
    player1_rating -= won_score
    player2_rating -= won_score
  return     player1_rating, player2_rating, player3_rating,player4_rating

# Example usage
player1_rating = 1200
player2_rating = 1600
player3_rating = 1000
player4_rating = 1000

team1_rating = player1_rating + player2_rating
team2_rating = player3_rating + player4_rating

update_score(player1_rating, player2_rating, player3_rating,player4_rating, 1)

