##
## Imprima la suma de la _c2 por cada letra de la _c1 
## de la tabla tbl0
## 
(tbl0.groupby('_c1').sum())['_c2']
