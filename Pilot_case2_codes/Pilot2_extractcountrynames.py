## Extracting Country names from literature 

import re 
import pandas as pd
df = pd.read_table('IPBES_VA_Uptake_Corpus_06May20.txt', header=0)
# index_col=False)
#df=df_total.iloc[:50,:].copy()

## open table and transform to dictionary for transforming country name to iso aplha3 code
import csv

dic = {}

with open("wikipedia-iso-country-codes_05.csv") as f:
    file = csv.DictReader(f, delimiter=',')
    for line in file:
        dic[line['English short name lower case']] = line['Alpha-3 code']

# list of countries from iso 
countries_list=[]
for country in dic.keys():
  countries_list.append(country)

# function to extract countries and transform to iso alpha3 code        
def extract(text):
    data = str(text).replace(".", " ").replace("-", " ").replace(",", " ").replace(";", " ").lower() 
    countries = re.compile(r'\b(?:%s)\b' % '|'.join([re.escape(x) for x in countries_list]),re.IGNORECASE) #regular expression
    #print(countries)
    result=countries.findall(data)
    #return result
    code = []
    for country in dic.keys():
      if  country.lower() in result:
        code.append(dic[country])
    return code      

# function to filter repeated values
def my_function(i):
    return list(dict.fromkeys(i))
# from list to strings

def mystrings(text):
    return ', '.join(text)
    

## columns to feed country1
df['title_country'] = df.TI.map(extract)
df['abstract_country'] = df.AB.map(extract)
#print(df['title_country'])
df['keywords_country'] = df.DE.map(extract)
df['keywords-plus_country'] = df.ID.map(extract)

df['countryname1'] = df['title_country'] + df['abstract_country'] + df['keywords_country'] + df['keywords-plus_country']
df['CountryName_TI_AB_DE_ID']=df['countryname1'].map(my_function).map(mystrings) 

## columns to feed country2
df['affiliation_country'] = df.C1.map(extract)
df['funding_country'] = df.FU.map(extract)
df['funding-acknowledge_country'] = df.FX.map(extract)
df['countryname2'] = df['affiliation_country'] + df['funding_country'] + df['funding-acknowledge_country']
df['CountryName_C1_FU_FX'] = df['countryname2'].map(my_function).map(mystrings)
#print(df['CountryName_C1_FU_FX'][0])

df2 = df.drop(['countryname1', 'countryname2', 'title_country', 'abstract_country', 'keywords_country', 'keywords-plus_country',
     'affiliation_country', 'funding_country', 'funding-acknowledge_country'], axis=1)

df2 = df2.reset_index(drop=True)
# print(df2.columns)

df2.to_csv('Pilot_case2_06.csv',index=False)
df2.to_excel('Pilot_case2_06.xlsx', index=False)
