import pandas as pd
#df = pd.read_csv('Pilot_case2_08.csv', header=0)
df = pd.read_csv('Pilot_case2_region.csv', header=0)
# index_col=False)


import csv

dic = {}

with open("final_land_vs1.csv") as f:
    file = csv.DictReader(f, delimiter=',')
    for line in file:
        dic[line['ISO_Alpha_3']] = line['Sub-Region']

def getSubregion(text):
    subregion = []
    for country in dic.keys():
      if str(country) in str(text):
        subregion.append(dic[country])
            
    return subregion
######

def my_function(i):
    return list(dict.fromkeys(i))


# from list to strings
def mystrings(text):
    return ', '.join(text)

# Sub-Region

df['Sub-Region country1'] = df['CountryName_TI_AB_DE_ID'].map(getSubregion)
df['Sub-Region country1'] = df['Sub-Region country1'].map(my_function).map(mystrings)
#print(getSubregion(df['country name1'][0]))
df['Sub-Region country2'] = df['CountryName_C1_FU_FX'].map(getSubregion)
df['Sub-Region country2'] = df['Sub-Region country2'].map(my_function).map(mystrings)
#print(getSubregion(df['country name2'][0]))
#df['Sub-Region'] = df['Sub-Region1'] + df['Sub-Region2']
#df['Sub-Region'] = df['Sub-Region'].map(my_function).map(mystrings)
#print(df['Sub-Region'][0])

#df2 = df.drop(['Sub-Region1', 'Sub-Region2'],axis=1)

df = df.reset_index(drop=True)
print(df.columns)

df.to_csv('Pilot_case2_region_subregion.csv',index=False)
df.to_excel('Pilot_case2_region_subregion.xlsx', index=False)
