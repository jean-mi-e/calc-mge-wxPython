#!/usr/bin/env python3
# coding: utf-8

import frame.interface as itf
import wx


def main():
    app = wx.App()
    frame = itf.Interface(parent=None, id=-1)

    frame.Show()
    app.MainLoop()

if __name__ == "__main__":
    main()
