import math
import pandas as pd

def get_ranking(df_data):
	#get the columns in data frame
	columns = list(df_data.columns.values)

	scores = []
	for column in columns:
		#print("score of column", column)
		#get levels and frecuency of each one per column
		levels = df_data[column].value_counts().index.tolist()
		frecuencies = df_data[column].value_counts().values.tolist()

		score = entropy(levels, frecuencies, df_data.shape[0])

		scores.append(score)

	return scores, columns


def entropy(levels, frecuencies, len_data):

	number_levels = len(levels)
	total_sum = []
	for i in range(0, number_levels):
		prob = float(frecuencies[i])/float(len_data)
		entropy_level = float(prob)*(math.log(float(prob)))
		total_sum.append(entropy_level)

	return (1/math.log(number_levels))*sum(total_sum)