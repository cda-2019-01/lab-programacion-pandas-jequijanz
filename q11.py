##
## Construya una tabla que contenga _c0 y una lista
## separada por ',' de los valores de la columna _c5a
## y _c5b (unidos por ':') de la tabla tbl2.tsv
## 
tbl2.head()
tbl2['_c5'] = tbl2['_c5a'] + ":" + tbl2['_c5b'].astype('str')
tblaux = tbl2.groupby('_c0')['_c5'].apply(list)
df = pd.DataFrame()
df['_c0'] = tblaux.keys()
df['lista'] = [elem for elem in tblaux]
df['lista'] = [",".join(str(v) for v in sorted(elem)) for elem in df['lista']]
df
