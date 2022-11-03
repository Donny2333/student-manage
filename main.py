# coding:utf-8
import pandas as pd

class_name = '408'

pd.set_option('display.unicode.east_asian.width', True)
df = pd.read_csv('./data/r'+ class_name +'.csv')

df = df[df['作业评分和状态'] == '待批改']

# print(df)

pattern = '([\u4e00-\u9fa5]{2,4})'

df['学生姓名'] = df['学生姓名'].str.extract(pattern)
df['学生姓名'] = df['学生姓名'].str.extract('([^\u7684]+)') # 的
df['学生姓名'] = df['学生姓名'].str.extract('([^\u7238]+)') # 爸
df['学生姓名'] = df['学生姓名'].str.extract('([^\u5988]+)') # 妈
df['学生姓名'] = df['学生姓名'].str.extract('([^\u53f7]+)') # 号
df['学生姓名'] = df['学生姓名'].str.extract('([^\u73ed]+)') # 班
df['学生姓名'] = df['学生姓名'].str.extract('([^\u662f]+)') # 是


df.drop_duplicates(subset=['学生姓名'], keep='first', inplace=True)

register = pd.read_csv('./data/' + class_name + '.csv')

register.insert(loc=1, column='是否提交', value=False)


def same_element(train_data, test_data):
    col_list = train_data.columns.tolist()
    for i in col_list:
        set1 = set(train_data[i])
        set2 = set(test_data[i])
        print(i, '相同的元素：', (set1 & set2), '\n', i, '相同元素的个数：', len(set1 & set2), '\n')
        print(i, '不同的元素：', (set1 ^ set2), '\n', i, '不相同的元素个数：', len(set1 ^ set2), '\n')
        print(i, '交了作业的名单中有花名册中没有的学生：', ((set1 | set2)-set2), '\n', i,
              '交了作业的名单中有花名册中没有的元素个数：', len(((set1 | set2)-set2)), '\n')
        print(i, '交了作业的名单中没有花名册中有的元素：', ((set1 | set2)-set1), '\n', i,
              '交了作业的名单中没有花名册中有的元素个数：', len(((set1 | set2)-set1)), '\n')


same_element(df.loc[:, '学生姓名'].to_frame(), register.loc[:, '学生姓名'].to_frame())

# for row in register.itertuples():
#     if (df[df['学生姓名'] == row[1]].shape[0]):
#         register.iloc[row[0], register.columns.get_loc("是否提交")] = True

# print(register[register['是否提交'] == True])

# print(register[register['是否提交'] == False])

# df.insert(loc=4, column='查无此人', value='')

# for row in df.itertuples():
#     if (register[register['学生姓名'] == row[1]].shape[0] == 0):
#         df.iloc[row[0], 4] = True

# print(df)
