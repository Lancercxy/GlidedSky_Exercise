import requests
import parsel

#实现获取数据的方法
def add_num():
    #目的网址
    url = "http://www.glidedsky.com/level/web/crawler-basic-1"
    #由于网站需要登录，添加User-Agent与Cookie数据
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.70',
                'Cookie': 'footprints=eyJpdiI6ImdUK3JFa1JXOWVMSTJFVEoxQ3hIT0E9PSIsInZhbHVlIjoiMTF3VlwvOXBLdUxEajRyVmY2RGJkeGZxbk1xK1RLMmdqaG9aUEU3SlBCWHZtcmZBY2x5ODRhZjY1bWdWNEJXY0kiLCJtYWMiOiIxYjA0M2Q1MTJiOTRjM2ZiMTdlMGQ4YzhjMjM3ZThmYThiZGYxNjhkYWNhZTVkYmNjM2NmZWQyODI4MTRiYTUwIn0%3D; remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d=eyJpdiI6IjJNMFJlaEFjOUNHRVF2RnZpTGgzcVE9PSIsInZhbHVlIjoidXhRQ0VvYVorcDRLUEgySlkwN211UThjWjU2RU4rUENxQVlkblNaSGp3eWw1cVZQcDJ0MnhPZnpwNGxldzJCeW5pYW83UWVaeTFyY1JFZ052M1wvZE9OSkJTaVpPU0R6b0cwVFBjNnNEUCsxbDc4ZWRBcVplcXNyVnl0MHE3akRiK0lRMktybFc0eVwvXC9XaGFyNHEzck80cmhUcHNUZ3VYM2JjdU5EQ3Z2MytJPSIsIm1hYyI6Ijk1NmY5NzYyODlkOTQ1NzJlMDFkYmRhMzFlMjdkOWJiNWRlNjFmYzU5NDA4ZmMyZDM0NDFlZDAyNTc0Zjk0MjkifQ%3D%3D; XSRF-TOKEN=eyJpdiI6IjdZNEFuWlwvK0o0N0hrNkxuZGc2bEpnPT0iLCJ2YWx1ZSI6ImI1MXhkSUlod1BrdDRvWUxKSklkNDE2Qlo2QTBkTnNwZmxSbE5xdFVMcGJvaVNmdGtrN3U1cTRnYlU2SVwvZTZIIiwibWFjIjoiZjcwZGVlMjhlZWU5ZGNjYjFlYTY2NmRlNGM3ZTM4MWY5MjA2NDEzNGMxODU0YzMwMTZhMzgxMmI3ZmM5NTM3YiJ9; glidedsky_session=eyJpdiI6InF6OTM4N2ZKXC9RYllSckh3UlNKajJRPT0iLCJ2YWx1ZSI6IkFVTVBHekEybEZiaVpuVzNtNDdLczdGbmRQd2lkZkZoRCtSRkhOM25uQWdCeDNuTWtBWW5xRWNCbWZKVFRVQUgiLCJtYWMiOiI0NmU4Yzc2ZDg5MGQ3MzU1NWVhNDE3ODM4OGRjOTVhMzM3YjBkYmRhNDk4ZDcxZGJlNWUwM2ZjNWU3NWJlMDMxIn0%3D'
            }
    #请求网站
    ret = requests.get(url=url, headers=headers)
    #将数据转化为selector类型
    selector = parsel.Selector(ret.text)
    #通过css定位到目标元素
    rets = selector.css('#app > main > div.container > div > div > div > div')
    #创建用于保存数据的
    addNum = 0
    #循环获取每一个数并计算和
    for ret in rets:
        num = ret.css('::text').get()
        addNum = addNum+int(num)
        # print(num)
    #打印最终答案
    print("最终答案为：",addNum)

if __name__=='__main__':
    #调用方法
    add_num()