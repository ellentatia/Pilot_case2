import pandas as pd

#df_total = pd.read_table('IPBES_VA_Uptake_Corpus_06May20.txt', header=0)

df = pd.read_csv('Pilot_case2_region_subregion.csv', header=0,low_memory=False)
#df=df_total.iloc[:100,:].copy()
#df.fillna('', inplace=True)

df_2 = pd.read_csv('2.csv', header=0,low_memory=False)
df_3 = pd.read_csv('3.csv', header=0,low_memory=False)
df_4 = pd.read_csv('4.csv', header=0,low_memory=False)
df_5 = pd.read_csv('5.csv', header=0,low_memory=False)
df_6 = pd.read_csv('6.csv', header=0,low_memory=False)
df_7 = pd.read_csv('7.csv', header=0,low_memory=False)
df_8 = pd.read_csv('8.csv', header=0,low_memory=False)
df_9 = pd.read_csv('9.csv', header=0,low_memory=False)
df_10 = pd.read_csv('10.csv', header=0,low_memory=False)
df_11 = pd.read_csv('11.csv', header=0,low_memory=False)
df_12 = pd.read_csv('12.csv', header=0,low_memory=False)
df_13 = pd.read_csv('13.csv', header=0,low_memory=False)
df_14 = pd.read_csv('14.csv', header=0,low_memory=False)
df_15 = pd.read_csv('15.csv', header=0,low_memory=False)
df_17 = pd.read_table('27NOT17.txt', header=0,low_memory=False)
df_18 = pd.read_table('18.txt', header=0,low_memory=False)
df_19 = pd.read_table('19.txt', header=0,low_memory=False)
df_20 = pd.read_table('20.txt', header=0,low_memory=False)
df_21 = pd.read_table('21.txt', header=0,low_memory=False)
df_22 = pd.read_table('22_AN.txt', header=0,low_memory=False)
df_23 = pd.read_table('23.txt', header=0,low_memory=False)
df_24 = pd.read_table('24.txt', header=0,low_memory=False)
df_25 = pd.read_table('25.txt', header=0,low_memory=False)
df_26 = pd.read_table('26.txt', header=0,low_memory=False)
#df_27 = pd.read_table('27NOT17.txt', header=0,low_memory=False)


#df[TS1] all entries are 1
value1=[]
for x in range(0, len(df)):
    value1.append(1)
df['TS1']=value1


def match(text):
  # clean 4 digts
  values=[]
  for x in range(0, len(text)):
    data=str(text[x])
    values.append(data.replace(data[:4], 'ISI'))
  # isin
  A = df.UT.isin(values)
  #return values
  TSN=[]
  for x in range(0, len(df)):
    TSN.append(int(A[x]))
  return TSN


# apply match function to files 2 to 15

df['TS2']= match(df_2['UT'])
df['TS3']= match(df_3['UT'])
df['TS4']= match(df_4['UT'])
df['TS5']= match(df_5['UT'])
df['TS6']= match(df_6['UT'])
df['TS7']= match(df_7['UT'])
df['TS8']= match(df_8['UT'])
df['TS9']= match(df_9['UT'])
df['TS10']= match(df_10['UT'])
df['TS11']= match(df_11['UT'])
df['TS12']= match(df_12['UT'])
df['TS13']= match(df_13['UT'])
df['TS14']= match(df_14['UT'])
df['TS15']= match(df_15['UT'])


#df[TS16] all entries are 1
value16=[]
for x in range(0, len(df)):
    value16.append(1)
df['TS16']=value16

def clean_4digts(text):
    values=[]
    for x in range(0, len(text)):
        data=str(text[x])
        values.append(data.replace(data[:4], 'ISI'))
    return values

#df[TS17]
value17=clean_4digts(df_17['UT'])
df['ts17'] = df.UT.isin(value17)
a=df['ts17']
b=1-a
df['TS17']=b


df['TS18']= match(df_18['UT'])
df['TS19']= match(df_19['UT'])
df['TS20']= match(df_20['UT'])
df['TS21']= match(df_21['UT'])
df['TS22']= match(df_22['UT'])
df['TS23']= match(df_23['UT'])
df['TS24']= match(df_24['UT'])
df['TS25']= match(df_25['UT'])
df['TS26']= match(df_26['UT'])

#value27 is 1
value27=[]
for x in range(0, len(df)):
    value27.append(1)
#print(value27[:5])
df['TS27']=value27
#print(df['TS27'][:5])

df2= df.drop(['ts17'], axis=1)
df2=df2.reset_index(drop=True)
#print(df2.columns)
#print(df2.head(2))

df2.to_excel('Pilot_case2_region_subregion_TS.xlsx', index=False)
df2.to_csv('Pilot_case2_region_subregion_TS.csv', index=False)
