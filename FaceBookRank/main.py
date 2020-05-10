import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import norm
import SQL

alpha=0.85   #阻尼系数，用户随机点击链接的概率，工程结论是0.85
eps = 1e-17   #判断收敛条件时的误差
N=22469

#建立临接矩阵
adjaMatrix = np.zeros([N, N], dtype=float)  # 6-7位的有效数字
adjaMatrix2 = np.zeros([N, N], dtype=float)
f = open(r'./facebook_large/facebook_edges.txt', 'r')
for edge in f.readlines():
    edge_ = edge.strip('\\n')
    node0, node1 = edge_.split(',')
    adjaMatrix[int(node0)-1][int(node1)-1] = 1 # 给的信息表中有0节点
    adjaMatrix[int(node1)-1][int(node0)-1] = 1
f.close()
#print(adjaMatrix)
#用计算范数的方法计算度，写入数据库
Norm=norm(adjaMatrix,axis=1,ord=1)  #对行向量进行一维范数的计算,axis=1指的是行向量，ord是维度
SQL.insertOneData('all_','in_degree',Norm)      #插入的动作太慢了，所以还是先注释掉，用的时候再插
print(Norm)
#计算转移概率矩阵
transMatrix=adjaMatrix
for i in range(0,N):
    if(Norm[i]==0):
        continue
    transMatrix[i,:]=adjaMatrix[i,:]/Norm[i]
    #print("devide")
#print(transMatrix)
#计算A矩阵,在pagerank中通过不断右乘A矩阵来达到收敛平衡
ee=np.ones([N,N])
A=alpha*transMatrix+(1-alpha)*ee/N
p=np.ones([1,N])*((1+0.0)/N)
pA=np.dot(p,A)
n=0
e=1000
while(e>eps):
    p,pA=pA,np.dot(pA,A)
    n=n+1
    e1=abs(norm(p-pA))     #默认的参数norm返回的是一个标量
    if e1>e:
        print(n,e,'no')
    if e1<e:
        print(n, e, 'yes')
    e=e1

p=p*1e10
p_=p[0]
p__=p_.tolist()
#print(p)
SQL.insertOneData('all_','rank_rate',p__)

p1=np.array([p[0],np.arange(0,N,1)])
p2=p1[:,p1[0].argsort()]
index=p2[1].tolist()
rank=p2[0].tolist()
SQL.insertRankData('all_','rank_',index)



