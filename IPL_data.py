# python3 ShubhangiLamkhade/friday_challenge.py

import pandas as pd

data_csv1 = pd.read_csv('/home/shubhangi/Downloads/archive (2)/archive/IPL Ball-by-Ball 2008-2020.csv')
# print(data_csv1) 

data_csv2 = pd.read_csv('/home/shubhangi/Downloads/archive (2)/archive/IPL Matches 2008-2020.csv')
# print(data_csv2)

# faced the first and last ball in IPL
def first_last_ball():
    first_batsman = df.sort_values(["id","inning", "over", "ball"], ascending=True).head(1)
    last_batsman = df.sort_values(["id","inning", "over", "ball"], ascending=False).head(1)
    return(first_batsman,last_batsman)
    print(first_last_ball(data_csv1))
    # print("Last ball faced by:\n\n" ,last_batsman.head(1))

# high and low scorer batsman:
def high_low_score_batsman():
    data = data_csv1.groupby('batsman').sum()
    Highest_scorer = data.sort_values(["batsman_runs"], ascending=False)
    scores = data_csv1.groupby('batsman').sum()
    Lowest_scorer = scores.sort_values(["batsman_runs"], ascending=True)
    print("Highest and lowest score Batmans are:\n", high_low_score_batsman)


#Total matches played per season
def total_matches_per_season():
    clm_add = data_csv2["Seasons"]=pd.DatetimeIndex(data_csv2["date"]).year
    total_match_per_season = data_csv2.groupby(['Seasons'])['id'].count().reset_index().rename(columns={'id':'Total_matches'})
    print("Tatal matches per season are:\n" ,total_matches_per_season)
    

# Total runs scored per season
def total_run_per_season():
    ball_details = data_csv1
    IPL_details = data_csv2[['id', 'Seasons']].merge(ball_details, left_on='id', right_on='id', how='left')
    Total_runs = IPL_details.groupby(['Seasons'])['total_runs'].sum().reset_index()
    print("\nTotal runs scored per season are:\n" ,total_run_per_season)

# Toss winners of all matches in ascending order
def toss_win():
    Toss_winners = data_csv2["toss_winner"].value_counts(ascending=True)
    print("\nToss winners are:\n" ,toss_win)

first_last_ball(data_csv1)