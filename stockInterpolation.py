import os

#csv 파일 시계열 데이터 선형 보간하는 데이터.

import pandas as pd
#fileRead
kospiCSV = pd.read_csv('C:/stock/data/mergedData/코스피병합본.csv', thousands=',')
print(kospiCSV.columns)
columns = kospiCSV.columns

for column in columns:
    kospiCSV[column] = kospiCSV[column].interpolate()

# for i in range(0,520):
#     kospiCSV = kospiCSV.drop([i])

#rename columns
# kospiCSV.rename(columns = {'날짜':'Date', '현재가':'KOSPI_Now', '오픈':'KOSPI_Open', '고가':'KOSPI_High','저가':'KOSPI_Low' }, inplace = True)

print(kospiCSV)
kospiCSV.to_csv("C:/stock/data/kospi_origin.csv")