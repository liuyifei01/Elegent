import requests
import json

url = 'https://movie.douban.com/j/chart/top_list'

# url的参数过多，需要重新封装参数
start= input("请输入你想要查询的电影序列号(20的倍数)：")
param = {
    "type": "24",
    "interval_id": "100:90",
    "action": "",
    "start": start,
    "limit": 20,
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"

}

resp = requests.get(url=url, params=param, headers=headers)
# print(resp.json())
resp.close()    # 关掉请求
# 持久化存储
fp = open('douban.json', 'w', encoding='utf-8')
# 中文无法使用Ascii码
json.dump(resp.json(), fp=fp, ensure_ascii=False, indent=4)
fp.close()      # 关闭文档
print("a")
print("b")

print("c")
print("d")

