import pandas as pd
import copy

task_DF = pd.read_csv('titanic.csv')

def groupStats(M, N, P):

    unique_values = list(task_DF[M].unique())
    answer_dict = dict()

    for value in unique_values:
        answer_key = copy.deepcopy(value)

        if P == 'mean':
            answer_value = task_DF.loc[task_DF[M] == value, [N]][N].mean()
            answer_value = round(answer_value, 2)
        elif P == 'min':
            answer_value = task_DF.loc[task_DF[M] == value, [N]][N].min()
        elif P == 'max':
            answer_value = task_DF.loc[task_DF[M] == value, [N]][N].max()
        elif P == 'count':
            answer_value = task_DF.loc[task_DF[M] == value, [N]][N].count()

        answer_dict[answer_key] = answer_value

    return answer_dict


# Тестовые данные
M = 'Pclass' # группируем по этому стобцу
N = 'Age' # расчет статистики
P = 'mean' # статистический метод

# min, max, mean, count — список действий
# {1: 38.23, 2: 29.88, 3: 25.14} — вывод значений

print(groupStats(M, N, P))