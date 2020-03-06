import pandas as pd
titulos = pd.read_csv('data/titles.csv' )

#print(titulos.head(10))
#print("\n"*2)
elenco = pd.read_csv('data/cast.csv', encoding='utf-8')

#print(elenco.head(10))
#print(len(titulos))
'''

print(titulos[titulos.year.between(1980,2000)])

print(len( titulos[ (titulos. >= 1980) & (titulos.year <= 2000)]))

print(titulos[titulos.year.str.contains("1980")].sort_values('year'))