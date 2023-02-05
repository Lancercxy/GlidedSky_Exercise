import requests
import parsel
import random


def add_num():
    url = "http://www.glidedsky.com/level/web/crawler-basic-1"

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.70',
                'Cookie': 'footprints=eyJpdiI6InRMRGFuMStzZGM2R3Z5VWVzUHc3Z3c9PSIsInZhbHVlIjoiSmhTOHI3SVRGWHFYcVd2cXE2NkRGZjFEaVRZa0syWUp2d2dcL2FzWlJGelBhQmlSaktTcmhFVzNkc1hjUHVnU2MiLCJtYWMiOiJmOGFjNWU4MTBjNGIyNzYyYTE1MGEwOTZlMzhmNjgwNWE1ZWUwNjdkZTRkZDM3MDM5MWIwNWYyMmFkZTFkMjk0In0%3D; remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d=eyJpdiI6IlFDTUcyNFArSDdOQ0h1eWFcLzhFaHZBPT0iLCJ2YWx1ZSI6IkREanZRS3o3VUI0WGFzNXVCKzQzb0lwdjhaQ21pNFByaW1ZVFdMXC9sNFFoOUxia0xJRDdZNXZIMzJPaEVlM0dtVXA5bXN5c0FwaFI1dTBCT0RxZ2dvTkkwcGZWbVhHMXZUNFhISUZXOXg1V1ZtS0QrY00waEFsUFwvMWw3M09zZDE1aU9OS2w4WStodmNORG44bzRYTWo2ajZkVVwvdkZKWWpZSkZRXC9QXC9uYnhjPSIsIm1hYyI6ImI4ZWYwOTE3MDlmYzViODcyMGU0ZGY3ZWI2M2Q3NzI5N2Y5ZTUxYjJiNTcwNzRiZmJlYzNhMmRhMmUxODE3NjYifQ%3D%3D; XSRF-TOKEN=eyJpdiI6IlFxdzJZS2dmUGNsUkZZK08rdE5WckE9PSIsInZhbHVlIjoiaVwvcjJWd2ZmSEdcL3k5dXBNXC83Y3QzMnM4Tk9kRUxKaDlZM08yVjRjS2hGN1IrU001bTh4RjV5c0ZRdU9LNHlLaiIsIm1hYyI6IjgxMWY1MzU3NTRiMjFmMTBlNWIxMmZlYTVjNzUyNmQ0YzIyNzY2NGQwYjNiZDY4NjE3ZWZmZjIzZWYzYTZkYzIifQ%3D%3D; glidedsky_session=eyJpdiI6IjhKWDZOb2dDaUQ4QkJGdm1QOGdCQUE9PSIsInZhbHVlIjoiYnNNNVFCZ3pnNUJsWGVJZVVPUks5bnVGSkxSMkthUCtJVDAwRGdQbEEwYThvTjRtRXhmK2RZZmJ0WG92NUs2aiIsIm1hYyI6IjUzNGFjYzRmYTJkYzJkZTZjOTk3NjJhMGJiMGI4MmZlZjZkOWQzZmQ4Y2RlNTUyMjY4ZDhhMDA1OTBjOTQ2MzgifQ%3D%3D'
            }
    ret = requests.get(url=url, headers=headers)
    # print(ret.text)
    selector = parsel.Selector(ret.text)

    rets = selector.css('#app > main > div.container > div > div > div > div')
    # app > main > div.container > div > div > div
    # app > main > div.container > div > div > div > div:nth-child(1)
    # app > main > div.container > div > div > div > div:nth-child(2)
    # print(rets)
    i = 0
    for ret in rets:
        num = ret.css('::text').get()
        i = i+int(num)
        # print(num)
    print(i)

if __name__=='__main__':
    add_num()