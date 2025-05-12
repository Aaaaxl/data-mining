import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 读取数据
df = pd.read_excel('economic_data_provinces.xlsx')

features = [
    '国内生产(亿元)', '居民消费(亿元)', '固定资产(亿元)', '职工工资(元)',
    '货物周转(亿吨公里)', '消费物价(上年=100)', '商品零售价格(上年=100)', '工业产值(亿元)'
]

X = df[features].values

# 标准化
X_std = StandardScaler().fit_transform(X)

# PCA 分析
pca = PCA()
X_pca = pca.fit_transform(X_std)
print("解释方差比:", pca.explained_variance_ratio_)
print("PCA components:\n", pca.components_)

# SVD 分析
U, S, Vt = np.linalg.svd(X_std, full_matrices=False)
print("奇异值:", S)
print("SVD loadings (V^T):\n", Vt)

# Scree Plot: 方差贡献率
plt.figure()
plt.plot(
    range(1, len(pca.explained_variance_ratio_) + 1),
    pca.explained_variance_ratio_,
    marker='o'
)
plt.title('PCA 解释方差比')
plt.xlabel('Principal Component')
plt.ylabel('Variance Ratio')
plt.xticks(range(1, len(pca.explained_variance_ratio_) + 1))
plt.show()

# Scatter Plot: 前两主成分投影
plt.figure()
plt.scatter(X_pca[:, 0], X_pca[:, 1])
for i, prov in enumerate(df['省份']):
    plt.text(X_pca[i, 0], X_pca[i, 1], prov)
plt.title('PCA 前两主成分投影')
plt.xlabel('PC1')
plt.ylabel('PC2')
plt.show()