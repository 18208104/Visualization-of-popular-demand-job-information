# 导入相应的文件
import requests
import json
import time
import csv


# 加入请求头
headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Referer": "https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",
}


def create_csv():
    csv_head = ['positionName', 'companyFullName', 'companySize', 'industryField', 'financeStage', 'firstType',
                'secondType', 'thirdType', 'positionLables', 'createTime', 'city', 'district', 'businessZones',
                'salary', 'workYear', 'jobNature', 'education', 'positionAdvantage']
    with open('lagou1.csv', 'w',newline="",encoding='utf-8') as f:
        csv_write = csv.DictWriter(f, fieldnames=csv_head)  # 提前预览列名，当下面代码写入数据时，会将其一一对应。
        #csv_write.writerow(csv_head)
        csv_write.writeheader()

def add_csv(data):
    path = "lagou1.csv"
    with open(path, 'a+',newline="",encoding='utf-8') as fd:
        w = csv.DictWriter(fd, data.keys())
        w.writerow(data)


# 获取cookies值
def get_cookie():
    # 原始网页的URL
    url = "https://www.lagou.com/jobs/list_/p-city_0?px=new#filterBox"
    s = requests.Session()
    s.get(url, headers=headers, timeout=10)  # 请求首页获取cookies
    cookie = s.cookies  # 为此次获取的cookies
    return cookie


'''定义获取页数的函数'''
def get_page(url, params):
    html = requests.post(url, data=params, headers=headers, cookies=get_cookie(), timeout=20)
    # 将网页的Html文件加载为json文件
    json_data = json.loads(html.text)
    # 解析json文件，后跟中括号为解析的路径
    total_Count = json_data['content']['positionResult']['totalCount']
    page_number = int(total_Count / 15)
    if page_number<30:
        page_number=200
    else:
        page_number=200
    '''
    先爬200页
    '''
    # 调用get_info函数，传入url和页数
    get_info(url, page_number)


# 定义获取招聘信息函数
def get_info(url, page):
    '''
    中途中断可计算那页，往后爬取
    '''
    for pn in range(1, page + 1):
        # post请求参数
        params = {
            "first": "true",
            "pn": str(pn),
            "kd": ""
        }
        # 获取信息 并捕获异常
        try:
            html = requests.post(url, data=params, headers=headers, cookies=get_cookie(), timeout=40)
            print(pn,url, html.status_code)
            # 将网页的Html文件加载为json文件
            json_data = json.loads(html.text)
            # 解析json文件，后跟中括号为解析的路径
            results = json_data['content']['positionResult']['result']

            for result in results:
                infos = {
                    "positionName": result["positionName"],#职业名称
                    "companyFullName": result["companyFullName"],#公司
                    "companySize": result["companySize"],#公司规模
                    "industryField": result["industryField"],
                    "financeStage": result["financeStage"],
                    "firstType": result["firstType"],
                    "secondType": result["secondType"],
                    "thirdType": result["thirdType"],
                    "positionLables": result["positionLables"],
                    "createTime": result["createTime"],#时间
                    "city": result["city"],#城市
                    "district": result["district"],
                    "businessZones": result["businessZones"],
                    "salary": result["salary"],#工资
                    "workYear": result["workYear"],#经验
                    "jobNature": result["jobNature"],
                    "education": result["education"],#教育程度
                    "positionAdvantage": result["positionAdvantage"]
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
    url = "https://www.lagou.com/jobs/positionAjax.json"
    # post请求参数
    params = {
        "first": "true",
        "pn": 1,
        "kd": ""
    }
    create_csv()
    get_page(url, params)