import requests
import sys
import os
print("请输入毕业年级:")
year = input()
print("请输入学校代码(查询见表格,后续加入搜索功能,不确定请输入“-1”):")
school = input()
if int(school) == -1:
    print("功能开发中")
    exit()

print("请输入教育ID,不确定请输入“-1”:")
eid = input()
if int(eid) == -1:
    for i in range(9000000, 9140000):
        for j in range(0,11):
            img_url = "http://211.153.82.210/cmisfolder/photos/2012" + str("%03d" % j) + "/" + str(year) + "/" + str(school) + "/" + str("%08d" % i) + ".jpg"
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
    for j in range(0,11):
        img_url = "http://211.153.82.210/cmisfolder/photos/2012" + str("%03d" % j) + "/" + year + "/" + school + "/" + eid + ".jpg"
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