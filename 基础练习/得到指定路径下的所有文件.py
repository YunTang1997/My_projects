# coding = utf-8

"""
Author: YunTang
version: 0.1
date: 2020/3/30
desc: 得到指定路径下的所有文件名
"""

import os
import sys


all_files = []
def find_all_files(address):
    files = os.listdir(address)  # 得到指定路径下的所有文件名，包括隐藏文件
    for f in files:
        path = os.path.join(address, f)
        if os.path.isdir(path):  # 判断path是否是一个存在的目录（文件夹）
            find_all_files(path)
        all_files.append(f)
    return all_files


if __name__ == '__main__':
    # os.chdir("D:/software/pycharm/PycharmProjects/project/基础练习")  # 更改当前路径
    print(find_all_files(os.getcwd()))
