import pandas as pd

test_DF = pd.read_csv('titanic.csv')

def ageSearch(m, n):
    count_values = ((test_DF['Age'] > m) & (test_DF['Age'] < n)).sum()
    return count_values

print(ageSearch(0, 10))