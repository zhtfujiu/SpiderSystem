# coding=UTF-8
import os

from selenium import webdriver

from doing_auto_login import Doing_Auto_login
from doing_database import Doing_Database
from doing_spider import Doing_Spider

print '=====Python爬虫系统及数据分析系统（以百度百科为例）=====\n' \
      '\n' \
      '功能List：\n' \
      '1、登录个人账号查询个人百科账号信息\n' \
      '2、自定词条并爬取若干条与其相关词条、URL和摘要信息\n' \
      '3、对已爬取数据进行筛选、提取、导出等操作\n' \
      '4、退出系统\n' \
      '\n' \
      '===================================================' \

# 启动Webdriver
driver = webdriver.Chrome()

while True:
    order = raw_input('\n========请输入要执行的功能序号：=========\n').strip()  # 去除前后空格
    if not order.isdigit():
        # 非法数据，重新输入
        print '*****请输入合法序号！*****'
        continue
    order = int(order)
    if order == 1:
        # 执行登录功能
        # 实例化Auto_login_baidu类
        auto_login = Doing_Auto_login(driver)
        auto_login.login()
        # 后续爬取个人信息未完成
        auto_login.get_user_baike_info()


    elif order == 2:
        # 执行查询词条操作
        spider = Doing_Spider()
        spider.crawl(driver)

    elif order == 3:
        # 执行数据分析功能
        doing_database = Doing_Database()
        doing_database.do_database()
        pass
    elif order == 4:
        # 系统退出，浏览器退出
        driver.quit()
        print '\nBye~'
        os._exit(0)
    else:
        # 非法数据，重新输入
        print '*****请输入合法序号！*****'
        continue