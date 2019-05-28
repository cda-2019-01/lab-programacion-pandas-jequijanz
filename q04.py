##
## Imprima los valores unicos e la columna _c4 de 
## de la tabla tbl1 en mayusculas
## 
unicos=tbl1['_c4'].unique()
[x.upper() for x in unicos]

