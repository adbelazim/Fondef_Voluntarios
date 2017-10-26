# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import pandas as pd
import json

import utils

def pre_process(df_data, args):
	#drop specific columns from the analysis
	df_data = utils.reduce_data(df_data)

	#get the columns in data frame
	columns = list(df_data.columns.values)

	list_categories = []
	for column in columns:
		print("procesando variable: ", column)
		#get levels and frecuency of each one per column
		levels = df_data[column].value_counts().index.tolist()
		frecuency = df_data[column].value_counts().values.tolist()

		#check if the colum contains binar data like si, or no: string#¢|@. Return boolean
		binar = utils.check_binar(utils.to_lower(df_data[column].value_counts().index.tolist()))

		#reduce levels by frecuency with the argument tol.
		#if a level in the column doesn't have meet the criterium frecuency/len_total_data is ignored
		levels, frecuency = utils.reduce_levels(levels, frecuency, df_data.shape[0], tol = args.tol)
		levels = list(set(levels))

		#process every colum like binar o with levels
		clean_column(df_data, unicode(column), levels, binar)
		print

	return df_data


def clean_column(df_data, column, levels, binar):
	"""Esta funcion se encarga de eliminar casos poco frecuentes y reemplazarlos como "otros"
	en la columna de datos original
	"""

	if binar:
		#print("la variable es binaria: ", column)
		i = 0
		for element in df_data[column]:
			#clean element in every instance
			element = unicode(utils.clean_string(element)).lower()
			if unicode("si") in element:
				df_data.set_value(i, column, u"si")
			else:
				df_data.set_value(i, column, u"no")
			i+=1

	else:
		#print("la variable no es binaria", column)
		if column == "Actividad_Fisica":
			process_act_fisica(df_data, column)

		elif column == "Nacionalidad":
			process_nacionalidad(df_data, column)

		elif column == "Dieta_Alimenticia":
			process_dieta(df_data, column)

		else:
			process_column_by_levels(df_data, column, levels)
			
#PROCESAMIENTO GENERICO DE LAS VARIABLES

def process_column_by_levels(df_data, column, levels):
	i = 0
	for element in df_data[column]:
		element = unicode(utils.clean_string(element)).lower()
		aux = False
		for level in levels:
			level_clean = unicode(utils.clean_string(level)).lower()
			if element in level_clean:
				df_data.set_value(i, column, unicode(utils.clean_points(level)))
				aux = True
		if not aux:
			df_data.set_value(i, column, unicode("otra_"+str(column)))
		i +=1
	return 0


#################################################################################################
####################PROCESAMIENTO PARTICULAR DE VARIABLES########################################

def process_act_fisica(df_data, column):
	i = 0
	for element in df_data[column]:
		#clean element in every instance
		element = unicode(utils.clean_string(element)).lower()
		if unicode("1vezporsemana") in element:
			df_data.set_value(i, column, u"1 vez por semana")

		elif unicode("2vecesporsemana") in element:
			df_data.set_value(i, column, u"2 veces por semana")

		elif unicode("3vecesporsemana") in element:
			df_data.set_value(i, column, u"3 veces por semana")

		else: 
			df_data.set_value(i, column, u"no")
		
		i+=1


def process_nacionalidad(df_data, column):
	i = 0
	for element in df_data[column]:
		element = unicode(utils.clean_string(element)).lower()
		if unicode("chi") in element or\
			unicode("temuco") in element or\
			unicode("calama") in element or\
			unicode("chlena") in element or\
			unicode("calama") in element or\
			unicode("chle") in element or\
			unicode("chulena") in element or\
			unicode("nacional") in element or\
			unicode("hileno") in element:
			df_data.set_value(i, column, u"chilena")

		elif unicode("colombiano") in element or\
			unicode("colom") in element:
			df_data.set_value(i, column, u"colombiano")

		elif unicode("peru") in element:
			df_data.set_value(i, column, u"peruano")

		elif unicode("argen") in element:
			df_data.set_value(i, column, u"argentina")

		elif unicode("bolivia") in element or\
			unicode("boli") in element:
			df_data.set_value(i, column, u"boliviana")

		elif unicode("alemana") in element:
			df_data.set_value(i, column, u"alemana")

		elif unicode("estado") in element:
			df_data.set_value(i, column, u"estadounidense")

		elif unicode("ecua") in element:
			df_data.set_value(i, column, u"ecuatoriana")

		elif unicode("vnezolano") in element or\
			unicode("vene") in element:
			df_data.set_value(i, column, u"venezolano")

		else:
			df_data.set_value(i, column, u"no especifica")
		i+=1

def process_dieta(df_data, column):
	i = 0
	for element in df_data[column]:
		element = unicode(utils.clean_string(element)).lower()
		if unicode("vegetariano") in element:
			df_data.set_value(i, column, u"vegetariano")

		elif unicode("vegano") in element:
			df_data.set_value(i, column, u"vegano")

		elif unicode("omnivoro") in element:
			df_data.set_value(i, column, u"omnivoro")

		elif unicode("normal") in element:
			df_data.set_value(i, column, u"omnivoro")

		elif unicode("comodetodo") in element:
			df_data.set_value(i, column, u"omnivoro")

		else:
			df_data.set_value(i, column, u"otro")
		i+=1


























