#coding=utf-8
import json,time,requests,sys,csv
csv_file = open('C:\\Users\\LENOVO\Desktop\\cs.csv','w',newline='',encoding='utf-8')
# 各个城市
writer = csv.writer(csv_file)
writer.writerow(['城市','日期','累计确诊','累计治愈','现存确诊','累计死亡','现存无症状'])
url = 'https://gwpre.sina.cn/interface/wap_api/feiyan/sinawap_get_area_tree.d.json?'
params = {
    'callback': 'yan_getdata'
}
headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'
}
res = requests.get(url,params=params,headers=headers)
text =json.loads(res.text[12:-2])["data"]["cities_cn"]
for x in range(len(text)):
    print("遍历城市成功辽！")
    city = text[x]["c"]
    link = text[x]["e"]
    print(city,link)
    url_base = 'https://gwpre.sina.cn/interface/news/ncp/data.d.json?mod=province&province={}&callback=_aProvinceFunction&_=1590562538833'.format(link)
    print(url_base)
    response = requests.get(url_base,headers=headers)
    print(response.status_code)
    txt = response.text
    City_list = json.loads(txt[19:-2])["data"]["historylist"]
    num_list = []
    for x in range(len(City_list)):
        print("遍历日期成功辽！")
        date = City_list[x]["date"]
        conNum = City_list[x]["conNum"]
        # 累计确诊
        cureNum = City_list[x]["cureNum"]
        # 累计治愈
        econNum = City_list[x]["econNum"]
        # 现存确诊
        deathNum = City_list[x]["deathNum"]
        # 累计死亡
        asymptomNum = City_list[x]["asymptomNum"]
        # 现存无症状
        # print("日期：",date,"累计确诊：",conNum,"累计治愈：",cureNum,"现存确诊：",econNum,"累计死亡：",deathNum,"现存无症状：",asymptomNum)
        num_list.append([city,date,conNum,cureNum,econNum,deathNum,asymptomNum])
    print(city,"success!")
    for row in num_list:
        writer.writerow(row)
csv_file.close()  
print("DONE!")