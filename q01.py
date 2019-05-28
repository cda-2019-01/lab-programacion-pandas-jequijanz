##
## Imprima la cantidad de registros por cada letra 
## de la columna _c1 de la tabla tbl0
## 
import pandas as pd
tbl0=pd.read_csv("tbl0.tsv",sep="\t")
tbl1=pd.read_csv("tbl1.tsv",sep="\t")
tbl2=pd.read_csv("tbl2.tsv",sep="\t")
print (tbl0)
print (tbl1)
print (tbl2)
tbl0['_c1'].value_counts()
