# coding=UTF-8
# 对百度百科Python词条及其1000个相关页面的词条及摘要数据进行爬取
# 爬虫入口
import html_outputer, url_manager, html_downloader, html_parser
import wx

class Doing_Spider(object):

    def __init__(self, driver, entry, num, status_text):
        self.entry = entry
        self.num = num
        self.driver = driver
        self.status_text = status_text

        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.outputer = html_outputer.HtmlOutputer()
        self.parser = html_parser.HtmlParser()

    def crawl(self):
        driver = self.driver
        while True:
            driver.get('https://baike.baidu.com/')
            entry = self.entry
            # 锁定页面的输入框，将用户词条输入
            driver.find_element_by_id("query").send_keys(entry)  # 注意汉语编码
            # 搜索   这里需要加一个对搜索结果的检测，该词条是否存在!!!!!!
            driver.find_element_by_id("search").click()
            # 搜索不到词条的话，都是下面这中url，后期匹配一下
            # http://baike.baidu.com/search/none?word=wowowow&pn=0&rn=10&enc=utf8
            if 'item' in driver.current_url and 'search/none' not in driver.current_url:
                # 搜索有结果,进行下一步爬取工作

                num = self.num

                print entry, num

                num = int(num)  #转变为int整型
                count = 1  # 变量count记录当前爬取的是第几个URL

                self.urls.add_new_url(driver.current_url)  # 添加根URL

                while self.urls.has_new_url():  # 爬虫的循环
                    # 异常处理，避免无效URL带来的崩溃
                    try:
                        new_url = self.urls.get_new_url()  # 获取一个待爬取的URL，添加进URL管理器
                        # now_text =  '正在爬取第'+count+'条: '+ new_url
                        print new_url
                        # 把现在的信息添加在展示栏
                        # self.status_text.AppendText(now_text)

                        html_content = self.downloader.download(new_url)  # 启动下载器，存储进html_content里
                        new_urls, new_data = self.parser.parse(new_url, html_content)  # 解析器对该URL的内容进行解析，分离出新的URL和数据
                        self.urls.add_new_urls(new_urls)  # 批量添加URL，跟上面那个add_new_url不一样，那个是单独添加一条
                        self.outputer.collect_data(new_data)  # 对数据进行收集

                        # 自定爬取数目
                        if count == num:
                            print num, '条数据已爬取完成'
                            break
                        count = count + 1
                    except:
                        print '本条爬取失败'


                # try:
                self.outputer.output_mysql()
                print '数据已存储至数据库'
                # except Exception, e:
                #     print '存储过程错误：', e

                break
            else:
                print '您输入的词条不存在，请重新输入'
