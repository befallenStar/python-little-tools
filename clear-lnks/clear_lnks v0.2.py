# -*- encoding: utf-8 -*-
import os
import sys
import win32com.client


def main():
    shell = win32com.client.Dispatch("WScript.Shell")
    for disk in ['C:\\','D:\\','E:\\']:
        for root, dirs, files in os.walk(disk):
            if '$Recycle.Bin' in root:
                continue
            for file in files:
                if '.lnk' in file:
                    shortcut=shell.CreateShortCut(os.path.join(root,file))
                    if not os.path.exists(shortcut.Targetpath):
                        # print(shortcut.Targetpath)
                        print(os.path.join(root,file))
                        # print(os.path.exists(shortcut.Targetpath))
                        # os.remove(os.path.join(root,file))

        # shortcut = shell.CreateShortCut("./Steam.lnk")
        # print(shortcut.Targetpath)
        # print(os.path.exists(shortcut.Targetpath))
        # if not os.path.exists(shortcut.Targetpath):
        #     os.remove("./Steam.lnk")



if __name__ == '__main__':
    main()