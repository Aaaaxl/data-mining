from scipy.cluster.hierarchy import linkage, fcluster
from scipy.spatial.distance import pdist
import numpy as np

def cal_distance(X_std, cluster_df, distance='all'):
    if distance == 'all':
        # 1. 欧氏距离
        Z_euclid = linkage(X_std, method='complete', metric='euclidean')
        cluster_df['Euclidean'] = fcluster(Z_euclid, t=4, criterion='maxclust')

        # 2. 曼哈顿距离（绝对值距离）
        Z_manhattan = linkage(X_std, method='complete', metric='cityblock')
        cluster_df['Manhattan'] = fcluster(Z_manhattan, t=4, criterion='maxclust')

        # 3. 切比雪夫距离
        Z_chebyshev = linkage(X_std, method='complete', metric='chebyshev')
        cluster_df['Chebyshev'] = fcluster(Z_chebyshev, t=4, criterion='maxclust')

        # 4. 马氏距离
        VI = np.linalg.inv(np.cov(X_std.T))
        D_mahal = pdist(X_std, metric='mahalanobis', VI=VI)
        Z_mahalanobis = linkage(D_mahal, method='complete')
        cluster_df['Mahalanobis'] = fcluster(Z_mahalanobis, t=4, criterion='maxclust')

    elif distance == '欧式':
        # 欧氏距离
        Z_euclid = linkage(X_std, method='complete', metric='euclidean')
        cluster_df['Euclidean'] = fcluster(Z_euclid, t=4, criterion='maxclust')

    elif distance == '曼哈顿':
        # 曼哈顿距离（绝对值距离）
        Z_manhattan = linkage(X_std, method='complete', metric='cityblock')
        cluster_df['Manhattan'] = fcluster(Z_manhattan, t=4, criterion='maxclust')

    elif distance == '切比雪夫':
        # 切比雪夫距离
        Z_chebyshev = linkage(X_std, method='complete', metric='chebyshev')
        cluster_df['Chebyshev'] = fcluster(Z_chebyshev, t=4, criterion='maxclust')

    elif distance == '马氏':
        # 马氏距离
        VI = np.linalg.inv(np.cov(X_std.T))
        D_mahal = pdist(X_std, metric='mahalanobis', VI=VI)
        Z_mahalanobis = linkage(D_mahal, method='complete')

    else:
        print("distance 只能是'all','欧式','曼哈顿','切比雪夫','马氏'")
        return 0

    return cluster_df
