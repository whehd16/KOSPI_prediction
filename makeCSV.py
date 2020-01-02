import os
import pandas as pd
#Read file from dir
file_list = os.listdir("C:/stock/data/stockData/")
kospiCSV = pd.read_csv('C:/stock/data/stockData/코스피지수 내역.csv', thousands=',')
kospiCSV = kospiCSV.drop('변동 %', axis=1)
kospiCSV = kospiCSV.drop('거래량', axis=1)

for file in file_list:
    if file == '코스피지수 내역.csv':
        continue
    try:
        csv = pd.read_csv("C:/stock/data/stockData/" + file, thousands=',')
        csv = csv.drop('변동 %', axis=1)
        if len(csv.columns) == 6:
            csv = csv.drop('거래량', axis=1)

        for i in range(1, len(csv.columns)):
            target = csv.columns[i]
            if target == "현재가":
                target = "Now"
            elif target == "오픈":
                target = "Open"
            elif target == "고가":
                target = "High"
            elif target == "저가":
                target = "Low"
            csv.rename(columns={csv.columns[i]: file.split(' ')[0] + '_' + target}, inplace=True)
        kospiCSV = pd.merge(kospiCSV, csv, on='날짜', how='left')

    except:
        print(file)
        continue

for i in range(len(kospiCSV['날짜'])):
    kospiCSV['날짜'][i] = kospiCSV['날짜'][i].split(' ')[0][:-1] + '-' +\
                        kospiCSV['날짜'][i].split(' ')[1][:-1] + '-' +\
                        kospiCSV['날짜'][i].split(' ')[2][:-1]

kospiCSV.rename(columns={kospiCSV.columns[0]: 'Date'}, inplace=True)
kospiCSV.rename(columns={kospiCSV.columns[1]: 'KOSPI_Now'}, inplace=True)
kospiCSV.rename(columns={kospiCSV.columns[2]: 'KOSPI_Open'}, inplace=True)
kospiCSV.rename(columns={kospiCSV.columns[3]: 'KOSPI_High'}, inplace=True)
kospiCSV.rename(columns={kospiCSV.columns[4]: 'KOSPI_Low'}, inplace=True)

# print(kospiCSV)
index = len(kospiCSV)-1
while True:
    if kospiCSV['Date'][index] == "2007-01-09":
        break
    kospiCSV = kospiCSV.drop([index])
    index -= 1

#역순으로
kospiCSV = kospiCSV.reindex(index=kospiCSV.index[::-1])
kospiCSV.to_csv("C:/stock/data/mergedData/코스피병합본.csv")