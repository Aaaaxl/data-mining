import numpy as np
from itertools import combinations

def guaranteed_Kst(n, d):
    s = int(d)
    t = 1
    return s, t

def find_Ks_t_in_graph(adj, max_search_n=8):

    n = adj.shape[0]
    if n > max_search_n:
        raise ValueError(f"n={n} 太大，枚举搜索 infeasible，建议只用于 n<={max_search_n}")

    max_s_t = (0, 0)
    for s in range(1, n + 1):
        for t in range(1, n + 1):
            if s < max_s_t[0] or t < max_s_t[1]:
                continue
            for left_subset in combinations(range(n), s):
                for right_subset in combinations(range(n), t):
                    sub = adj[np.ix_(left_subset, right_subset)]
                    if np.all(sub == 1):
                        max_s_t = (s, t)
                        break
                else:
                    continue
                break
    return max_s_t

if __name__ == "__main__":
    # 1) 计算保证存在的 (s,t)
    n, d = 20, 5
    s_g, t_g = guaranteed_Kst(n, d)
    print(f"对 n={n}, d={d} 保证存在的最大 K_s,t 是 s={s_g}, t={t_g}")

    # 2) 小规模示例：枚举搜索 n <= 6
    small_n, small_d = 6, 3
    print("\n在小规模 (n=6, d≈3) 图中实际搜索最大 K_s,t：")
    np.random.seed(0)
    adj_small = (np.random.rand(small_n, small_n) < (small_d / small_n)).astype(int)
    s_a, t_a = find_Ks_t_in_graph(adj_small, max_search_n=6)
    print(f"找到的最大 K_s,t 是 s={s_a}, t={t_a}")
