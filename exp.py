import requests

url = "https://jwxt.sztu.edu.cn/jsxsd/xspj/xspj_find.do"
headers = {
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Cookie":"JSESSIONID=60C9840BEA55A728C686E823A7EBE9ED; JSESSIONID=90E8268C913100564EBC347EC10E192E; SERVERID=124",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.51"
}



r = requests.get(url)

print(r.content)