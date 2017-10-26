import json
import pandas as pd

import utils

	
def append_data_dict(list_to_append, dict_data):
	for element in dict_data:
		list_to_append.append(element)

def create_column_json(levels, frecuencies, column, binar):

	if binar:
		list_levels = [{"atributo_original": column,"name": column ,"binar": binar}]

	else:
		list_levels = [{"atributo_original": column,"name": level ,"frecuency": frecuency, "binar": binar} \
		for level, frecuency in zip(levels, frecuencies)]
	
	return list_levels


def ranking_json(scores, columns, path, filename):

	list_ranking = [{"atributo_original": column, "score": score} for column, score in zip(columns, scores)]

	list_ranking = sorted(list_ranking, key=lambda k: k['score']) 

	#print("list ranking",list_ranking)
	with open(path + "/Data/"+ filename, 'w') as f:
		f.write(json.dumps(list_ranking, f))


def create_json_categories(df_data, path):
	#get the columns in data frame
	columns = list(df_data.columns.values)

	list_categories = []
	for column in columns:
		#get levels per column
		levels = df_data[column].value_counts().index.tolist()
		frecuencies = df_data[column].value_counts().values.tolist()

		#check if the column is a binar category
		binar = utils.check_binar(utils.to_lower(df_data[column].value_counts().index.tolist()))

		#create dict of levels and categories
		dict_levels = create_column_json(levels, frecuencies, column, binar)
		#add every item in the dict to a list
		append_data_dict(list_categories, dict_levels)

	#print("list categories",list_categories)
	with open(path + "/Data/categories.json", 'w') as f:
		f.write(json.dumps(list_categories, f))








