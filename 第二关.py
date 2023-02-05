import requests
import parsel


#实现获取数据的方法
def add_num():
    #创建用于保存所有页数据的变量
    addNum = 0
    for i in range(1, 1001):
        #目的网址
        url = f"http://www.glidedsky.com/level/web/crawler-basic-2?page={i}"
        #由于网站需要登录，添加User-Agent与Cookie数据
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.70',
                    'Cookie': 'footprints=eyJpdiI6ImdUK3JFa1JXOWVMSTJFVEoxQ3hIT0E9PSIsInZhbHVlIjoiMTF3VlwvOXBLdUxEajRyVmY2RGJkeGZxbk1xK1RLMmdqaG9aUEU3SlBCWHZtcmZBY2x5ODRhZjY1bWdWNEJXY0kiLCJtYWMiOiIxYjA0M2Q1MTJiOTRjM2ZiMTdlMGQ4YzhjMjM3ZThmYThiZGYxNjhkYWNhZTVkYmNjM2NmZWQyODI4MTRiYTUwIn0%3D; remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d=eyJpdiI6IjJNMFJlaEFjOUNHRVF2RnZpTGgzcVE9PSIsInZhbHVlIjoidXhRQ0VvYVorcDRLUEgySlkwN211UThjWjU2RU4rUENxQVlkblNaSGp3eWw1cVZQcDJ0MnhPZnpwNGxldzJCeW5pYW83UWVaeTFyY1JFZ052M1wvZE9OSkJTaVpPU0R6b0cwVFBjNnNEUCsxbDc4ZWRBcVplcXNyVnl0MHE3akRiK0lRMktybFc0eVwvXC9XaGFyNHEzck80cmhUcHNUZ3VYM2JjdU5EQ3Z2MytJPSIsIm1hYyI6Ijk1NmY5NzYyODlkOTQ1NzJlMDFkYmRhMzFlMjdkOWJiNWRlNjFmYzU5NDA4ZmMyZDM0NDFlZDAyNTc0Zjk0MjkifQ%3D%3D; XSRF-TOKEN=eyJpdiI6Imp4bkJHNVByOFNDZXN1Z0l0ek9COHc9PSIsInZhbHVlIjoib2FmVkdPZjFXSllWVHRJMVVWdDlsU3dYU3EyTE1HNFV4eXFrZVBKcDlFU0Q3NFVUK2VmbWpicTJxeEtNWk0rcCIsIm1hYyI6ImJjNDFlYjU3OWU4ZGMyNmVlYTEzZTA5ZTBhZTQ0NTRlOGRhNGM3MjI4MmYwZGI4NTUwMjY0NmJlMTVhMmVjMTMifQ%3D%3D; glidedsky_session=eyJpdiI6IkFKSVhnU1ZnV2xvTThsZ1VuNTdrS0E9PSIsInZhbHVlIjoidTR5Sk8yYmZFR2VJQUhMZXRXTlwvZUQ3UHV0bGIxM1pHcjRyVmlXUUorZTZVNHY3emc5MEFURXB4Y2lMRmZ4R0YiLCJtYWMiOiJhNjYzMDZiMTY5MDNkZmI3NTIwZjFhYjg5YTc5NjlkOTA0OWE4ZGY5ZWU5OGU0YTQ5MWUzN2QxMWRmYzRlYTc3In0%3D'
                }
        #请求网站
        ret = requests.get(url=url, headers=headers)
        #将数据转化为selector类型
        selector = parsel.Selector(ret.text)
        #通过css定位到目标元素
        rets = selector.css('#app > main > div.container > div > div > div > div')
        #创建用于保存一页数据的变量
        onepage_addNum = 0
        #循环获取每一个数并计算和
        for ret in rets:
            num = ret.css('::text').get()
            onepage_addNum = onepage_addNum+int(num)
            # print(num)
        addNum = addNum+onepage_addNum
    #打印最终答案
    print("最终答案为：",addNum)

if __name__=='__main__':
    #调用方法
    add_num()