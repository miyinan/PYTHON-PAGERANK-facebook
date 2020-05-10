import re


def all_list():
    informationfile = open("./facebook_large/musae_facebook_target.txt", "r")
    informationList = []
    for information in informationfile.readlines():
        information = re.split(',', information)
        informationList.append(information)       #添加到我们建的列表
        informationList[-1][0]=int(informationList[-1][0])
        while(len(informationList[-1])>4):
            fullname = informationList[-1][2] + str(informationList[-1][3])
            informationList[-1][2] = fullname
            i=3
            while (i < len(informationList[-1])-1):
                informationList[-1][i] = informationList[-1][i + 1]
                i = i + 1
            del (informationList[-1][-1])
            print("modified")
            print(informationList[-1])
        if re.match('government',informationList[-1][-1]):   #给数据分类
            informationList[-1][3] = 'government'
        elif re.match('politician', informationList[-1][-1]):
            informationList[-1][3] = 'politician'
        elif re.match('company', informationList[-1][-1]):
            informationList[-1][3] = 'company'
        elif re.match('tvshow', informationList[-1][-1]):
            informationList[-1][3] = 'tvshow'

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



def type_list():
    informationfile = open("./facebook_large/musae_facebook_target.txt", "r")
    informationList = []
    typelist=[]
    for information in informationfile.readlines():
        information = re.split(',', information)
        informationList.append(information)       #添加到我们建的列表
        informationList[-1][0]=int(informationList[-1][0])
        while(len(informationList[-1])>4):
            fullname = informationList[-1][2] + str(informationList[-1][3])
            informationList[-1][2] = fullname
            i=3
            while (i < len(informationList[-1])-1):
                informationList[-1][i] = informationList[-1][i + 1]
                i = i + 1
            del (informationList[-1][-1])
            print("modified")
            if re.match('government', informationList[-1][-1]):  # 给数据分类
                informationList[-1][3] = 'government'
            elif re.match('politician', informationList[-1][-1]):
                informationList[-1][3] = 'politician'
            elif re.match('company', informationList[-1][-1]):
                informationList[-1][3] = 'company'
            elif re.match('tvshow', informationList[-1][-1]):
                informationList[-1][3] = 'tvshow'
            typelist.append(str(informationList[-1][-1]))
            print(typelist[-1])

    return typelist

print(type_list())






