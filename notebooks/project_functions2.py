import pandas as pd
import os

def load_and_process(csv_file):
    df = pd.read_csv(csv_file)
    df1=(
        df.dropna(subset=['EdLevel','Country','LearnCode','ConvertedCompYearly']) 
        .drop(['LanguageHaveWorkedWith', 'LanguageWantToWorkWith',
       'DatabaseHaveWorkedWith', 'DatabaseWantToWorkWith',
       'PlatformHaveWorkedWith', 'PlatformWantToWorkWith',
       'WebframeHaveWorkedWith', 'WebframeWantToWorkWith',
       'MiscTechHaveWorkedWith', 'MiscTechWantToWorkWith',
       'ToolsTechHaveWorkedWith', 'ToolsTechWantToWorkWith',
       'NEWCollabToolsHaveWorkedWith', 'NEWCollabToolsWantToWorkWith', 'OpSys',
       'NEWStuck', 'NEWSOSites', 'SOVisitFreq', 'SOAccount', 'SOPartFreq',
       'SOComm', 'NEWOtherComms','SOAccount','SOPartFreq','SurveyLength','SurveyEase'], axis=1)
         .sort_values("EdLevel")
         .reset_index(drop=True)
        )    
    return df1

def groupby_EdLevel(dfp):
    df1 = dfp.groupby('EdLevel', as_index=False).sum()
    return df1

def show_Percentage(dfp, plt):
    total = len(dfp)
    for p in plt.patches:
        percentage = f'{100 * p.get_height() / total:.1f}%\n'
        x = p.get_x() + p.get_width() / 2
        y = p.get_height()
        plt.annotate(percentage, (x, y), ha='center', va='center')