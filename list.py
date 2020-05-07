import re


def all_list():
    informationfile = open("./facebook_large/musae_facebook_target.txt", "r")
    informationList = []
    for information in informationfile.readlines():
        information = re.split(',', information)
        informationList.append(information)       #添加到我们建的列表
        informationList[-1][0]=int(informationList[-1][0])
        if len(informationList[-1]) > 4:                       #有的名字中间会带逗号，应当把被分割掉的名字合并
            fullname=informationList[-1][2]+informationList[-1][3]
            informationList[-1][2]=fullname
            informationList[-1][3]=informationList[-1][4]
            informationList[-1].pop()
        if re.match('government',informationList[-1][3]):   #给数据分类
            informationList[-1][3] = 1
        elif re.match('politician', informationList[-1][3]):
            informationList[-1][3] = 2
        elif re.match('company', informationList[-1][3]):
            informationList[-1][3] = 3
        elif re.match('tvshow', informationList[-1][3]):
            informationList[-1][3] = 4
        if not isinstance(informationList[-1][3],int):  #有一些无法被识别的文字，如果不删除就是乱码，不方便后面操作
            del(informationList[-1])
        if informationList[-1][3]>4:
            del (informationList[-1])


    return informationList


def government():
    list=all_list()
    governmentList=[]
    for i in range(0,len(list)):
        if list[i][-1]==1:
            governmentList.append(list[i])
    return governmentList


def company():
    list=all_list()
    companyList=[]
    for i in range(0,len(list)):
        if list[i][-1]==3:
            companyList.append(list[i])
    return companyList


def politician():
    list=all_list()
    politicianList=[]
    for i in range(0,len(list)):
        if list[i][-1]==2:
            politicianList.append(list[i])
    return politicianList


def tvshow():
    list=all_list()
    tvshowList=[]
    for i in range(0,len(list)):
        if list[i][-1]==4:
            tvshowList.append(list[i])
    return tvshowList


def alltype(type):
    list=all_list()
    typeList=[]
    if type=='all_':
        return list
    typenum = {"government": 1,"politician": 2,"company": 3,"tvshow": 4 }

    for i in range(0,len(list)):
        if list[i][-1]==typenum[type]:
            typeList.append(list[i])
    return typeList

for li in tvshow():
    print(li)








