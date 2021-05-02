# encoding:utf-8

import os
import time
import sys

def main(localDir):
    bookNames = []
    bookDirs = []
    allFiles = os.listdir(localDir)
    for fileName in allFiles:
        if os.path.isdir(os.path.join(localDir, fileName)) and fileName != 'PDF':
            bookNames.append(fileName)
    for bookName in bookNames:
        subDir = os.listdir(os.path.join(localDir, bookName))
        allDir = os.path.join(localDir, bookName, subDir[0])
        if (os.path.isdir(os.path.join(localDir, bookName, subDir[0])) and len(subDir) == 1):
            bookDirs.append(os.path.join(localDir, bookName, subDir[0]))
        else:
            bookDirs.append(os.path.join(localDir, bookName))
    print('In ' + localDir)
    print('Found ' + str(len(bookNames)) + ' book(s):')
    for bookName in bookNames:
        print('  ' + bookName)
    if not os.path.exists(os.path.join(localDir,'PDF')):
        os.system('mkdir ' + os.path.join(localDir,'PDF'))
    for bookName,bookDir in zip(bookNames,bookDirs):
        startTime = time.time()
        print('Converting : ' + bookName + '...')
        inputCmd = 'convert.exe "' + bookDir + '\\*.{png,jpeg,jpg}" -quality 100 "' + localDir + '\\PDF\\' + bookName + '.pdf"'
        os.system(inputCmd)
        endTime = time.time()
        print('  Completed. Converted %d file(s) in %d second(s).' % (len(os.listdir(bookDir)) , (endTime - startTime)))
        
if __name__ == '__main__':
    if len(sys.argv) == 1:
        main('.')
    elif len(sys.argv) == 2:
        main(sys.argv[1])