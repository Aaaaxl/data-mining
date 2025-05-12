import numpy as np
from pagerank import compute_pagerank

stu_id = input("请输入学号的后两位：")
stu_id = int(stu_id)

compute_pagerank(stu_id)
