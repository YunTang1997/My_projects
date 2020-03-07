from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class taobao_infos:
    def __init__(self):
        url = "https://login.taobao.com/member/login.jhtml"
        self.url = url

        options = webdriver.ChromeOptions()
        options.add_experimental_option(
            "prefs", {"profile.managed_default_content_setting.images": 2})
        options.add_experimental_option(
            "excludeSwitches", ["enable-automation"])

        self.browser = webdriver.Chrome(
            executable_path=chromedriver_path, options=options)
        self.wait = WebDriverWait(self.browser, 10)

    def login(self):
        self.browser.get(self.url)

        password_login = self.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, ".qrcode-login > .login-links > .forget-pwd")))
        password_login.click()

        weibo_login = self.wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, ".weibo-login")))
        weibo_login.click()

        weibo_user = self.wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, ".username > .W_input")))
        weibo_user.send_keys(weibo_username)

        weibo_pwd = self.wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, ".password > .W_input")))
        weibo_pwd.send_keys(weibo_password)

        submit = self.wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, ".btn_tip > a > span")))
        submit.click()

        taobao_name = self.wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR,
                 ".site-nav-bd > ul.site-nav-bd-l > li#J_SiteNavLogin "
                 "> div.site-nav-menu-hd > div.site-nav-user > a.site-nav-login-info-nick ")))
        print(taobao_name.text)


if __name__ == "__main__":

    chromedriver_path = "C:/Users/tangyun/Desktop/chromedriver.exe"
    weibo_username = "18205175303"
    weibo_password = "tyaunng5277"

    a = taobao_infos()
    a.login()
