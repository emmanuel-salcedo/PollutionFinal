import pandas as pd
from pandas import ExcelFile, ExcelWriter
import sqlalchemy
print('ReadingCSV...')
pollution_tbl = pd.read_table('/Users/emmanuelsalcedo/PythonPro/PythonClass/ExternalScripts/uspollution.csv',
                              sep=',', encoding='cp1252')
print('mySqlExport Started')
engine = sqlalchemy.create_engine('mysql://root:PASSWORD@localhost/Pollution')
pollution_tbl.to_sql('pollution_tbl', engine, if_exists='replace')
print('Finished')