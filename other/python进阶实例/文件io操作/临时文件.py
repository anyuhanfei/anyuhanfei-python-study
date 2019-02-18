'''
    使用临时文件
'''
'''
    某些项目的数据是一次性的，如果常驻内存，则将消耗大量内存资源，可以使用临时文件存储这些临时数据（外部存储）
    临时文件不用命名，且关闭后会自动被删除
'''
# 使用标准库中tempfile下的TemporaryFile，NamedTemporaryFile
from tempfile import TemporaryFile, NamedTemporaryFile

f = TemporaryFile()
f.write(b'asdf' * 10000)
f.seek(0)
for i in range(1,10):
    print(f.read(100))

# TemporaryFile()创建的临时文件不能由文件系统路径找到它，
# 如果想要创建文件系统路径可以找到的临时文件，可以由NamedTemporaryFile()函数创建
ntf = NamedTemporaryFile()
print(ntf.name)  # 这就是临时文件的名字
# 临时文件在关闭之后会被删除，如果不想被删除，可以在实例化是使用delete=False参数