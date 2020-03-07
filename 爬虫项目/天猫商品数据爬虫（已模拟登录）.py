from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from pyquery import PyQuery as pq
from time import sleep


class taobao_infos:
    def __init__(self):
        url = "https://login.taobao.com/member/login.jhtml"
        self.url = url

        options = webdriver.ChromeOptions()
        options.add_experimental_option(
            "prefs", {"profile.managed_default_content_setting.images": 2})
        options.add_experimental_option(
            "excludeSwitches", ["enable-automation"])

        self.broswer = webdriver.Chrome(
            executable_path=chromedriver_path, options=options)
        self.wait = WebDriverWait(self.broswer, 10)

    def sleep_and_alter(self, sec, message, is_alert):

        for second in range(sec):
            if(is_alert):
                alert = "alert(\"" + message + ":" + str(sec - second) + "秒\")"
                self.broswer.execute_script(alert)
                al = self.broswer.switch_to.alert
                sleep(1)
                al.accept()
            else:
                sleep(1)

    def login(self):
        self.broswer.get(self.url)

        self.broswer.implicitly_wait(30)
        self.broswer.find_element_by_xpath(
            '//*[@class="forget-pwd J_Quick2Static"]').click()

        self.broswer.implicitly_wait(30)
        self.broswer.find_element_by_xpath('//*[@class="weibo-login"]').click()

        self.broswer.implicitly_wait(30)
        self.broswer.find_element_by_name('username').send_keys(weibo_username)

        self.broswer.implicitly_wait(30)
        self.broswer.find_element_by_name('password').send_keys(weibo_password)

        self.broswer.implicitly_wait(30)
        self.broswer.find_element_by_xpath(
            '//*[@class="btn_tip"]/a/span').click()

        taobao_name = self.wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, '.site-nav-bd > ul.site-nav-bd-l'
                 ' > li#J_SiteNavLogin > div.site-nav-menu-hd'
                 ' > div.site-nav-user > a.site-nav-login-info-nick ')))
        print(taobao_name.text)

    def search_toal_page(self):
        good_total = self.wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, '#J_ItemList '
                 '> div.product'
                 ' > div.product-iWrap')))

        number_total = self.wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, '.ui-page '
                 '> div.ui-page-wrap'
                 ' > b.ui-page-skip > form')))
        page_total = number_total.text.replace(
            "共",
            "").replace(
            "页，到第页 确定",
            "").replace(
            "， ",
            "")

        return page_total

    def next_page(self, page_number):
        input = self.wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR,
                 '.ui-page > div.ui-page-wrap'
                 ' > b.ui-page-skip > form'
                 ' > input.ui-page-skipTo')))

        submit = self.wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR,
                 '.ui-page > div.ui-page-wrap'
                 ' > b.ui-page-skip'
                 ' > form > button.ui-btn-s')))
        input.clear()
        input.send_keys(page_number)
        sleep(1)
        submit.click()

    def swipe_down(self, second):
        for i in range(int(second / 0.1)):
            js = "var q=document.documentElement.scrollTop=" + \
                str(300 + 200 * i)
            self.broswer.execute_script(js)
            sleep(0.1)
        js = "var q=document.documentElement.scrollTop=100000"
        self.broswer.execute_script(js)
        sleep(0.2)

    def crawwl_good_data(self):
        self.broswer.get("https://list.tmall.com/search_product.htm?q=羽毛球")
        err1 = self.broswer.find_element_by_xpath(
            "//*[@id='content']/div/div[2]").text
        err1 = err1[:5]
        if(err1 == "喵~没找到"):
            print("找不到您想要的")
            return
        try:
            self.broswer.find_element_by_xpath("//*[@id='J_ComboRec']/div[1]")
            err2 = self.broswer.find_element_by_xpath(
                "//*[@id='J_ComboRec']/div[1]").text

            err2 = err2[:5]

            if(err2 == "我们还为您"):
                print("您要查询的商品书目太少了")
                return
        except BaseException:
            print("可以爬取这些信息")

        page_total = self.search_toal_page()
        print("总共页数" + page_total)

        for page in range(2, int(page_total)):
            good_total = self.wait.until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, '#J_ItemList '
                     '> div.product '
                     '> div.product-iWrap')))
            input = self.wait.until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR,
                     '.ui-page > div.ui-page-wrap'
                     ' > b.ui-page-skip'
                     ' > form > input.ui-page-skipTo')))
            now_page = input.get_attribute('value')
            print("当前页数" + now_page + ",总共页数" + page_total)

            html = self.broswer.page_source

            doc = pq(html)

            good_items = doc('#J_ItemList .product').items()

            for item in good_items:
                good_title = item.find('.productTitle').text().replace(
                    '\n', "").replace('\r', "")
                good_status = item.find('.productStatus').text().replace(
                    " ",
                    "").replace(
                    "笔",
                    "").replace(
                    '\n',
                    "").replace(
                    '\r',
                    "")
                good_price = item.find('.productPrice').text().replace(
                    "¥",
                    "").replace(
                    " ",
                    "").replace(
                    '\n',
                    "").replace(
                    '\r',
                    "")
                good_url = item.find('.productImg').attr('href')
                print(
                    good_title +
                    "   " +
                    good_status +
                    "   " +
                    good_price +
                    "   " +
                    good_url +
                    '\n')

            self.swipe_down(2)

            self.next_page(page)

            WebDriverWait(
                self.broswer, 5, 0.5).until(
                EC.presence_of_element_located(
                    (By.ID, "nc_1_n1z")))  # 等待滑动拖动控件出现
            try:
                swipe_button = self.broswer.find_element_by_id(
                    'nc_1_n1z')  # 获取滑动拖动控件

                # 模拟拽托
                action = ActionChains(self.broswer)  # 实例化一个action对象
                # perform()用来执行ActionChains中存储的行为
                action.click_and_hold(swipe_button).perform()
                action.reset_actions()
                action.move_by_offset(580, 0).perform()  # 移动滑块

            except Exception as e:
                print('get button failed: ', e)


if __name__ == "__main__":

    chromedriver_path = "C:/Users/tangyun/Desktop/chromedriver.exe"
    weibo_username = "18205175303"
    weibo_password = "tyaunng5277"

    a = taobao_infos()
    a.login()
    a.crawwl_good_data()
