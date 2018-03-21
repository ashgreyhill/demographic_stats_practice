import pandas as pd

path = 'files/Demographic_Statistics_By_Zip_Code.csv'
pd.DataFrame
df = pd.read_csv(path)

# print(df)

df_col_names= df.iloc[:,0:5]
print(df_col_names)
print(type(df_col_names))

df_first_5_rows = df.iloc[0:5, :]



print(df.columns[0:5])


