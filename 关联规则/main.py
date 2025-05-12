import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

df_high = pd.read_csv('data.csv')

# 选取 7 个类别变量
cat_cols = [
    'workclass', 'education', 'marital_status',
    'occupation', 'relationship', 'race', 'sex'
]
df_cat = df_high[cat_cols].astype(str)

# 转成“交易列表”格式
transactions = df_cat.values.tolist()

# One-Hot 编码
te = TransactionEncoder()
te_ary = te.fit(transactions).transform(transactions)
df_ohe = pd.DataFrame(te_ary, columns=te.columns_)

# 挖掘频繁项集（支持度阈值可根据样本量调节，这里示例设为 0.05）
frequent_itemsets = apriori(df_ohe, min_support=0.05, use_colnames=True)

# 生成关联规则，并按 lift 排序取前 10
rules = association_rules(
    frequent_itemsets,
    metric="lift",
    min_threshold=1.0
).sort_values('lift', ascending=False).head(10)

# rules.to_csv('result.csv', index=False)
rules.to_excel('result.xlsx', index=False)

# 显示规则
print(rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']])

