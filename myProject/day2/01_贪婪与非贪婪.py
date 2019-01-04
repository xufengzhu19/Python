import re


def test1():
    html = """
    <div><p>苟利国家生死以</p></div>
    <div><p>床前明月光</p></div>
    """
    p = re.compile('<div><p>.*<p/><div/>', re.S)
    r = p.findall(html)
    print(r)


# 分组
def test2():
    s = "A B C D"
    p1 = re.compile('\w+\s+\w+')
    print(p1.findall(s))

    p2 = re.compile('(\w+)\s+\w+')
    print(p2.findall(s))

    p3 = re.compile('(\w+)\s+(\w+)')
    print(p3.findall(s))


def test3():
    html = '''
    <div class="animal">
        <p class="name">
            <a title="Tiger"></a>
        </p>
        <p class="content">
            tiger white rabbit white and white
        </p>
    </div>
    <div class="animal">
        <p class="name">
            <a title="Rabbit"></a>
        </p>
        <p class="content">
            Small white rabbit white and white
        </p>
    </div>    
    '''
    rList = []
    res_div = r'<div class="animal">(.*?)</div>'
    m_div = re.findall(res_div, html, re.S | re.M)
    for div in m_div:
        # print(div)
        res_p = r'<p class="name">(.*?)</p>'
        m_p = re.findall(res_p, div, re.S | re.M)
        for p in m_p:
            # print(p)
            res_a = r'<a title="(.*?)"></a>'
            m_a = re.findall(res_a, p, re.S | re.M)
            for a in m_a:
                rList.append(a)
    return rList


if __name__ == '__main__':
    # test1()
    # test2()
    rList = test3()
    print(rList)
    for r in rList:
        print("动物名称：%s" % r[0].strip())
        print("动物描述：%s" % r[1].strip())
        print("*" * 30)
