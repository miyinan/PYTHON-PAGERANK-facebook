#作业说明
Pagerank是谷歌搜索引擎给网页排名的算法，主要原理是马尔可夫链。pagerank又很多应用，只要有一个节点信息表node和节点关系文档txt，就可以根据edges来算出节点的pr值，这个pr值的含义有很多中解读办法我将在后续说明。
我先从Konect找到了符合pr要求又可以计算的过来的数据，在文件夹facebook_large中。
先在mysql中建立表格，再用python读取数据并计算，用python将数据存到mysql中，利用navicat绘制图表。
文件说明：
List.py:定义了很多获取信息列表的函数。从txt文档读取信息，规整格式，返回列表。
SQL：定义了连接数据库，建立表格，插入数据，修改数据的函数。
Main：写了pagerank的计算过程，并使用SQL和List中的函数完成存入数据库的操作。计算结果存储在‘分析结果’-‘FaceBookRank.sql’文件中。
Plot：根据得到的pr值绘制pr值曲线。由于计算能力，最多绘制4000个节点。其中展现了不同取样的是个图，反映了一定规律

注：因为计算过程和插入过程复杂，所以并没有让main函数中一键运行即可完成所有工作，而是根据需求注释掉了一些操作。运行时需要先读懂代码，恢复部分被注释的内容。


使用的mysql语句：
create table FaceBookRank.tpo100 select * from FaceBookRank.all_ where rank_<=100;
alter table FaceBookRank.tvshow add No2 int not null primary key Auto_increment;