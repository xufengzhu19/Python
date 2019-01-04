from bs4 import BeautifulSoup

def test():
    html='''
    <div class="test">雄霸</div>
    <div class="test">聂风</div>
    <div class="test2">
        <span>步惊云</span>
    </div>
    '''
    soup=BeautifulSoup(html,'lxml')
    rList=soup.find_all('div',{'class':'test2'})
    # print(rList)

    for r in rList:
        print(r.get_text())
        print(r.span.string)

if __name__ == '__main__':
    test()