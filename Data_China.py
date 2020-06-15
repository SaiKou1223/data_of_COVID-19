import requests,json,time,csv
csv_file = open('C:\\Users\\LENOVO\Desktop\\qgyq.csv','w',newline='',encoding='utf-8')
# 全国疫情
writer = csv.writer(csv_file)
writer.writerow(['日期','现存确诊','累计境外输入','现存无症状','现存确诊重症','累计确诊','累计死亡','累计治愈','现存疑似'])
headers = {
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'referer': 'https://news.sina.cn/zt_d/yiqing0121',
    'sec-fetch-dest': 'script',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'
    }
params = {
    '_': '1585756800000',
# 毫秒时间戳 自行加
    'callback': 'dataAPIData'
}
url = 'https://gwpre.sina.cn/interface/fymap2020_data.json?'
res = requests.get(url,params=params,headers=headers)
text = json.loads(res.text[12:-2])["data"]
history = text["historylist"]
c_data = []
for i in range(len(history)):
    date = history[i]["date"]
    xcqz = history[i]["cn_econNum"]
    # 现存确诊
    ljjwsr = history[i]["cn_jwsrNum"]
    # 累计境外输入
    xcwzz = history[i]["cn_asymptomNum"]
    # 现存无症状
    xcqzzz = history[i]["cn_heconNum"]
    # 现存确诊重症
    ljqz = history[i]["cn_conNum"]
    # 累计确诊
    ljsw = history[i]["cn_deathNum"]
    # 累计死亡
    ljzy = history[i]["cn_cureNum"]
    # 累计治愈
    xcys = history[i]["cn_susNum"]
    # 现存疑似
    c_data.append([date,xcqz,ljjwsr,xcwzz,xcqzzz,ljqz,ljsw,ljzy,xcys])
for row in c_data:
        writer.writerow(row)
csv_file.close()
print('OOOOOOOOOOOOK--------------------------------------------------------------------')