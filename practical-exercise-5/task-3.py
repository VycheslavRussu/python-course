import pandas as pd

task_DF = pd.read_csv('titanic.csv')

def multipleConditions(M, N, P, K):
    persons_count = ((task_DF['Survived'] == True) &(task_DF['Age'] > M) &(task_DF['Pclass'] == N) &(task_DF['Parch'] == P) &(task_DF['Embarked'] == K)).sum()
    if persons_count > 0:
        proportion = round((persons_count / len(task_DF)), 4)
    else:
        proportion = 0
    return proportion

print(multipleConditions(1, 3, 0, 'Q'))