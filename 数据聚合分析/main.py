import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

from scipy.cluster.hierarchy import linkage, fcluster
from scipy.spatial.distance import pdist
from sklearn.preprocessing import StandardScaler
from cal_distance import cal_distance

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

# 聚类结果
cluster_df = pd.DataFrame({'省份': df['省份']})
cluster_df = cal_distance(X_std, cluster_df)

# 输出各种距离下的聚类标签
print(cluster_df)

# PCA 降维到 2 维
pca2 = PCA(n_components=2)
X_pca2 = pca2.fit_transform(X_std)

# 可视化
for name in ['Euclidean', 'Manhattan', 'Chebyshev', 'Mahalanobis']:
    labels = cluster_df[name].values
    save_path = 'image/{name}.jpg'

    plt.figure()
    plt.scatter(
        X_pca2[:, 0], X_pca2[:, 1],
        c=labels, edgecolor='k', s=60
    )
    plt.title(f'通过计算 {name} 距离聚类 (k=4)')
    plt.xlabel('PC1')
    plt.ylabel('PC2')
    plt.xticks([])
    plt.yticks([])
    plt.savefig(save_path, dpi=300)
    plt.show()