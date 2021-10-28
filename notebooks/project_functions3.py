import pandas as pd
import os

def loadU(csv):
    return pd.read_csv(csv)


def load_and_process(csv):
    df = pd.read_csv(csv)
    
    dfRemovedCols = ['Country', 'US_State',
       'UK_Country','Age1stCode', 'LearnCode', 'YearsCode',
       'YearsCodePro', 'OrgSize', 'Currency', 'CompTotal',
       'CompFreq', 'LanguageWantToWorkWith',
       'DatabaseWantToWorkWith','PlatformWantToWorkWith', 'WebframeWantToWorkWith',
       'MiscTechWantToWorkWith','ToolsTechWantToWorkWith','NEWCollabToolsWantToWorkWith', 
       'OpSys','NEWStuck', 'NEWSOSites', 'SOVisitFreq', 'SOAccount', 'SOPartFreq',
       'SOComm', 'NEWOtherComms', 'Age', 'Gender', 'Trans', 'Sexuality',
       'Ethnicity', 'Accessibility', 'MentalHealth', 'SurveyLength',
       'SurveyEase']
      
    
    dfProcessed = (df.drop(dfRemovedCols, axis = 1))
    
    return dfProcessed