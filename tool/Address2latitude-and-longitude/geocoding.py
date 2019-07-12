'''
    将地理位置转换为坐标
'''
import requests


class geocoding():
    ''' 将地理位置转换为坐标 '''
    key = 'cc7515d2f731c56a203d3d82480f43d8'

    def __init__(self, key=''):
        ''' 修改key值 '''
        if key != '':
            self.key = key

    def url_joint(self, address):
        ''' 拼接网址和参数 '''
        self.gao_url = 'https://restapi.amap.com/v3/geocode/geo' + '?key=%s&address=%s' % (self.key, address)

    def url_get(self, get_type):
        ''' 获取json数据，可选择是全部返回还是只返回坐标 '''
        gao_url_get = requests.get(self.gao_url)
        if get_type == 'all':
            return gao_url_get.json()
        else:
            json_gao = gao_url_get.json()
            if json_gao['status'] == '1':
                if json_gao['geocodes'] != []:
                    return json_gao['geocodes'][0]['location']
            return 0

    def index(self, address, get_type='all'):
        ''' 入口方法 '''
        self.url_joint(address)
        content = self.url_get(get_type)
        return content


if __name__ == '__main__':
    g = geocoding()
    print(g.index('15054748439'))
