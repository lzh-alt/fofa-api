import base64
import json
import re
import requests
import urllib3


def fofa_search(search_data):
    """开始发送 fofa 扫描请求"""

    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    data = {
        "key": "4efd9a21cc4f276101f51fac5f4bc31e",
        "qbase64": base64.b64encode(search_data.encode("UTF-8")),
        "fields": 'ip,port,city,host,os,server,title,jarm',
    }
    req = requests.get(url='https://fofa.info/api/v1/search/all', verify=True, params=data, timeout=10)
    print(req)
    if req.status_code != 200:
        print('fofa 请求失败，请检查配置')
        return False

    data = req.json()
    if data.get("error", True) is not False:
        print('fofa 请求失败，请检查配置')
        return False

    string_data = json.dumps(data, ensure_ascii=False)

    # 使用正则表达式匹配方括号内的内容并保留下来
    pattern1 = r'\[(.*?)\]'
    result = re.findall(pattern1, string_data)
    result = '\n'.join(result)
    result = re.sub(r'\[', '\0', result)

    print(result)

    # print(data)
    return True

if __name__ == '__main__':
    search_data = 'city="Nanjing" && host="cas.zzjc.edu.cn"'
    fofa_search(search_data)
