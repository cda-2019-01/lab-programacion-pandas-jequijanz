##
## Agregue el año como una columna a la tabla tbl0.tsv 
## 
import datetime
tbl0['_c3']=pd.to_datetime(tbl0['_c3'],errors='NA')
tbl0['year']=tbl0['_c3'].dt.year
tbl0
