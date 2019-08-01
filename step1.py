import requests

# 使用 requests 库可以请求网页


# 主函数
if __name__=="__main__":
    # 浏览器头
    header = {
        'Accept': 'text / html, application / xhtml + xml, application / xml; q = 0.9, image / webp, * / *;q = 0.8',
        'Accept - Encoding': 'gzip, deflate, sdch',
        'Accept - Language': 'zh-CN,zh;q = 0.8',
        'Cache - Control': 'max-age=0',
        'Connection': 'keep - alive',
        'Cookie':'cy=2; cityid=2; cye=beijing; _lxsdk_cuid=16c1de5329dc8-067648637d919f-4d045769-1fa400-16c1de5329ec8; _lxsdk=16c1de5329dc8-067648637d919f-4d045769-1fa400-16c1de5329ec8; _hc.v=f1d1cb8b-09e8-e3ca-beb5-ae8a7642dbb3.1563869656; Hm_lvt_e6f449471d3527d58c46e24efb4c343e=1563869658; Hm_lpvt_e6f449471d3527d58c46e24efb4c343e=1563869683; ua=dpuser_5018876716; ctu=f35c58dbc6235d3b52f43ee8a7642e06a4718b421fba467e17ec170a86fc54d7; uamo=17375899343; cy=2; cye=beijing; s_ViewType=10; _lxsdk_s=16c4cdc33ef-8a3-764-105%7C%7C534',
        'Upgrade - Insecure - Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'
    }
    # 请求网页
    response = requests.get("http://www.dianping.com/shop/28576064", headers = header)
    # 获取网页所有的信息
    content = response.content.decode("utf-8")
    # 打印
    print(content)


