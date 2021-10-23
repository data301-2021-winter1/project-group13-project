import zipfile
import pandas as pd
import os # to get to document and open it
from collections import Counter

def unprocessed(csvFile):
    return pd.read_csv(csvFile)

def load_and_process(csvFile):
    lastThree = csvFile[-3:]
    if(lastThree == 'zip'):
        with zipfile.ZipFile('../data/raw/survey_results_public_2019.csv.zip') as myzip:
            data2019 = myzip.open('survey_results_public_2019.csv')
        df = pd.read_csv(data2019,dtype='unicode')
    else:
        df = pd.read_csv(csvFile)

    dfCleaned = df.copy().drop(['SOAccount','SOPartFreq','SurveyLength','SurveyEase'],axis=1)
    return dfCleaned


def dfLangCount(df, col):
    ''' Takes in dataframe and column to count in the dataframe and returns a counter object
        params
        ------
        df: dataframe
        col: string

        returns
        -------
        counter collections object
     '''
    cnt = Counter()
    for index, row in df.iterrows():
        str_row = str(row[col])
        list_row = str_row.split(";")
        for progLang in list_row:
            cnt[progLang] += 1
    return cnt

def countPrintLang(cnt,year):
    for lang in sorted(cnt):
        print(f"{cnt[lang]} people have worked with {lang} in {year} ")


load_and_process('hello.zip')
