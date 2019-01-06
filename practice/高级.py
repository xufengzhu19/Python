#===========正则
import re
#p=re.match('www','www.baidu.com')
#print(type(p))#<class '_sre.SRE_Match'>
#print(p.span())#(0, 3)
#print(re.match('com','a.com'))#None
#print(re.search('com','a.com'))
#<_sre.SRE_Match object; span=(2, 5), match='com'>
########################################################################
#str='you are my girl'
#s=re.search(r'(.*) are (.*?) .*',str,re.M|re.I)
#print(s.group())#you are my girl
#print(s.group(1))#you
#print(s.group(2))#my
#print(s.groups())#('you', 'my')
#print(re.sub(r'm','','you are mmy girl',count=1))
#you are my girl
#count : 模式匹配后替换的最大次数，默认 0 表示替换所有的匹配。
########################################################################
#compile 函数用于编译正则表达式，生成一个正则表达式（ Pattern ）对象，
#供 match() 和 search() 这两个函数使用。
#re.compile(pattern[, flags])
#pattern=re.compile(r'\d+')
#m=pattern.match('sdfdggr24gytoi87')#None
#print(m)
#m = pattern.match('one12twothree34four', 3, 10)
#print(m)#<_sre.SRE_Match object; span=(3, 5), match='12'>
#print(m.group())#12
#print(m.start(0))#3
#print(m.end(0))#5
#print(pattern.findall('21jkjhj79jkhfj34343khj3'))
#['21', '79', '34343', '3']
#it = re.finditer(r"\d+","12a32bc43jf3") 
#for match in it:
#    print(match.group())
#12
#32
#43
#3
#print(re.split('a*', 'hello world'))#['hello world']   
# 对于一个找不到匹配的字符串而言，split 不会对其作出分割
#print(re.split('(\W+)', ' runoob, runoob, runoob.'))
#['', ' ', 'runoob', ', ', 'runoob', ', ', 'runoob', '.', '']











