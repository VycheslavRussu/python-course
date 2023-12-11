import pandas as pd

task_DF = pd.read_csv('titanic.csv')

def ageFillMean(M):
    task_DF['Age'].fillna(value=M, inplace=True)
    mean_value = task_DF['Age'].mean()
    return round(mean_value, 4)

print(ageFillMean(11.5))