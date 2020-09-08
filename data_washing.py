import pandas as pd

#读取文件
data = pd.read_csv('merge_csv.csv',header=0)#


#转换为字符串
data=data.astype(str)


#文件查重
data = data.drop_duplicates()



#删除含有缺失值的行（含有缺失值的行少，直接删除）
data.dropna(axis=0, how='any', inplace=True)

#显示缺失值数量
# print(data.isnull().any().sum())

#含有缺失值列
#print(data.isnull().any())



#提取工资范围
#print(data['salary'].str.split('-',expand=True))
data=pd.concat([data, data['salary'].str.split('-',expand=True)],axis=1)
#print(data)


#统一列名
data.drop(columns=["salary"],inplace=True)
data.columns =['name','company','company_size','field','workarea','background','education','low_salary','high_salary']


#统一单位
data['low_salary'] = data['low_salary'].map(lambda x: x.rstrip('k'))
data['high_salary'] = data['high_salary'].map(lambda x: x.rstrip('k'))


#保存文件
data.to_csv('wash_data.csv',index=False, encoding='utf-8')
