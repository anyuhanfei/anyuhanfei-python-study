import rsa
from binascii import b2a_hex # 将加密后的数据中的\x去除


class MyRSA:
    '''
        使用rsa加密算法封装一个加密类
    '''
    def __init__(self, rsa_n, rsa_e='10001'):
        '''
            初始化一个MyAES类
            self.rsa_n 公钥n
            self.rsa_e 公钥e
            self.publicKey 公钥
        '''
        self.rsa_n = int(rsa_n, 16)
        self.rsa_e = int(rsa_e, 16)
        self.publicKey = rsa.PublicKey(self.rsa_n, self.rsa_e)

    def encrypt(self, data):
        '''
            加密
        '''
        return rsa.encrypt(data.encode(), self.publicKey)


if __name__ == "__main__":
    publickey_n = ''
    a = MyRSA(publickey_n)
    h2a_hex(a.encrypt('测试数据'.encode()))
