# 导入相应的文件
import requests
import json
import time
import csv

# 加入请求头
headers = {
    "Accept": "*/*",
    "Referer": "https://www.kanzhun.com/search/?city=0&cityName=%E5%85%A8%E5%9B%BD&experience=0&industry=0&pageCurrent=1&q=%E6%89%BE%E8%81%8C%E4%BD%8D&salary=0&type=recruit",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36"
}


def create_csv():
    csv_head = ['positionName', 'companyName', 'companySize', 'industryName', 'city', 'salary',
                'experience', 'education']
    with open('kanzhun3.csv', 'w',newline="",encoding='utf-8') as f:
        csv_write = csv.DictWriter(f, fieldnames=csv_head)  # 提前预览列名，当下面代码写入数据时，会将其一一对应。
        #csv_write.writerow(csv_head)
        csv_write.writeheader()

def add_csv(data):
    path = "kanzhun3.csv"
    with open(path, 'a+',newline="",encoding='utf-8') as fd:
        w = csv.DictWriter(fd, data.keys())
        w.writerow(data)


# 获取cookies值



'''定义获取页数的函数'''
def get_page(url):
    html = requests.get(url,headers=headers)
    #print(html.text)
    r=html.text
    # 将网页的Html文件加载为json文件,
    json_data = json.loads(r)
    print(json_data)

    # 解析json文件，后跟中括号为解析的路径
    #total_Count = json_data['resdata']['totalCount']
    page_count = json_data['resdata']['pageCount']
    print(page_count)

    '''if page_number<1000:
        page_number=1000
    else:
        page_number=1000
     '''
    '''
    先爬1000页
    '''
    # 调用get_info函数，传入url和页数
    get_info(page_count)


# 定义获取招聘信息函数
def get_info( page):
    '''
    中途中断可计算那页，往后爬取
    '''
    for pn in range(1, page+1):
        # post请求参数
        url1="https://www.kanzhun.com/search/job.json?query=%E6%89%BE%E8%81%8C%E4%BD%8D&type=0&cityCode=0&industryCodes=0&experienceId=0&salaryId=0&pageNum="+str(pn)+"&limit=15"
        # 获取信息 并捕获异常
        try:
            html = requests.get(url1,headers=headers, timeout=50)
            print(url1, html.status_code)
            # 将网页的Html文件加载为json文件
            json_data = json.loads(html.text)
            # 解析json文件，后跟中括号为解析的路径
            results = json_data['resdata']['jobs']

            for result in results:
                infos = {
                    "positionName": result["positionName"],#名称
                    "companyName": result["companyName"],#公司名称
                    "companySize": result["scaleDes"],#公司规模
                    "industryName": result["industryName"],#内容
                    "city": result["cityName"],#城市
                    "salary": result["salary"],  #工资
                    "experience": result["experience"],#经验
                    "education": result["degree"],#学历
                }
                print(infos)
                # 插入
                add_csv(infos)
                # 睡眠2秒
                time.sleep(2)
        except requests.exceptions.ConnectionError:
            print("requests.exceptions.ConnectionError")
            pass


# 主程序入口
if __name__ == '__main__':
    url = "https://www.kanzhun.com/search/job.json?query=%E6%89%BE%E8%81%8C%E4%BD%8D&type=0&cityCode=0&industryCodes=0&experienceId=0&salaryId=0&pageNum=1&limit=15"
    # post请求参数

    create_csv()
    get_page(url)