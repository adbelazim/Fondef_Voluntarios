import argparse
import re
import pandas as pd

def get_args():
	"""Args given by command line.

	Return:
	Args given by command line. Some parameters has default behavior.
	
	"""

	parser = argparse.ArgumentParser()
	parser.add_argument("-f","--filename", type = str, default = "postulantes_injuv.xls", \
    					help = "Filename of the data.")
	# parser.add_argument("-p","--pre_process", type = bool, default = False, \
 #    					help = "True to pre process the data")
	# parser.add_argument("-b","--complex_binar", type = bool, default = False, \
 #    					help = "True to make complex binarization off all columns in dataset")
	parser.add_argument("-t","--tol", type = float, default = 0.001, \
    					help = "Tolerancia para considerar en el pre-procesamiento. \
    					Representa la frecuencia minima de ocurrencia de un nivel en un variable.")

	args = parser.parse_args()

	return args


def to_lower(list_categories):

	lower_categories = []
	for element in list_categories:
		lower_categories.append((unicode(element)).lower())

	return set(lower_categories)

def clean_string(string):
	chars = ";:, "
	for char in chars:
		string = unicode(string).replace(char,"")

	return string

def clean_points(string):
	chars = ";:,."
	for char in chars:
		string = unicode(string).replace(char,"")

	return string


def check_binar(list_categories):

	binar = False

	aux_si = False
	aux_no = False

	for element in list_categories:
		element = element.replace(" ", "")
		if "si:" in unicode(element) or\
			unicode(element) == "si":
			aux_si = True
		if "no:" in unicode(element) or\
			unicode(element) == "no":
			aux_no = True


	if aux_si and aux_no:
		binar = True

	return binar


def reduce_data(data):
	reduce_data = data.drop(['Detalle_Prevision','Comentarios',\
				'Voluntarios_que_ha_participado','Puede_Participar',\
				'Asistir_por_medios_propios','Conocimientos_especificos',\
				'Fecha_de_Inscripcion','Problema_Altura'],axis=1)   

	return reduce_data


# def check_binarization(df_data, apply = False):
# 	columns = list(df_data.columns.values)

# 	if apply:
# 		for column in columns:
# 			print("variable", column)
# 			print("index",df_data[column].value_counts().index.tolist())
# 			print("values",df_data[column].value_counts().values.tolist())
# 			print
# 			print

def reduce_levels(levels, frecuency, len_data, tol = 0.001):
	"""

	Parameters:
	levels --
	frecuency -- 
	tol -- porcentaje minimo de ocurrencia de un nivel para considerarse en el procesamiento.

	"""

	new_levels = []
	new_frecuency = []
	for i in range(0, len(levels)):
		if float(float(frecuency[i])/float(len_data)) >= tol:
			new_levels.append(unicode(levels[i]).lower())
			new_frecuency.append(frecuency[i])

	return new_levels, new_frecuency



















