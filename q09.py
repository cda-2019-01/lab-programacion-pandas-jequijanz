##
## Construya una tabla que contenga _c1 y una lista
## separada por ':' de los valores de la columna _c2
## para el archivo tbl0.tsv
## 
tblaux = tbl0.groupby('_c1')['_c2'].apply(list)

df = pd.DataFrame()
df['_c1'] = tblaux.keys()
df['_c2'] = [elem for elem in tblaux]

df['_c2'] = [":".join(str(v) for v in sorted(elem)) for elem in df['_c2']]

df

