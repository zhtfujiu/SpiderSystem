# coding=UTF-8

import wx, time

class MainWindow(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(600, 400))
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)

        # 创建位于窗口底部的状态栏
        self.CreateStatusBar()

        # 设置菜单
        filemenu1 = wx.Menu()
        filemenu2 = wx.Menu()

        # wx.ID_ABOUT和wx.ID_EXIT是wxWidgets提供的标准ID
        item1 = filemenu1.Append(wx.ID_ABOUT, '关于', '关于程序的信息')
        # filemenu1.AppendSeparator()
        item2 = filemenu1.Append(wx.ID_EXIT, '退出', '终止应用程序')
        # filemenu1.AppendSeparator()

        '''
        添加绑定事件
        '''
        self.Bind(wx.EVT_MENU, self.Method, item2)

        filemenu2.Append(wx.ID_EXIT, '退出', '终止应用程序')
        # 创建菜单栏
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu1, '文件')
        menuBar.Append(filemenu2, '登录')
        self.SetMenuBar(menuBar)

        self.Show(True)

    def Method(self, event):
        # self.control.AppendText('李筱奕')
        # time.sleep(1)
        # self.control.AppendText('赵昊天')
        # time.sleep(1)
        self.Close(True)
        # self.Destroy()

app = wx.App(False)  # 创建1个APP，禁用stdout/stderr重定向
frame = MainWindow(None, 'Editor')
app.MainLoop()