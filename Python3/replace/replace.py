# coding: utf-8

# 本脚本仅支持替换文件夹名和文件名

import sys
import os

def needs_replace(root, name, oldwords, newwords):
    if oldwords in name:
        toname = name.replace(oldwords, newwords)
        return True, toname
    return False, name

def rename_file(root, name, oldwords, newwords): 
    replace, toname = needs_replace(root, name, oldwords, newwords)
    if (replace):
        path = os.path.join(root, name)
        toPath = os.path.join(root, toname)
        try:
            os.rename(path,toPath)
            print(path, '-->', toname)
        except Exception as e:
            print(e)

if __name__ == '__main__':
    args = sys.argv
    path = args[1]
    oldwords = args[2]
    newwords = args[3]
    print(path)
    dirs = os.listdir(path)
    for root, dirs, files in os.walk(path):
        for name in files:
            rename_file(root, name, oldwords, newwords)
        for name in dirs:
            rename_file(root, name, oldwords, newwords)
        
    
    