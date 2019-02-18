'''
    解析简单的xml文档
'''
'''
<?xml version="1.0"?>
<data>
    <country name=a11'>
        <rank updated="yes">111</rank>
        <year>2008</year>
    </country>
    <country name=a12'>
        <rank updated="yes">112</rank>
        <year>2009</year>
    </country>
</data>
'''
# 使用标准库中的xml.etree.ElementTree，其中的parse函数可以解析xml

from xml.etree.ElemenTree import parser

f = open('demo.xml')

et = parse(f)
print(et)
# 因无法导入包，放弃

