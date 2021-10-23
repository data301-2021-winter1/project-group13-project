import zipfile
import pandas as pd
import os # to get to document and open it

def loadCsvZipDf(csvFile):
    with zipfile.ZipFile('../data/raw/survey_results_public_2019.csv.zip') as myzip:
        data2019 = myzip.open('survey_results_public_2019.csv')
    df = pd.read_csv(data2019,dtype='unicode')
    return df


def dfCleaner(df):
    dfCleaned = df.copy().drop(['SOAccount','SOPartFreq','NEWSOSites','SurveyLength','SurveyEase'],axis=1)
    return dfCleaned
