import zipfile
import pandas as pd
import os # to get to document and open it

def loadCsvZipDf(csvFile):
    with zipfile.ZipFile('../data/raw/survey_results_public_2019.csv.zip') as myzip:
        data2019 = myzip.open('survey_results_public_2019.csv')
    df = pd.read_csv(data2019,dtype='unicode')
    return df


def dfCleaner(df):
    dfCleaned = df.copy().drop(['US_State','SOAccount','SOPartFreq','NEWSOSites','SurveyLength','SurveyEase'],axis=1)
    return dfCleaned

def dfUserCount(progLang)
    count = 0
    for index, row in df.iterrows():
        str_row = str(row['LanguageHaveWorkedWith'])
        list_row = str_row.split(";")
        if (progLang in list_row):
            count += 1
        return count
