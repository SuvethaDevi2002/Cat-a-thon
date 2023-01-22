from idcard import Auth_data,d,t

import csv
header = ['Id number', 'Date', 'Time']
data = [Auth_data, d,t]
       # writer.writerow(header)
with open('entries.csv', 'a', newline='',encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(data)
    f.close()
import pandas as pd
file = pd.read_csv("entries.csv")
file.to_csv("ids.csv",header=header,index=False)