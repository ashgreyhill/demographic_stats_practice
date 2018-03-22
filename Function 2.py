import pandas as pd

path= 'files/Demographic_Statistics_By_Zip_Code.csv'
pd.DataFrame
df=pd.read_csv(path)

df_5_rows= df.iloc[0:5, :]
print(df_5_rows)


