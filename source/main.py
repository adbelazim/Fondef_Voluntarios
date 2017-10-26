import os
import json
import pandas as pd
import time

import utils
import binarization
import ranking
import pre_process
import create_json

def main(path):
	args = utils.get_args()

	filename = path + "/Data/" + args.filename
	
	#read data
	xls_data = binarization.read_xls(filename)
	#drop columns
	xls_reduce_data = utils.reduce_data(xls_data)
	
	#scores_xls, columns_xls = ranking.get_ranking(xls_reduce_data)
	#create_json.ranking_json(scores_xls, columns_xls, path, "pre_process_ranking.json")

	process_data = pre_process.pre_process(xls_data, args)
	process_data.to_csv(path + "/Data/process_data.csv")
	create_json.create_json_categories(process_data, path)
	
	

	scores_ranking, columns_ranking = ranking.get_ranking(process_data)
	create_json.ranking_json(scores_ranking, columns_ranking, path, "after_process_ranking.json")
	
	columns = list(process_data.columns.values)
	print("columns", columns)

	start = time.time()
	binar_data = pd.DataFrame()
	for column in columns:
	 	print("process column: ", column)
	 	binar_column = binarization.process_column(process_data[str(column)], column, args)
	 	binar_data = pd.concat([binar_data, binar_column], axis = 1)
	 	#binar_data[column] = binar_df

	end = time.time()
	print("binarizacion demoro", end-start)
	print(binar_data)
	binar_data.to_csv(path + "/Data/binar_data.csv")





if __name__ == "__main__":
	path = os.getcwd()
	path_env, path_source = os.path.split(path)
	main(path_env)







