import pandas as pd
import numpy as np

import utils


def read_xls(filename):
   """Read data with pandas like excel file.

   Parametros:
   filename -- archivo .xls para leer. Se considera que existe una sola hoja en el archivo.

   Esta funcion retorna una matriz con los datos 
   etiquetados segun el nombre de la columna.
   
   """

   print("Load file...")
   xls = pd.ExcelFile(filename)
   sheetX = xls.parse(0) #2 is the sheet number
   print("Uploaded file")
   return sheetX

def binar_column(list_data, categories, column_name):

	initialize_data = np.zeros((len(list_data),len(categories)), dtype = np.int32)

	binar_data = pd.DataFrame(data = initialize_data, columns = list(categories), index = np.arange(len(list_data)))

	for category in categories:
		for i in range(0, len(list_data)):
			if unicode(list_data[i]).lower() == category:
				binar_data.set_value(i, category, 1)

	return binar_data

def simple_binarization(list_data, categories, column_name):

	initialize_data = np.zeros((len(list_data),), dtype = np.int32)
	binar_data = pd.DataFrame(data = initialize_data, columns = [column_name], index = np.arange(len(list_data)))

	i = 0
	for element in list_data:
		if element == "si" or element == "Si" or "Si" in unicode(element) or "si" in unicode(element):
			initialize_data[i] = 1
		i+=1

	return binar_data

def process_column(list_data, column_name, args):
	categories = set(list_data)
	categories = list(utils.to_lower(list(categories)))
	print("low categories", categories)

	binar = utils.check_binar(categories)

	if binar:
		print("binar category")
		binar_data = simple_binarization(list_data, categories, column_name)

	else:
		print("multivariate category")
		binar_data = binar_column(list_data, categories, column_name)

	return binar_data



















