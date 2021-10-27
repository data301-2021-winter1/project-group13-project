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

    lastThree = fileString[-3:] #checking if should use read csv or open zipfile
                                #then read

    if(lastThree == 'zip'):
        with zipfile.ZipFile(fileString) as myzip:
            dataFileString = 'survey_results_public_'+str(year)+'.csv'
            data = myzip.open(dataFileString)
        df = pd.read_csv(data,dtype='unicode')
    else:
        df = pd.read_csv(fileString)

    #Made genericish column drop for all dataframes
    #genericish since the names are prodominantly from 2021 for time sake
    columnDrop = ['SOAccount','SOPartFreq','SurveyLength','SurveyEase',
                    'SOVisitFreq','NEWOtherComms','Trans','OpSys','NEWSOSites',
                    'NEWStuck','SOComm','NEWOtherComms','Accesibility','SOVisitTo',
                    'SOFindAnswer','SOTimeSaved','SOHowMuchTime','MilitaryUS','SurveyTooLong'
                    ,'SurveyEasy','Exercise','SurveyLong','QuestionsConfusing','QuestionsInteresting'
                    ,'PlatformHaveWorkedWith','PlatformWantToWorkWith','WebframeHaveWorkedWith',
                    'MiscTechWantToWorkWith','NEWCollabToolsHaveWorkedWith','ToolsTechWantToWorkWith',
                    'Sexuality','Ethnicity','WebframeWantToWorkWith','US_State','UK_Country','Age1stCode'
                    'Country','CompFreq','DatabaseWanttoWorkWith','MiscTechHaveWorkedWith','ToolsTechHaveWorkedWith',
                    'NEWCollabToolsWantToWorkWith','ToolsTechHaveWorkedWith','DatabaseHaveWorkedWith','MentalHealth']

    #errors='ignore' since all columns are not in each df
    dfCleaned = (df.copy()
                 .drop(columnDrop,axis=1,errors='ignore')
                 .rename(columns={'LanguageHaveWorkedWith':'ProgrammingLanguage'
                                    ,'LanguageWorkedWith':'ProgrammingLanguage'
                                    ,'HaveWorkedLanguage':'ProgrammingLanguage'} ,errors='ignore')
                 )
    return dfCleaned

def dfAdjustColNames(dict):
    ''' Takes a dictionary and returns a dataframe, where the column names,
        are a transpose of a previous column of the dictionary
        params
        ------
        df: dictionary

        returns
        -------
        dataframe
     '''
    dfAdjusted = pd.DataFrame.from_dict(dict,orient='index').reset_index()
    dfAdjusted = dfAdjusted.transpose()
    dfAdjusted.columns = dfAdjusted.iloc[0]
    dfAdjusted = dfAdjusted[1:]

    return dfAdjusted

def dfLangSalaryMean(df):
    ''' Takes a dataframe and returns a dataframe of means of the columns
        subtracting the overall mean of the dataframe
        params
        ------
        df: DataFrame

        returns
        -------
        DataFrame of mean of column minus mean of all columns
     '''
    assert df.size != 0, "Dataframe is empty"
    meanDiffLang2021Dict = {}
    for col in df:
        meanDiff = df[col].mean() - df.mean().mean()
        meanDiffLang2021Dict[col] = meanDiff

    meanDiffLang2021Df = dfAdjustColNames(meanDiffLang2021Dict)
    return meanDiffLang2021Df

def dfLangSalary(df,countObj):
    ''' Takes in dataframe and counter object produce a dataframe of programming language to salary
        and returns a counter object
        params
        ------
        df: dataframe
        col: counter object

        returns
        -------
        dataframe
     '''
     #Samle of what the dictionary looks like before being loaded with salaries
     # dictLangSalary = {"C++":[],'APL':[],'Assembly':[],'Bash/Shell':[],'C':[],'C#':[],
    #                 'COBOL':[],'Clojure'}
    dictLangSalary = {}
    for k,v in countObj.items():
        dictLangSalary[k] = []
    for index, row in df.iterrows():
        str_row = str(row['ProgrammingLanguage'])
        list_row = str_row.split(";") #splitting by delimiter to separate languages
        for progLang in list_row:
            if progLang not in ['Nan','NaN','NAN','nan'] and row['ConvertedCompYearly'] not in ['nan']:
                dictLangSalary[progLang].append(row['ConvertedCompYearly'])

    dfLangSalary = dfAdjustColNames(dictLangSalary)
    return dfLangSalary

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
            if progLang not in ['Nan','NaN','NAN','nan']:
                cnt[progLang] += 1
    return cnt

def countPrintLang(cnt,year):
    for lang in sorted(cnt):
        print(f"{cnt[lang]} people have worked with {lang} in {year} ")
