import codecs
from numpy import *
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

def load_data(path):
    data_set = list()
    with codecs.open(path) as f:
        for line in f.readlines():
            data = line.strip().split("\t")
            flt_data = list(map(float, data))
            data_set.append(flt_data)
    return data_set

def dist_eucl(vecA, vecB):

    return sqrt(sum(power(vecA - vecB, 2)))

def rand_cent(data_mat, k):
    n = shape(data_mat)[1]
    centroids = mat(zeros((k, n)))
    for j in range(n):
        minJ = min(data_mat[:, j])
        rangeJ = float(max(data_mat[:, j]) - minJ)
        centroids[:, j] = mat(minJ + rangeJ * random.rand(k, 1))

    return centroids

def kMeans(data_mat, k, dist="dist_eucl", create_cent="rand_cent"):
    m = shape(data_mat)[0]
    # 初始化点的簇
    cluster_assment = mat(zeros((m, 2)))  # 类别，距离
    # 随机初始化聚类初始点
    centroid = eval(create_cent)(data_mat, k)
    cluster_changed = True
    # 遍历每个点
    while cluster_changed:
        cluster_changed = False
        for i in range(m):
            min_index = -1
            min_dist = inf
            for j in range(k):
                distance = eval(dist)(data_mat[i, :], centroid[j, :])
                if distance < min_dist:
                    min_dist = distance
                    min_index = j
            if cluster_assment[i, 0] != min_index:
                cluster_changed = True
                cluster_assment[i, :] = min_index, min_dist ** 2
        # 计算簇中所有点的均值并重新将均值作为质心
        for j in range(k):
            idx = nonzero(cluster_assment[:, 0].A == j)[0]

            if idx.size > 0:
                # 簇不空：正常用簇内点的均值更新
                per_data_set = data_mat[idx]
                centroid[j, :] = mean(per_data_set, axis=0)
            else:
                rand_i = random.randint(0, data_mat.shape[0])
                centroid[j, :] = data_mat[rand_i, :]

    return centroid, cluster_assment

def plot_cluster(data_mat, cluster_assment, centroid):
    plt.figure(figsize=(15, 6), dpi=80)
    plt.subplot(121)
    plt.plot(data_mat[:, 0], data_mat[:, 1], 'o')
    plt.title("source zip", fontsize=15)
    plt.subplot(122)
    k = shape(centroid)[0]
    colors = [plt.cm.get_cmap("Spectral")(each) for each in linspace(0, 1, k)]
    for i, col in zip(range(k), colors):
        per_data_set = data_mat[nonzero(cluster_assment[:, 0].A == i)[0]]
        plt.plot(per_data_set[:, 0], per_data_set[:, 1], 'o', markerfacecolor=tuple(col),
                 markeredgecolor='k', markersize=10)
    for i in range(k):
        plt.plot(centroid[:, 0], centroid[:, 1], '+', color='k', markersize=18)
    plt.title("K-Means Cluster, k = 3", fontsize=15)
    plt.savefig('image/kmeans.jpg', dpi=300)
    plt.show()