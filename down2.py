# import pandas as pd

# df = pd.read_csv('LAADS_query.2018-11-13T13_07.csv')
# urls = df['url'].values
# downloaded = []
# with open('downloaded.txt', 'r') as file:
#     for i in file:
#         downloaded.append(i.strip())
# # print(downloaded)

# undownloead = []
# url_head = 'https://ladsweb.modaps.eosdis.nasa.gov/'
# for i in urls:
#     # print(str(i).split(r'/')[-1])
#     if str(i).split(r'/')[-1] not in downloaded:
#         undownloead.append(i)
# with open('undownloaded.txt', 'w') as file:
#     for i in undownloead:
#         file.write(url_head + i + '\n')

import os

with open('undownloaded.txt', 'r') as file:
    for i in file:
        os.system('wget %s' % i[:-2])