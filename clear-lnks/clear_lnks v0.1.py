# -*- encoding: utf-8 -*-
import os
import sys
import win32com.client


def main():
    shell = win32com.client.Dispatch("WScript.Shell")
    shortcut = shell.CreateShortCut("./Steam.lnk")
    print(shortcut.Targetpath)
    print(os.path.exists(shortcut.Targetpath))
    if not os.path.exists(shortcut.Targetpath):
        os.remove("./Steam.lnk")



if __name__ == '__main__':
    main()