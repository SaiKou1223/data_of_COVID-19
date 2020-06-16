#coding=utf-8
import json,time,requests,sys,csv
csv_file = open('C:\\Users\\LENOVO\Desktop\\ggyq.csv','w',newline='',encoding='utf-8')
# 各国疫情
writer = csv.writer(csv_file)
writer.writerow(['国家','日期','累计确诊','累计治愈','累计死亡'])
url = 'https://gwpre.sina.cn/interface/wap_api/feiyan/sinawap_get_area_tree.d.json?'
params = {
    'callback': 'yan_getdata'
}
headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'
}
res = requests.get(url,params=params,headers=headers)
text =json.loads(res.text[12:-2])["data"]["countries"]
countrynum_list = []
for x in range(len(text)):
    print("遍历国家成功辽！")
    city = text[x]["c"]
    link = text[x]["i"]
    print(city,link)
    url_base = 'https://gwpre.sina.cn/interface/news/wap/ncp_foreign.d.json?citycode={}&_=1590570483531&callback=_dataAPIData'.format(link)
    print(url_base)
    response = requests.get(url_base,headers=headers)
    print(response.status_code)
    txt = response.text
    City_list = json.loads(response.text[13:-2])["data"]["historylist"]
    num_list = []
    # time.sleep(2)
    for x in range(len(City_list)):
        print("遍历日期成功辽！")
        date = City_list[x]["date"]
        conNum = City_list[x]["conNum"]
        # 累计确诊
        cureNum = City_list[x]["cureNum"]
        # 累计治愈
        deathNum = City_list[x]["deathNum"]
        # 累计死亡
        num_list.append([city,date,conNum,cureNum,deathNum])

    countrynum_list =countrynum_list + num_list
    print(city, "success!")
for row in countrynum_list:
        writer.writerow(row)

csv_file.close()
print("DONE!")
