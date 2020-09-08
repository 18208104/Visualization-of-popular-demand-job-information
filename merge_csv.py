import pandas as pd
import glob
import csv

            #     'kanzhun*.csv'看准网数据合并
csv_num = glob.glob('lagou*.csv') #查看与该py文件同文件夹下的csv文件数
print(len(csv_num))#数目

csv_list=[]

for f in csv_num:
    csv_list.append(f)
    #print(f)

path='merge_csv.csv'
csv_head = ['name','company','company_size','field','workarea','salary','background','education']
with open(path, 'w', newline="", encoding='utf-8') as f:
    csv_write = csv.DictWriter(f, fieldnames=csv_head)  # 提前预览列名，当下面代码写入数据时，会将其一一对应。
    csv_write.writeheader()

for i in range(0, len(csv_list)):
    #print(csv_list[i])
    df = pd.read_csv(csv_list[i])
    # header=None表示原始文件数据没有列索引，这样的话read_csv会自动加上列索引
    df = df.iloc[:, [0, 1, 2, 3, 10,13,14,16]]  # 想保留的列的编号。0为起点
    df.to_csv(path, mode='a', index=None, encoding='utf-8', header=False)
    # header=False表示不保留列名，index=False表示不 保留行索引，mode='a'表示附加方式写入，文件原有内容不会被清除

#看准网和拉勾网数据合并
df2= pd.read_csv('kanzhun1.csv')
df2.to_csv(path, mode='a', index=None, encoding='utf-8', header=False)