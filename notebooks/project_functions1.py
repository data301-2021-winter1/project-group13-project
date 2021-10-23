import zipfile
import pandas as pd
import os # to get to document and open it
from collections import Counter

def loadCsvZipDf(csvFile):
    with zipfile.ZipFile('../data/raw/survey_results_public_2019.csv.zip') as myzip:
        data2019 = myzip.open('survey_results_public_2019.csv')
    df = pd.read_csv(data2019,dtype='unicode')
    return df


def dfCleaner(df):
    dfCleaned = df.copy().drop(['SOAccount','SOPartFreq','SurveyLength','SurveyEase'],axis=1)
    return dfCleaned

def dfUserCount(df, progLang):
    count = 0
    iterDf = df
    for index, row in iterDf.iterrows():
        str_row = str(row['LanguageHaveWorkedWith'])
        list_row = str_row.split(";")
        if (progLang in list_row):
            count += 1
    return count

def dfLangCount(df):
    cnt = Counter()
    for index, row in df.iterrows():
        str_row = str(row['LanguageHaveWorkedWith'])
        list_row = str_row.split(";")
        for progLang in list_row:
            cnt[progLang] += 1
    return cnt

def countPrintLang(cnt,year):
    for lang in sorted(cnt):
        print(f"{cnt[lang]} people have worked with {lang} in {year} ")
