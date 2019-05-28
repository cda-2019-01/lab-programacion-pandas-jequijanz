##
## Imprima el maximo de la _c2 por cada letra de la _c1 
## de la tabla tbl0
## 
(tbl0.groupby('_c1').max())['_c2']
