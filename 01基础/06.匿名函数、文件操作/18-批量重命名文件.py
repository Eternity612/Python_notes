import os

#1.获取要重命名的文件夹名字
folder_name = input("请输入想要重命名的文件名：")

#2.获取指定的文件夹中的所有文件名
names = os.listdir(folder_name)
print(names)
os.chdir(folder_name)   #改变默认的操作路径

#3.重命名
for name in names:
    print(name)
    os.rename(name,"京东出品-"+name)
