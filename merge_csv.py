import pandas as pd
import csv
            #     'kanzhun*.csv'看准网数据合并

#拉勾网数据文件
path_data='lagou10.csv'

path='总数据文件.csv'#合并文后件
path2='福利待遇.csv'#提取福利列文件
path3='金融阶段.csv'#金融阶段文件
path4='要求技能.csv'#技能

csv_head = ['name','company','company_size','field','workarea','salary','background','education']

with open(path, 'w', newline="", encoding='utf-8') as f:
    csv_write = csv.DictWriter(f, fieldnames=csv_head)  # 提前预览列名，当下面代码写入数据时，会将其一一对应。
    csv_write.writeheader()

df1 = pd.read_csv(path_data)
    # header=None表示原始文件数据没有列索引，这样的话read_csv会自动加上列索引
df = df1.iloc[:, [0, 1, 2, 3, 10,13,14,16]]  # 想保留的列的编号。0为起点
df.to_csv(path, mode='a', index=None, encoding='utf-8', header=False)
# header=False表示不保留列名，index=False表示不 保留行索引，mode='a'表示附加方式写入，文件原有内容不会被清除
df2=df1.iloc[:, [17]]
df2.to_csv(path2, mode='a', index=None, encoding='utf-8', header=True)
df3 = df1.iloc[:, [4]]
df3.to_csv(path3, mode='a', index=None, encoding='utf-8', header=True)
df4=df1.iloc[:, [7]]
df4.to_csv(path4 ,mode='a', index=None, encoding='utf-8', header=True)


#看准网和拉勾网数据合并
df2= pd.read_csv('kanzhun1.csv')
df2.to_csv(path, mode='a', index=None, encoding='utf-8', header=False)