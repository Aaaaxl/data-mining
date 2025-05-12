import pandas as pd

# 读入原始数据
column_names = [
    'age', 'workclass', 'fnlwgt', 'education', 'education_num',
    'marital_status', 'occupation', 'relationship', 'race', 'sex',
    'capital_gain', 'capital_loss', 'hours_per_week', 'native_country', 'income'
]
df = pd.read_csv(
    'adult/adult.data',
    header=None,
    names=column_names,
    skipinitialspace=True
)

# 筛选年收入 >50K 的样本
df_select = df[df['income'] == '>50K']

# 保存过滤后的数据到 data.csv
df_select.to_csv('data.csv', index=False)
