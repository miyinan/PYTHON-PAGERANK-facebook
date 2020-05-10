
import matplotlib.pyplot as plt
import SQL

N = 22469

plt.figure(figsize=[15,8])
plt.title("pr曲线随样本数变化的演示")
n = 10
rankrate=SQL.getRankRate('all_',n)
plt.subplot(2,5,1)
plt.plot(rankrate)
plt.show()

n=30
rankrate=SQL.getRankRate('all_',n)
plt.subplot(2,5,2)
plt.plot(rankrate)
plt.show()

n=60
rankrate=SQL.getRankRate('all_',n)
plt.subplot(2,5,3)
plt.plot(rankrate)
plt.show()

n=100
rankrate=SQL.getRankRate('all_',n)
plt.subplot(2,5,4)
plt.plot(rankrate)
plt.show()

n=200
rankrate=SQL.getRankRate('all_',n)
plt.subplot(2,5,5)
plt.plot(rankrate)
plt.show()

n=400
rankrate=SQL.getRankRate('all_',n)
plt.subplot(2,5,6)
plt.plot(rankrate)
plt.show()

n=800
rankrate=SQL.getRankRate('all_',n)
plt.subplot(2,5,7)
plt.plot(rankrate)
plt.show()

n=1000
rankrate=SQL.getRankRate('all_',n)
plt.subplot(2,5,8)
plt.plot(rankrate)
plt.show()

n=2000
rankrate=SQL.getRankRate('all_',n)
plt.subplot(2,5,9)
plt.plot(rankrate)
plt.show()

n=4000
rankrate=SQL.getRankRate('all_',n)
plt.subplot(2,5,10)
plt.plot(rankrate)
plt.show()
