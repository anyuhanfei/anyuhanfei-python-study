'''
    实现可迭代对象和迭代器对象
    字符串，列表，元组，字典和集合都是可迭代对象，由iter(可迭代对象)得到迭代器对象；
    实际上，数据类型中存在__iter__魔法方法（存在__getitem__也是可以的）的数据类型都是可迭代对象，调用iter()函数实际上就是调用__iter__魔法方法；
    迭代器对象只有一个方法，next()方法，返回当前元素并指向下一个元素；
'''
'''
    一个查询城市气温的软性，从网络上抓取信息。
    如果一次抓取所有城市的天气再显示，那么就会有很高的延迟，我们可以用
    ‘用时访问’的策略。
    模仿可迭代对象和迭代器对象来创建一个专职功能的类
'''
import requests
from collections import Iterable, Iterator

class WeatherIterator(Iterator):
    ''' 实现一个迭代器对象Weatherlterator，next方法每次返回一个城市气温 '''
    def __init__(self, cities):
        ''' 所有需要查询城市的字典，初始化指针 '''
        self.cities = cities
        self.index = 0

    def getWeather(city):
        ''' 获取城市天气，此网站已关闭 '''
        r = requests.get(u'http://wthrcdn.etouch.cn/weater_mini?city=' + city)
        data = r.json()['data']['forecast'][0]
        return '%s: %s, %s' % (city, data['low'], data['high'])
    
    def next(self):
        if self.index = len(self.cities):
            raise StopIteration
        city = self.cities[self.index]
        self.index += 1
        return self.getWeather(city)

class WeatherIterable(Iterable):
    ''' 实现一个可迭代对象Weatherlterable，__iter__方法返回一个迭代器对象 '''
    def __init__(self, cities):
        ''' 所有需要查询城市的字典'''
        self.cities = cities
    
    def __iter__(self):
        ''' 返回一个迭代器对象 '''
        return WeatherIterator(self.cities)

if __name__ == '__main__' :
    for x in WeatherIterable([u'北京', u'上海', u'广州', u'郑州']):
        print(x) # 返回的就是四个城市的气温信息。

