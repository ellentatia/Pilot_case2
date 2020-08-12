#used the outcome from the code ellen_test50.py 
# objective to extract region based on the file final_land_vs1.csv 

import pandas as pd
#df = pd.read_csv('Pilot_case2_05.csv', header=0)
df = pd.read_csv('~/pilot2_re/Pilot_case2_06.csv', header=0) #25.06.2020
# index_col=False)


import csv

dic = {}
#dic2 = {}
with open("final_land_vs1.csv") as f:
    file = csv.DictReader(f, delimiter=',')
    for line in file:
        dic[line['ISO_Alpha_3']] = line['Region']
        #dic2[line['ISO_Alpha_3']] = line['Sub-Region']
#print(dic['USA'])
#print(dic2['USA'])
#print(dic.keys())


def getRegion(text):
    region = []
    for country in dic.keys():
      if str(country) in str(text):
        region.append(dic[country])
            
    return region
######

#def getSubregion(data):
 #  subregion = []
  # for code in dic2.keys():
   # if str(code) in str(data):
    #  subregion.append(dic2[code])
      
    #return subregion

# function to filter repeated values

def my_function(i):
    return list(dict.fromkeys(i))


# from list to strings
def mystrings(text):
    return ', '.join(text)


# Region

df['Region country1'] = df['CountryName_TI_AB_DE_ID'].map(getRegion)
df['Region country1'] = df['Region country1'].map(my_function).map(mystrings)
df['Region country2'] = df['CountryName_C1_FU_FX'].map(getRegion)
df['Region country2'] = df['Region country2'].map(my_function).map(mystrings)

#df['Region'] = df['Region1'] + df['Region2']
#df['Region'] = df['Region'].map(my_function).map(mystrings)
#print(df['Region'][0])

# Sub-Region

#df['Sub-Region1'] = df['country name1'].map(getSubregion)
#print(getSubregion(df['country name1'][0]))
#df['Sub-Region2'] = df['country name2'].map(getSubregion)
#print(getSubregion(df['country name2'][0]))
#df['Sub-Region'] = df['Sub-Region1'] + df['Sub-Region2']
#df['Sub-Region'] = df['Sub-Region'].map(my_function).map(mystrings)
#print(df['Sub-Region'][0])

#df['countryname2'] = df['affiliation_country'] + df['funding_country'] + df['funding-acknowledge_country']
#df['country name2'] = df['countryname2'].map(my_function).map(mystrings)
# print(df['country name2'][0])

#df2 = df.drop(['Region1', 'Region2'],axis=1)

df = df.reset_index(drop=True)
print(df.columns)

df.to_csv('Pilot_case2_region.csv',index=False)
df.to_excel('Pilot_case2_region.xlsx', index=False)
