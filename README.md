# Hacker Statistics
In this case study you are in the door of the empire state building. 
You through a dice 100 times:
  - if it's 1 or 2 you go one step down, 
  - if it's 3,4 or 5 you climb one step, 
  - if you throw a 6 you throw the dice again and will climb the resulting number in steps. 
There is 0.1% chance youre gonna fall down the stairs. 
Conditions: You can't go below step zero(0). 

Task: Calculate your chances you're gonna reach step 60 and make a bet with a friend

# Superbowl, TV and halftime shows
Analysing straight from wikipedia page.
      Super Bowl championships --> https://en.wikipedia.org/wiki/List_of_Super_Bowl_champions
      Super Bowl tv ratings --> https://en.wikipedia.org/wiki/Super_Bowl_television_ratings
      Halftime musicians data --> https://en.wikipedia.org/wiki/List_of_Super_Bowl_halftime_shows
In this project we get into an EDA regarding the results of the superbowl over time (combined points, score differences, blowouts etc)
and how this relates to other data, like the number of viewers and the quality of the halftime show.Specifically:
  - Visualising data of combined points
  - Visualising point differences. Also, checking for closest game(s) and biggest blowouts
  - Checking whether blowouts translate to lost viewers
  - Analysing viewership and the ad industry over time. Checking the ad cost over time and how the # of users relates to that
  - Counting halftime show appearances for each musician
  - Checking who performed the most songs in a halftime show
  
# The app market in google play
In this project we take a look at the android app market by using data straight from the Google Play website.
The data consist of two sets: one for the appstore and a second one for the reviews
https://www.kaggle.com/lava18/google-play-store-apps?select=googleplaystore.csv
https://www.kaggle.com/lava18/google-play-store-apps?select=googleplaystore_user_reviews.csv
In the 1st part we import and inspect the data, dropping duplicates, examining datas' types and check for missing values
In the 2nd part we clean the data, replacing unecessary characters with 'space' and prepare the data for analysis
In the 3rd part we analyse the general characteristics of the data, specifically:
  - Explore the different app categories
  - Checking the distribution of the ratings
  - Go deeper in the relationship between several characteristics like: price vs category & Free vs non-free apps
