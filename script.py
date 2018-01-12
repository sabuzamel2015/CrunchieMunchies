import codecademylib

import numpy as np


#generate CSV file
calorie_stats = np.genfromtxt('cereal.csv', delimiter =",")

#Finding the mean of calorie stats
average_calorie = np.mean(calorie_stats)

#Sort data in order to see if there is any potential outliers in our data
sorting_data = np.sort(calorie_stats)

#Find the median of calorie_stats. This is more accurate than mean for finding the average of a dataset
median_calorie = np.median(calorie_stats)

#This is the percentile of cereals that have over 100 calories. That is over 30 more than Yummy Corp's brand
calorie_percentile = np.percentile(calorie_stats, 39)

#This is the percentile of cereals that have 100 or more calories. That is 30 more than Yummy Corp's brand
high_calorie = np.percentile(calorie_stats, 18)

#This is the percentile that Crunchie_Munchies is in. Almost all of the cereals are less healthy than Yummy Corp's
Crunchie_Munchies = np.percentile(calorie_stats, 4)

#Finding the Standard Deviation of the dataset
calorie_std = np.std(calorie_stats)

#finding the difference of all the cereals within the first and third quartile
calorie_interquartile = np.percentile(calorie_stats, 75) -np.percentile(calorie_stats, 25)

print(average_calorie)
print(sorting_data)
print(median_calorie)
print(calorie_percentile)
print(high_calorie)
print(Crunchie_Munchies)
print(calorie_std)
print(calorie_interquartile)

# Based off of my findings, I can infer that the cereals of the competitors of Yummy Corps have a higher intake of calories per serving.

# 82 percent of the other cereal brands have 100 or more calories per serving. That is at least 30 calories more than Yummy Corp's CrunchieMunchies.

# 96 percent of Yummy Corp's competitors have a higher calorie intake than CrunchieMunchies. This should be mentioned when marketing the product.

