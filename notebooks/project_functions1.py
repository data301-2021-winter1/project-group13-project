import zipfile
import pandas as pd
import os # to get to document and open it
from collections import Counter

def unprocessed(csvFile):
    ''' A wrapped pandas function '''
    return pd.read_csv(csvFile)

def load_and_process(fileString,year):
    ''' Takes a filename and year and returns a dataframe
        params
        ------
        fileString: String
        year: int

        returns
        -------
        cleaned dataframe
     '''
    lastThree = fileString[-3:]
    #should improve this line
    dataFileString = 'survey_results_public_'+str(year)+'.csv'
    if(lastThree == 'zip'):
        with zipfile.ZipFile(fileString) as myzip:
            data = myzip.open(dataFileString)
        df = pd.read_csv(data,dtype='unicode')
    else:
        df = pd.read_csv(fileString)
    #need to find common columns accross the dataframes for cleaning
    #dfCleaned = df.copy().drop(['SOAccount','SOPartFreq','SurveyLength','SurveyEase'],axis=1)
    return df


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
