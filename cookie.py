import urllib3
import cookie

print('start')
cookie = cookielib.CookieJar()
opener = urllib3.build_opener(urllib3.HTTPCookieProcessor(cookie))
response = opener.open('http://www.zhihu.com')
for item in cookie:
    print(item.name +':' item.value)
print('over')    