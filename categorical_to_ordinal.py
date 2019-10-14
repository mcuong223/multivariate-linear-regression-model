import pandas
from labels import school

categories = [
    'school',
    'sex',
    'address',
    'famsize',
    'Pstatus',
    'Mjob',
    'Fjob',
    'reason',
    'guardian',
    'schoolsup',
    'famsup',
    'paid',
    'activities',
    'nursery',
    'higher',
    'internet',
    'romantic',
]

def to_ordinal(df, key):
    df[key] = df[key].astype('category')
    df[key] = df[key].cat.codes


df = pandas.read_csv('./data/student-mat.csv', ';')
df.fillna(-1, inplace=True)

for c in categories:
    to_ordinal(df, c)

df_path = './casted_data/casted.csv'

df.to_csv(df_path, index = False)

# print(df)


# # print(type(df['age'][0]))
# print(df)

# data = df.copy(deep = True)
# data = data.astype('category')
# # data['school'] = data['school'].cat.reorder_categories(['GP', 'MS'])
# data = data.cat.codes
# # print()
# # for i, j in zip(data, df):
# #     print(f'{i}   -    {j}')

