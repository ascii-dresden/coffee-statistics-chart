import sys
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

if sys.argv[1] is None:
	print('Missing data file')
	
raw_config = open('config.json')

if raw_config is None:
	print('Missing config.json')

#load data
config = json.load(raw_config)
table = pd.read_csv(sys.argv[1], sep=';')

#get date of statistics
date = list(table)[2][:10]

#delete useless columns
table = table.drop(table.columns[2], axis = 1) 
table = table.drop(table.columns[0], axis = 1) 

table.head()

#iterate over rows to get same name for entries which should be summarized
#remove unnecessary rows
for ind in table.index:
	drop = True
	for key in config:
		if table['PRODUKTNAME'][ind] == key or any(table['PRODUKTNAME'][ind] == altName for altName in config[key]['altNames']):
			table.loc[ind, 'PRODUKTNAME'] = config[key]['language']
			drop = False
			break;
	if drop:
		table = table.drop([ind])		

#sum rows with same name and sort from high to low
table = table.groupby('PRODUKTNAME', as_index=False).aggregate({'Gesamtzähler': 'sum'}).reindex(columns=table.columns)
table = table.sort_values(by='Gesamtzähler', ascending=False)

#get colors from config
colors = []
for ind in table.index:
	for key in config:
		if table['PRODUKTNAME'][ind] == config[key]['language']:
			colors.append(config[key]['color'])
			break

#sum beverage count
total = sum(table['Gesamtzähler'])

#draw plot
plt.bar(x=np.arange(1, len(table.index)+1),height=table['Gesamtzähler'], color=colors)
plt.xticks(np.arange(1, len(table.index)+1), table['PRODUKTNAME'], rotation=45, ha='right')
plt.title('01.08.2015 - ' + date + ', total: ' + str(total))
plt.tight_layout()
plt.show()
