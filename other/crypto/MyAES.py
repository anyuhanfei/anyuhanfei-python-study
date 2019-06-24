# windows (pip install pycryptodomex)
from Cryptodome.Cipher import AES
from Cryptodome import Random

# linux (pip install pycryptodome)
# from Crypto.Cipher import AES
# from Crypto import Random

from binascii import b2a_hex # 将加密后的数据中的\x去除


class MyAES:
    '''
        使用aes加密算法封装一个加密解密类
    '''
    def __init__(self, key):
        '''
            初始化一个MyAES类，传入key参数作为密钥
            self.key 密钥
            self.iv 加盐
            self.mode 加密方式
        '''
        self.key = self.check_key(key).encode()
        self.iv = Random.new().read(AES.block_size)
        self.mode = AES.MODE_CFB

    def check_key(self, key):
        '''
            检查key长度是否符合aes要求;
            密钥key 长度必须为16（AES-128）、24（AES-192）、或32（AES-256）Bytes 长度.
        '''
        if len(key) in [16, 24, 32]:
            return key
        else:
            raise Exception('key的长度不符合要求!')

    def encrypt(self, data):
        '''
            加密
            使用初始化参数生成一个aes对象，用来加密；
            传入的需要加密的内容在加密前需要encode()编码
        '''
        cipher = AES.new(self.key, self.mode, self.iv)
        return cipher.encrypt(data.encode())

    def decrypt(self, data, is_decode=False):
        '''
            解密
            使用初始化参数生成一个aes对象，用来解密；
            is_decode参数判断解密后的数据是否需要decode()解码；
        '''
        cipher = AES.new(self.key, self.mode, self.iv)
        res = cipher.decrypt(data)
        return res if is_decode is False else res.decode()


if __name__ == "__main__":
    aes = MyAES("asdfghjkqwertyui")
    res_en = aes.encrypt('测试数据')
    print(b2a_hex(res_en))
    res_de = aes.decrypt(res_en, True)
    print(res_de)
