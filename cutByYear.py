#년도(행)을 분리하는 코드.
import pandas as pd
#2007 2008 2009 2010 2011 2012 2013 2014 2015 2016 2017 2018
for i in range(2):
    kospiCSV = pd.read_csv('C:/stock/data/kospi_origin.csv', thousands=',')
    for ins in range(kospiCSV.count()[0]):
        if len(kospiCSV.loc[ins]['Date'].split(str(int('2007') + 4 * i))) == 2:
            continue
        elif len(kospiCSV.loc[ins]['Date'].split(str(int('2008') + 4 * i))) == 2:
            continue
        elif len(kospiCSV.loc[ins]['Date'].split(str(int('2009') + 4 * i))) == 2:
            continue
        elif len(kospiCSV.loc[ins]['Date'].split(str(int('2010') + 4 * i))) == 2:
            continue
        elif len(kospiCSV.loc[ins]['Date'].split(str(int('2011') + 4 * i))) == 2:
            continue
        elif len(kospiCSV.loc[ins]['Date'].split(str(int('2012') + 4 * i))) == 2:
            continue
        elif len(kospiCSV.loc[ins]['Date'].split(str(int('2013') + 4 * i))) == 2:
            continue
        elif len(kospiCSV.loc[ins]['Date'].split(str(int('2014') + 4 * i))) == 2:
            continue
        else:
            kospiCSV = kospiCSV.drop([ins])

    kospiCSV.to_csv("C:/stock/data/8/kospi_original_" + str(int('2007') + 4 * i) +"_"+str(int('2014') + 4 * i) + ".csv")