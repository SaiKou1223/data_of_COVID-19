import requests,json,time,csv
csv_file = open('C:\\Users\\LENOVO\Desktop\\sjyq.csv','w',newline='',encoding='utf-8')
# 世界疫情
writer = csv.writer(csv_file)
writer.writerow(['日期','累计确诊','累计死亡','累计治愈'])
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
    '_': '1590578850896',
# 毫秒时间戳 自行加
    'callback': 'dataAPIData'
}
url = 'https://gwpre.sina.cn/ncp/foreign?'
res = requests.get(url,params=params,headers=headers)
worldhistory_list = json.loads(res.text[16:-14])["result"]["history"]
c_data = []
for i in range(len(worldhistory_list)):
    date = worldhistory_list[i]["date"]
    certain = worldhistory_list[i]["certain"]
    die = worldhistory_list[i]["die"]
    recure = worldhistory_list[i]["recure"]
    c_data.append([date,certain,die,recure])
for row in c_data:
        writer.writerow(row)
csv_file.close()
print('OOOOOOOOOOOOK--------------------------------------------------------------------')