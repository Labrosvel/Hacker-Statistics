'''Superbowl. Analysing data straight from wikipedia page. Specifically:
    Super Bowl championships --> https://en.wikipedia.org/wiki/List_of_Super_Bowl_champions
    Super Bowl tv ratings --> https://en.wikipedia.org/wiki/Super_Bowl_television_ratings
    Halftime musicians data --> https://en.wikipedia.org/wiki/List_of_Super_Bowl_halftime_shows
'''

# Loading and reading the data
import pandas as pd
import matplotlib.pyplot as plt

super_bowls = pd.read_csv('super_bowls.csv')
tv = pd.read_csv('tv.csv')
halftime_musicians = pd.read_csv('halftime_musicians.csv')

display(super_bowls.head())
display(tv.head())
display(halftime_musicians.head())

# Inspecting the data
super_bowls.info()
print('\n')
tv.info()
print('\n')
halftime_musicians.info()

# Exploratory Data Analysis
# Visualising data of combined points. Also check for highest and lowest scores.
from matplotlib import pyplot as plt 
plt.hist(super_bowls['combined_pts'])
plt.xlabel('Combined Points')
plt.ylabel('Number of Super Bowls')
plt.show()
display(super_bowls[super_bowls['combined_pts'] > 70])
display(super_bowls[super_bowls['combined_pts'] < 25])

# Visualising point differences. Also check for closest game(s) and biggest
# blowouts 
plt.hist(super_bowls.difference_pts)
plt.xlabel('Point Difference')
plt.ylabel('Number of Super Bowls')
plt.show()
display(super_bowls[super_bowls['difference_pts']==1])
display(super_bowls[super_bowls['difference_pts']>=35])

#Check whether blowouts translate to lost viewers
games_tv = pd.merge(tv[tv['super_bowl'] > 1], super_bowls, on='super_bowl')
import seaborn as sns
sns.regplot(x='difference_pts', y='share_household', data=games_tv)


#Analysing Viewership and the ad industry over time. Today's 30sec spot
#costs $5m. Check how was it in the past and how the # of users relates to that
#or the household rating
import matplotlib.pyplot as plt
plt.subplot(3, 1, 1)
plt.plot(super_bowls['super_bowl'], tv.avg_us_viewers, color='blue')
plt.title('Average Number of US Viewers')

plt.subplot(3, 1, 2)
plt.plot(super_bowls['super_bowl'], tv['rating_household'], color='#DC267F')
plt.title('Household Rating')

plt.subplot(3, 1, 3)
plt.plot(super_bowls['super_bowl'], tv['ad_cost'], color='#FFB000')
plt.title('Ad Cost')

plt.xlabel('SUPER BOWL')
plt.tight_layout()


# All halftime musicians for Super Bowls up to and including Super Bowl XXVII
display(halftime_musicians[halftime_musicians['super_bowl']<=27])


# Count halftime show appearances for each musician and sort them 
# from most to least
halftime_appearances = halftime_musicians.groupby('musician').count()['super_bowl'].reset_index()
halftime_appearances = halftime_appearances.sort_values('super_bowl', ascending=False)
display(halftime_appearances[halftime_appearances['super_bowl']>=2])


# Who permormed the most songs in a halftime show
no_bands = halftime_musicians[~halftime_musicians.musician.str.contains('Marching')]
no_bands = no_bands[~no_bands.musician.str.contains('Spirit')]

most_songs = int(max(no_bands['num_songs'].values))
plt.hist(no_bands.num_songs.dropna(), bins=most_songs)
plt.xlabel('Number of Songs Per Halftime Show Performance')
plt.ylabel('Number of Musicians')
plt.show()

no_bands = no_bands.sort_values('num_songs', ascending=False)
display(no_bands.head(15))





