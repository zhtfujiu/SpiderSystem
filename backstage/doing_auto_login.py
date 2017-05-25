# coding=UTF-8

import time
from doing_mysql import Doing_mysql

class Doing_Auto_login(object):
    def __init__(self, driver):
        self.driver = driver

    def login(self):

        login_url = 'https://passport.baidu.com/v2/?login'

        try:
            while True:

                self.driver.get(login_url)  # 把访问链接放在这，免得输入错误后

                username_blank = self.driver.find_element_by_id("TANGRAM__PSP_3__userName")
                psw_blank = self.driver.find_element_by_id("TANGRAM__PSP_3__password")
                login_btn = self.driver.find_element_by_id("TANGRAM__PSP_3__submit")

                username = raw_input('请输入您的百度账号：\n')
                psw = raw_input('请输入您的百度账号密码：\n')

                # username = '伏久飞天'
                # psw = '5556zht'

                username_blank.clear()
                psw_blank.clear()

                username_blank.send_keys(unicode(username, 'utf-8'))  # 编码问题，这里需要加上unicode
                # UnicodeDecodeError: 'utf8' codec can't decode byte 0xe4 in position 0: unexpected end of data
                time.sleep(2)
                psw_blank.send_keys(psw)
                time.sleep(2)

                login_btn.click()
                time.sleep(2)
                # ***************************************
                # 登录之后延迟一秒，检测当前页面是否仍然是登录url，如果是，则登录失败
                # ***************************************
                if self.driver.current_url == login_url:
                    # 登录失败
                    print '登录失败，请核对账户或密码！'
                else:
                    # 登录成功，转到下一个所需页面
                    print username, '登录成功！'
                    self.username = username

                    break
        except Exception, e:
            print '登录过程发生错误：', e

    def get_user_baike_info(self):
        try:
            # 转到个人百科页面
            self.driver.get('https://baike.baidu.com/usercenter')
            time.sleep(2)
            # 创建个人数据表，以username为table名称来
            doing_mysql = Doing_mysql()
            doing_mysql.do_create_info_table(self.username)
            # 摘取个人信息
            user_pic_url = self.driver.find_element_by_xpath(
                '/html/body/div[2]/div[1]/div/div[1]/div[1]/img').get_attribute('src')  # 头像图片链接
            user_level = self.driver.find_element_by_xpath(
                '/html/body/div[2]/div[1]/div/div[1]/div[4]/i[1]').text  # 用户百科等级
            tongguo = self.driver.find_element_by_xpath(
                '/html/body/div[2]/div[1]/div/div[2]/ul/li[1]/a/dl/dd').text  # 通过的词条数目
            youzhi = self.driver.find_element_by_xpath(
                '/html/body/div[2]/div[1]/div/div[2]/ul/li[2]/a/dl/dd').text  # 优质词条数目
            tese = self.driver.find_element_by_xpath(
                '/html/body/div[2]/div[1]/div/div[2]/ul/li[3]/a/dl/dd').text  # 特色词条数目
            tijiao = self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[2]/ul/li[4]/i').text  # 提交的词条数目
            tongguolv = self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[2]/ul/li[6]/i').text  # 通过率
            chuangjian = self.driver.find_element_by_xpath(
                '/html/body/div[2]/div[1]/div/div[2]/ul/li[8]/i').text  # 创建版本
            caifuzhi = self.driver.find_element_by_xpath(
                '/html/body/div[2]/div[1]/div/div[2]/div/div/label/i').text  # 财富值

            # 将信息写入数据库
            doing_mysql.do_add_userinfo(self.username, user_pic_url, user_level, tongguo, youzhi, tese, tijiao,
                                        tongguolv, chuangjian, caifuzhi)
            print self.username,'用户的个人信息已保存至baike数据库的',self.username,'表中。'
            # 关闭数据库
            doing_mysql.do_end_sql()
        except Exception, e:
            print '获取并存储个人信息时发生错误：', e

