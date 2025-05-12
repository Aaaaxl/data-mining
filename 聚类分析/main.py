import pandas as pd
from sklearn.preprocessing import StandardScaler
from numpy import *
import random
import numpy as np

# 固定 random
SEED = 123
random.seed(SEED)
np.random.seed(SEED)

# 读取数据
df = pd.read_excel('forest_grassland.xlsx')
features = [
    '森林面积(万公顷)', '森林覆盖率(%)', '林木蓄积(亿立方米)', '草原面积(万公顷)'
]
X = df[features].values

# 标准化
X_std = StandardScaler().fit_transform(X)

# 转成 numpy.matrix
data_mat = mat(X_std)

# kmeans
from model.kmeans import kMeans, plot_cluster
centroid, cluster_assment = kMeans(data_mat, 3)
sse = sum(cluster_assment[:, 1])
print("kmeans: sse is ", sse)
plot_cluster(data_mat, cluster_assment, centroid)

# kmeans++
from model.kmeansplus import kpp_Means, plot_cluster
centroid, cluster_assment = kpp_Means(data_mat, 3)
sse = sum(cluster_assment[:, 1])
print("kmeans++: sse is ", sse)
plot_cluster(data_mat, cluster_assment, centroid)

# bi-kmeans
from model.bikmeans import bi_kMeans, plot_cluster
centroid, cluster_assment = bi_kMeans(data_mat, 3)
sse = sum(cluster_assment[:, 1])
print("bikmeans: sse is ", sse)
plot_cluster(data_mat, cluster_assment, centroid)