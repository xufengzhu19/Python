import time
from selenium import webdriver

address = 'http://www.baidu.com/'


def test():
    driver = webdriver.Chrome()
    driver.get(address)
    print(driver.page_source)
    driver.save_screenshot('百度.png')
    driver.quit()


def test1():
    driver = webdriver.Chrome()
    driver.get(address)
    key = input("请输入要搜索的内容：")
    driver.find_element_by_id('kw').send_keys(key)
    time.sleep(10)
    driver.find_element_by_id('su').click()
    time.sleep(1)
    driver.save_screenshot('美女.png')
    driver.quit()


def QuiShi():
    driver = webdriver.PhantomJS()
    driver.get('http://qiushibaike.com/text/')
    # rOne = driver.find_element_by_class_name('content')
    # print(rOne.text)
    rList = driver.find_element_by_class_name('content')
    print(rList)


def RenRen():
    # 用户名：email，密码：password，验证码：icode，登录(id)：login
    # driver=webdriver.PhantomJS()
    opt = webdriver.ChromeOptions()
    opt.set_headless()
    opt.add_argument('windows-size=1920*5000')
    driver = webdriver.Chrome(options=opt)

    # driver=webdriver.Chrome()
    driver.get('http://www.renren.com/')
    driver.maximize_window()
    driver.save_screenshot('yzm.png')
    uname = driver.find_element_by_name('email')
    uname.send_keys('18633615542')
    pwd = driver.find_element_by_name('password')
    pwd.send_keys('zhanshen001')
    driver.save_screenshot('yzm.png')
    yzm = input("请输入验证码：")
    driver.find_element_by_name('icode').send_keys(yzm)
    driver.find_element_by_id('login').click()
    time.sleep(10)
    driver.save_screenshot('成功.png')
    driver.quit()


def JD():
    # 目标：名称，价格，评论数量，商家名称
    driver = webdriver.Chrome()
    driver.get('https://www.jd.com/')
    key = input('请输入要搜索的内容：')
    content=driver.find_element_by_class_name('text')
    content.send_keys(key)
    button=driver.find_element_by_class_name('button')
    button.click()

    while True:
        driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        time.sleep(2)
        rList = driver.find_elements_by_xpath('//div[@id="J_goodsList"]//li')
        # print(rList)
        for r in rList:
            contentList = r.text.split('\n')
            price = contentList[0]
            name = contentList[1]
            commit = contentList[2]
            market = contentList[3]

            d = {
                "价格": price,
                "名称": name,
                "评论": commit,
                "商家": market,
            }
            with open("jd.json", "a", encoding="utf-8") as f:
                f.write(str(d) + '\n')

        if driver.page_source.find('pn-next disabled')==-1:
            driver.find_element_by_class_name('pn-next').click()
            time.sleep(1)
        else:
            print("爬虫结束")
            break



if __name__ == '__main__':
    # test();
    # test1()
    # QuiShi()
    # RenRen()
    JD()