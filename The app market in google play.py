#Import and inspect the data
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
apps_with_duplicates = pd.read_csv('apps.csv')
apps=apps_with_duplicates.drop_duplicates()

print('Total number of apps in the dataset = ', len(apps) )
print('\n')
print(apps.info())
print('\n')
print(apps.sample(n=5))

#Clean the data
cols_to_clean = ['Installs', 'Price'] 
chars_to_remove = ['+', ',' ,'Free', '$', 'Everyone']

for col in cols_to_clean:
    for char in chars_to_remove:
        apps.loc[:, col] = apps.loc[:, col].astype(str).str.replace(char, '')
    apps.loc[:, col]=pd.to_numeric(apps.loc[:, col])
 
print(apps.info())
print('\n')

# Do an EDA of app categories
num_categories = len(apps['Category'].unique())
print('Number of categories = ', num_categories)
num_apps_in_category = apps['Category'].value_counts().sort_values(ascending = False)
num_apps_in_category.plot(kind='bar', rot=270)
plt.show()


#Do an EDA of app Ratings 
avg_app_rating = apps['Rating'].mean()
print('Average app rating = ', avg_app_rating)
x=apps['Rating']
plt.hist(x, bins=30, range=(0.5,5.5))
plt.axvline(x.mean(), color='k', linestyle='dashed', linewidth=1)

#Explore further the relation between app's price and app's category
popular_app_cats = apps[apps.Category.isin(['GAME', 'FAMILY', 'PHOTOGRAPHY',
                                            'MEDICAL', 'TOOLS', 'FINANCE','LIFESTYLE','BUSINESS'])]
plt.subplot(2,1,1)
sns.stripplot(x = 'Price', y ='Category', data=popular_app_cats, jitter=True, orient= 'h', size=3)
plt.title('App pricing trend across categories')

# Select only apps priced below $100
apps_under_100 = popular_app_cats[popular_app_cats['Price']<100]
plt.subplot(2,1,2)
sns.stripplot(x = 'Price', y ='Category', data=apps_under_100, jitter=True, orient= 'h', size=3)
plt.title('App pricing trend across categories after filtering for junk apps')
plt.tight_layout()

#Explore further the relation between the type of the app and it's popularity
print(apps['Type'].value_counts())
apps.loc[:, 'Type']=apps.loc[:, 'Type'].astype(str).str.replace('0', 'Free')
print(apps['Type'].value_counts())
apps.boxplot(column='Installs', by='Type')














