<!-- README.md -->

# 数据挖掘实验

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) [![Issues](https://img.shields.io/github/issues/你的用户名/data-mining)](https://github.com/你的用户名/data-mining/issues) [![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)]()

> 本仓库收录了《数据挖掘》课程的六个实验，涵盖 PageRank、社区发现、关联挖掘、聚类分析等核心技术。
> 每个实验均附带实验背景、问题描述、算法思路及结果展示。

---

## 📑 目录

* [实验一：PageRank 计算](#实验一-pagerank-计算)
* [实验二：社区发现](#实验二-社区发现)
* [实验三：关联挖掘与降维](#实验三-关联挖掘与降维)
* [实验四：数据聚合分析](#实验四-数据聚合分析)
* [实验五：关联规则挖掘](#实验五-关联规则挖掘)
* [实验六：聚类分析](#实验六-聚类分析)

---

## 实验一：PageRank 计算

**背景描述**：对于给定的网络链路图，计算每个节点的 PageRank 值。随机跳跃因子 β 的计算方式：

```text
β = 1 − |N − 30| / 100
```

其中 N 为个人学号后两位（例如学号后两位为 43，则 β = 1 − |43 − 30|/100 = 0.92）。

**任务要求**：

1. 根据上述公式计算 β。
2. 对链路示意图中的各节点进行迭代计算，直至收敛。

**示意图**：

<p align="center">
  <img src="https://github.com/user-attachments/assets/f5dec573-2542-4377-be57-3b2e1fb006bb" alt="PageRank 网络示意图" width="400" />
</p>

---

## 实验二：社区发现

**问题描述**：假设一个 2n 节点的社区，随机划分为大小均为 n 的两组，并在两组间构建二分图。

**参数设置**：

* n = 20
* 平均度数 d = 5

**任务要求**：

> 在上述条件下，寻找使得 K<sub>s,t</sub> 实例一定存在的最大 (s, t) 对，且满足 t ≤ s。

---

## 实验三：关联挖掘与降维

**背景描述**：基于我国某年份的经济指标数据，对核心成分进行降维分析。

**核心任务**：

* 使用 PCA（主成分分析）提取主要成分
* 使用 SVD（奇异值分解）验证和对比降维效果

**数据示意图**：

<p align="center">
  <img src="https://github.com/user-attachments/assets/5de584bb-fd71-448f-9811-91aae7598f73" alt="经济指标示意图" width="500" />
</p>

---

## 实验四：数据聚合分析

**问题描述**：延续前一实验的经济指标数据，分别基于以下四种距离度量对样本进行聚类：

* **欧氏距离**
* **曼哈顿距离（绝对值距离）**
* **切比雪夫距离**
* **马氏距离**

**任务要求**：

> 对比不同距离度量下的聚类结果，并讨论各自的优缺点。

---

## 实验五：关联规则挖掘

**数据来源**：UCI Adult 数据集（[下载链接](https://archive.ics.uci.edu/ml/datasets/Adult)）

**任务流程**：

1. 抽取年收入 > 50K 的样本
2. 针对以下 7 个类别属性进行关联规则挖掘：

   * 工作环境
   * 教育程度
   * 婚姻状况
   * 职业
   * 关系类型
   * 种族
   * 性别
3. 使用 Apriori 或 FP-Growth 算法，提取前 10 条最强关联规则

---

## 实验六：聚类分析

**研究目标**：探索世界各国森林、草原资源的分布规律

**数据说明**：共有 21 个国家，每个国家包含 4 项指标（详见下表）

**任务要求**：

* 基于上述指标构建特征矩阵
* 选择合适的聚类算法（如 K-Means、层次聚类等），分析国家间的相似性

**数据示意图**：

<p align="center">
  <img src="https://github.com/user-attachments/assets/0318ae64-db4c-4af7-8837-c5bf85e01f98" alt="森林草原资源数据示例" width="500" />
</p>

---

## 🛠 环境与运行

```bash
# 克隆仓库
git clone https://github.com/你的用户名/data-mining.git
cd data-mining

# 安装依赖（示例）
pip install -r requirements.txt

# 运行对应实验脚本
python experiment1_pagerank.py
```

---

> 如有疑问或建议，欢迎提 [Pull Request](https://github.com/你的用户名/data-mining/pulls) 或 Issue。
