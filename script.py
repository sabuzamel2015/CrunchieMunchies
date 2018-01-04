import codecademylib

import numpy as np

import matplotlib as plt

calorie_stats = np.genfromtxt('cereal.csv', delimiter =",")

average_calorie = np.mean(calorie_stats)

sorting_data = np.sort(calorie_stats)

median_calorie = np.median(calorie_stats)

calorie_percentile = np.percentile(calorie_stats, 39)

high_calorie = np.percentile(calorie_stats, 18)

Crunchie_Munchies = np.percentile(calorie_stats, 4)

calorie_std = np.std(calorie_stats)

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

