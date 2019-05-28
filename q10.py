##
## Construya una tabla que contenga _c0 y una lista
## separada por ',' de los valores de la columna _c4
## de la tabla tbl1.tsv
## 
tbl1.head()
tblaux = tbl1.groupby('_c0')['_c4'].apply(list)
df = pd.DataFrame()
df['_c0'] = tblaux.keys()
df['lista'] = [elem for elem in tblaux]
df['lista'] = [",".join(str(v) for v in sorted(elem)) for elem in df['lista']]
df
