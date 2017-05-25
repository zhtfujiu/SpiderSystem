# coding=UTF-8
import wx

class MianWindow(wx.Frame):

    def __init__(self, parent, title):
        wx.Frame.__init__(parent=parent, title=title,size=(600,400))
        p = wx.Panel(self)
        img = wx.Image('xiaoyi_1.jpeg', wx.BITMAP_TYPE_ANY)
        box = wx.BoxSizer(wx.VERTICAL)
        box.Add(img, wx.EXPAND)
        p.SetSizer(box)

if __name__=='__main__':
    a = wx.App(False)
    MianWindow(None, title='Pic')
    a.MainLoop()

