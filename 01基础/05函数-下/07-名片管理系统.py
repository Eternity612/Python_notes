#1.打印功能提示
print("="*50)
print("    名片管理系统  v0.01")
print("1.添加一个新名片")
print("2.删除一个名片")
print("3.修改一个名片")
print("4.查询一个名片")
print("5.显示所有的名片")
print("6.退出系统")
print("="*50)

#用来存储名片
card_info = []

while True:
    #2.获取用户的输入
    num = int(input("请输入操作序号："))

    #3.根据用户输入的序号执行相应的功能
    if num == 1:
        new_name = input("请输入姓名：")
        new_qq = input("请输入新的QQ：")
        new_weixin = input("请输入微信：")
        new_addr = input("请输入地址：")

        #定义一个新的字典，用来存储一个新的名片
        new_info = {}
        new_info["name"] = new_name
        new_info["qq"] = new_qq
        new_info["weixin"] = new_weixin
        new_info["addr"] = new_addr

        #将字典添加到名片列表中
        card_info.append(new_info)

    elif num ==2:
        pass
    elif num ==3:
        pass
    elif num ==4:
        find_name = input("请输入要查询的姓名：")

        for temp in card_info:
            if find_name == temp["name"]:
                #print("姓名\tQQ\t微信\t住址")
                print("姓名：%s\nQQ：%s\n微信：%s\n住址：%s"%(temp["name"],temp["qq"],temp["weixin"],temp["addr"]))
                break

            else:
                print("查无此人……")

    elif num ==5:
        for temp in card_info:
            #print("姓名\tQQ\t微信\t住址")
            print("姓名：%s\nQQ：%s\n微信：%s\n住址：%s" % (temp["name"], temp["qq"], temp["weixin"], temp["addr"]))

    elif num ==6:
        break
    else:
        print("输入有误，请重新输入")

    print("")