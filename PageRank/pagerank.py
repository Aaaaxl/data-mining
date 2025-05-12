import numpy as np

def compute_pagerank(N):
    # 计算 β
    beta = 1 - abs(N - 30) / 100.0

    # 构建邻接矩阵 A
    A = np.array([
        [1, 1, 1],
        [1, 0, 1],
        [0, 1, 1],
    ], dtype=float)

    # 计算出度
    out_deg = A.sum(axis=1)

    # 构造转移矩阵 M
    M = (A / out_deg[:, None]).T

    # 设置线性方程 (I - βM) P = (1 - β) / n * 1
    n = A.shape[0]
    I = np.eye(n)
    ones = np.ones(n)
    b = (1 - beta) / n * ones

    # 求解 PageRank 向量 P
    P = np.linalg.solve(I - beta * M, b)

    # 打印结果
    print(f"β = {beta:.4f}")
    print("PageRank 值:")
    for node, score in zip(['a', 'b', 'c'], P):
        print(f"  {node}: {score:.4f}")

    return beta, P