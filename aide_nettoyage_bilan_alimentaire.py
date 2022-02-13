# Import des librairies
import numpy as np
import pandas as pd

# Import des données des bilans alimentaires
veg = pd.read_csv("data/vegetal.csv")
ani = pd.read_csv("data/animal.csv")

# Concaténation des bilans animaux et végétaux

# Ajout de la variable origin
ani["origin"] = "animal"
veg["origin"] = "vegetal"

# On regroupe veg et ani en un unique dataframe, via une union
temp = ani.append(veg)

# Suppression de ani et veg
del ani, veg

# On renomme les colonnes de temp
temp.columns = ["xx","xx2","country_code","country",'xx3','element'
    ,'item_code','item','xx4',"year","unit","value",'xx5','xx6'
    ,'origin']

# Transformation de temp en table pivot
data = temp.pivot_table(
   index=["country_code","country","item_code","item","year","origin"],
   columns = ["element"], values=["value"], aggfunc=sum)

# On renomme les colonnes (attention l'ordre peut changer selon vos données !)
data.columns = ['Domestic supply quantity', 'Export Quantity', 'Fat supply quantity (g/capita/day)',
                'Feed','Food', 'Food supply (kcal/capita/day)', 'Food supply quantity (kg/capita/yr)',
                'Import Quantity', 'Waste', 'Other uses', 'Processing', 'Production',
                'Protein supply quantity (g/capita/day)', 'Seed', 'Stock Variation']


#data = data.reset_index()
data.head()
