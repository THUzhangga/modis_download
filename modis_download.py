import pandas as pd
import os

df = pd.read_csv('LAADS_query.2018-11-13T13_07.csv')
url_head = 'https://ladsweb.modaps.eosdis.nasa.gov/'
# print(df.head())
# wget https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/6/MOD13Q1/2000/049/MOD13Q1.A2000049.h26v04.006.2015136104814.hdf
for i in df['url'].values:
    url = url_head + i
    os.system('wget %s' % url)