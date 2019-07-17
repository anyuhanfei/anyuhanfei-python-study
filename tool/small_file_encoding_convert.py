class SmallFileEncodingConvert:
    '''
        小体积文件编码转换
        一次性读取完文件的内容，一次性写入文件内容，大体积文件可能会导致内存占满
    '''
    be_convert_file = ''
    be_convert_file_encoding = ''
    convert_file = ''
    convert_file_encoding = ''

    def __init__(self):
        '''
            初始化编码格式和文件路径
        '''
        self.update_be_convert_file()
        self.update_be_convert_file_encoding()
        self.update_convert_file_encoding()
        self.update_convert_file()

    def input(self, content, input_content):
        '''
            如果不传入内容则让用户输入
        '''
        if content == '':
            return input(input_content)
        else:
            return content

    def update_be_convert_file(self, file_path='', input_content='请输入被转换编码格式的文件路径：'):
        '''
            修改被转换编码格式的文件路径
        '''
        self.be_convert_file = self.input(file_path, input_content)

    def update_be_convert_file_encoding(self, encoding='', input_content='请输入被转换文件的编码格式：'):
        '''
            修改被转换文件的编码格式
        '''
        self.be_convert_file_encoding = self.input(encoding, input_content)

    def update_convert_file(self, file_path='', input_content='请输入目的文件路径(不输入则替换原文件)：', be_convert_file=None):
        '''
            修改目的文件路径
        '''
        be_convert_file = self.be_convert_file
        input_return = self.input(file_path, input_content)
        self.convert_file = be_convert_file if input_return == '' else input_return

    def update_convert_file_encoding(self, encoding='', input_content='请输入目的编码格式：'):
        '''
            修改目的编码格式
        '''
        self.convert_file_encoding = self.input(encoding, input_content)

    def convert(self):
        '''
            进行转换
        '''
        while True:
            try:
                with open(self.be_convert_file, 'r', encoding=self.be_convert_file_encoding) as b:
                    be_convert_file_read = b.read()
            except BaseException:
                print('文件打开错误！')
            try:
                if be_convert_file_read:
                    with open(self.convert_file, 'w', encoding=self.convert_file_encoding) as u:
                        u.write(be_convert_file_read)
            except BaseException:
                print('文件写入错误！')
            is_go_on = input('是否进行下一个文件编码的转换？(y/n)')
            if is_go_on == 'y':
                res = self.next()
                if res is False:
                    break
            else:
                break

    def next(self):
        '''
            进行下一个文件编码转换的配置
        '''
        print('可选择的选项：<br/>')
        print('1：只修改被转换编码格式的文件路径')

        print('2：修改被转换编码格式的文件路径和被转换文件的编码格式')
        print('3：修改被转换编码格式的文件路径和目的编码格式')
        print('4：修改被转换编码格式的文件路径和目的文件路径')

        print('5：修改被转换编码格式的文件路径、被转换文件的编码格式和目的编码格式')
        print('6：修改被转换编码格式的文件路径、被转换文件的编码格式和目的文件路径')

        print('7：修改被转换编码格式的文件路径、被转换文件的编码格式、目的编码格式和目的文件路径')
        convert_type = int(input('请修改下一次转换的配置：'))
        if convert_type <= 7 and convert_type >= 1:
            self.update_be_convert_file()
            self.update_convert_file(self.be_convert_file)
        if convert_type == 1:
            pass
        elif convert_type == 2:
            self.update_be_convert_file_encoding()
        elif convert_type == 3:
            self.update_convert_file_encoding()
        elif convert_type == 4:
            self.update_convert_file()
        elif convert_type == 5:
            self.update_be_convert_file_encoding()
            self.update_convert_file_encoding()
        elif convert_type == 6:
            self.update_be_convert_file_encoding()
            self.update_convert_file()
        elif convert_type == 7:
            self.update_be_convert_file_encoding()
            self.update_convert_file_encoding()
            self.update_convert_file()
        else:
            over = input('您输入了未知的选项,是否结束(y/n):')
            return True if over == 'y' else False
        return True


if __name__ == '__main__':
    fec = SmallFileEncodingConvert()
    fec.convert()
