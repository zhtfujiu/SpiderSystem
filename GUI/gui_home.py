# coding=UTF-8
import wx
from gui_login import GUI_LOGIN
from gui_spider import GUI_SPIDER
from gui_data import GUI_DATA


import py2app

class GUI_HOME(wx.Frame):
    def __init__(self, parent):
        super(GUI_HOME, self).__init__(parent, title="百度百科爬虫及数据分析系统", size=(500, 300))
        self.parent = parent
        self.InitUI()
        self.Centre()
        self.Show()

    def InitUI(self):
        panel = wx.Panel(self)

        # 最外层盒子，垂直方向
        self.boxsizer = wx.BoxSizer(wx.VERTICAL)

        # 第三个内层盒子，水平包含3个勾选框
        hbox3 = wx.BoxSizer(wx.VERTICAL)

        btn1 = wx.Button(panel, label='登录并爬取个人百科信息')
        hbox3.Add(btn1, proportion=1, flag=wx.EXPAND)
        btn2 = wx.Button(panel, label='设定根词条并爬取')
        hbox3.Add(btn2, proportion=1, flag=wx.EXPAND)
        btn3 = wx.Button(panel, label='数据分析系统')
        hbox3.Add(btn3, proportion=1, flag=wx.EXPAND)

        # 最外层盒子添加内层3号盒子，靠左对齐，边距10
        self.boxsizer.Add(hbox3, proportion=1, flag=wx.ALIGN_CENTER, border=10)
        # 下边距25
        self.boxsizer.Add((-1, 10))


        btn1.Bind(wx.EVT_LEFT_DOWN, self.login)  # 登录转到登录界面
        btn2.Bind(wx.EVT_LEFT_DOWN, self.spider)  # 爬虫
        btn3.Bind(wx.EVT_LEFT_DOWN, self.data)  # 数据分析

        panel.SetSizer(self.boxsizer)
        panel.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBack)  # 背景图片


    def OnEraseBack(self, event):
        dc = event.GetDC()
        if not dc:
            dc = wx.ClientDC(self)
            rect = self.GetUpdateRegion().GetBox()
            dc.SetClippingRect(rect)
        dc.Clear()
        bmp = wx.Bitmap("spider.jpg")
        dc.DrawBitmap(bmp, 0, 0)

    def login(self, event):
        self.Hide()
        GUI_LOGIN(self).Show()
        event.Skip()

    def spider(self, event):
        self.Hide()
        GUI_SPIDER(self).Show()
        event.Skip()

    def data(self, event):
        self.Hide()
        GUI_DATA(self).Show()
        event.Skip()


    def change(self, event):
        self.Hide()
        self.example.Show()
        event.Skip()

if __name__ == '__main__':
    app = wx.App()
    GUI_HOME(None)
    app.MainLoop()
