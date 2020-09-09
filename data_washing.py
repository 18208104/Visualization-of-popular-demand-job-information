import pandas as pd

#读取文件
data1 = pd.read_csv('总数据文件.csv',header=0)#

#转换为字符串
data1=data1.astype(str)

#文件查重
data1 = data1.drop_duplicates()

#删除含有缺失值的行（含有缺失值的行少，直接删除）
data1.dropna(axis=0, how='any', inplace=True)

#显示缺失值数量
# print(data.isnull().any().sum())
#含有缺失值列
#print(data.isnull().any())
#含有特殊字符的行
#df2 = data1[data1['salary'].str.contains('元/天')]
#print(df2)

data=data1[~data1['salary'].str.contains('元/天')]
#通过~取反，选取不包含数字1的行

#提取工资范围
#print(data['salary'].str.split('-',expand=True))
data=pd.concat([data, data['salary'].str.split('-',expand=True)],axis=1)
#print(data)

#统一列名
data.drop(columns=["salary"],inplace=True)
data.columns =['name','company','company_size','field','workarea','background','education','low_salary','high_salary']

newName = data['low_salary'].str.strip();
data['low_salary'] = newName;

#统一单位
data['low_salary'] = data['low_salary'].map(lambda x: x.rstrip('k'))
data['high_salary'] = data['high_salary'].map(lambda x: x.rstrip('k'))


#保存文件
data.to_csv('清洗后数据.csv',index=False, encoding='utf-8')
