# coding=UTF-8
import wx


class Example(wx.Frame):
    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, size=(500, 300))
        self.InitUI()
        self.Centre()
        # self.Show()

    def InitUI(self):
        panel = wx.Panel(self)

        # 最外层盒子，垂直方向
        boxsizer = wx.BoxSizer(wx.VERTICAL)

        # 内层第一个盒子，水平方向，存储根词条和输入框
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        statictext_1 = wx.StaticText(panel, label='根词条')
        # 内层盒子1，布局设计根词条位置
        hbox1.Add(statictext_1, flag=wx.RIGHT, border=8)  # 提示词‘根词条’，Right右边距是border

        # 输入框
        textctrl1 = wx.TextCtrl(panel)
        hbox1.Add(textctrl1, proportion=1)  # proportion比例1，证明是填充完剩余空间

        # 最外层盒子添加内层盒子1
        boxsizer.Add(hbox1, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)  # 左右上下边距都是10 EXPAND意思是使用所有分配给他的空间
        boxsizer.Add((-1, 10))  # 10是下边距，不知道-1是什么


        # 内层盒子2
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        # 创建大输入框
        # tc2 = wx.TextCtrl(panel, style=wx.TE_MULTILINE)

        img = wx.Image('xiaoyi_1.jpeg', wx.BITMAP_TYPE_ANY)
        staticbitmap = wx.StaticBitmap(panel, -1, wx.BitmapFromImage(img))

        # 内层盒子2添加输入框，扩展占据全部
        hbox2.Add(staticbitmap, proportion=1, flag=wx.EXPAND)

        # 最外层盒子添加内层2号盒子，扩展占据全部
        boxsizer.Add(hbox2, proportion=1, flag=wx.LEFT | wx.RIGHT | wx.EXPAND,
                 border=10)
        # 下边距25
        boxsizer.Add((-1, 25))

        # 第三个内层盒子，水平包含3个勾选框
        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        # 创建3个勾选框对象
        cb1 = wx.CheckBox(panel, label='Case Sensitive')
        hbox3.Add(cb1)
        cb2 = wx.CheckBox(panel, label='Nested Classes')
        hbox3.Add(cb2, flag=wx.LEFT, border=10)  # 与左边的勾选框距离10
        cb3 = wx.CheckBox(panel, label='Non-Project classes')
        hbox3.Add(cb3, flag=wx.LEFT, border=10)

        # 最外层盒子添加内层3号盒子，靠左对齐，边距10
        boxsizer.Add(hbox3, flag=wx.LEFT, border=10)
        # 下边距25
        boxsizer.Add((-1, 25))

        # 创建内层4号盒子，内含两个按钮，水平放置
        hbox4 = wx.BoxSizer(wx.HORIZONTAL)
        # 按钮大小，名称设置
        btn1 = wx.Button(panel, label='OK', size=(70, 30))
        hbox4.Add(btn1)
        btn2 = wx.Button(panel, label='Close', size=(70, 30))
        hbox4.Add(btn2, flag=wx.LEFT | wx.BOTTOM, border=5)  # 按钮距离左侧和底部都是5

        # 最外层盒子添加内层4号盒子，盒子右对齐，靠在外层盒子的右侧，边距10
        boxsizer.Add(hbox4, flag=wx.ALIGN_RIGHT | wx.RIGHT, border=10)

        # 面板设置Sizer
        panel.SetSizer(boxsizer)


# if __name__ == '__main__':
#     app = wx.App()
#     Example(None, title="百度百科爬虫及数据分析系统")
#     app.MainLoop()