import requests
import sys
import os
school_id = {}
#school_id[input()]
print("请输入毕业年级:")
year = input()
print("小学/初中/高中:1/2/3")
typ = input()
print("请输入学校代码,不确定请输入“-1”:")
school = input()
if school == "-1":
    print("请输入学校名称或关键字:")
    f = open('data/school_id.dat', 'r')
    dictid = eval(f.read())
    temp = input()
    p = 0
    for key in dictid:
        if temp in key:
            if p == 0:
                print("搜索到全称中包含" + temp + "的学校:")
                p = 1
            print(key)
    print("请确认输入学校全称:")
    school = dictid[input()][2:11]
f = open('data/school_id.dat', 'r')
dictid = eval(f.read())
#print(dictid[input()])
#print(dictid)
print("请输入教育ID,不确定请输入“-1”进入遍历模式获取全年级文件，耗时较长:")
eid = input()
print("Working...")
if int(eid) == -1:
    for i in range(9000000, 9140000):
        img_url = "http://211.153.82.210/cmisfolder/photos/201200" + str(typ) + "/" + str(year) + "/" + str(school) + "/" + str("%08d" % i) + ".jpg"
        #print(img_url)
        img = requests.get(img_url) 
        #print(sys.getsizeof(img))
        name = str("%05d" % i) + ".jpg"
        f = open(name,'ab')
        f.write(img.content)
        f.close()
        fsize = os.path.getsize(name)
        if fsize < 500:
            os.remove(name)
else:
    img_url = "http://211.153.82.210/cmisfolder/photos/201200" + str(typ) + "/" + year + "/" + school + "/" + eid + ".jpg"
    print(img_url)
    img = requests.get(img_url) 
    #print(sys.getsizeof(img))
    name = str(eid) + ".jpg"
    f = open(name,'ab')
    f.write(img.content)
    f.close()

    fsize = os.path.getsize(name)
    if fsize < 500:
        os.remove(name)
print("Done!")