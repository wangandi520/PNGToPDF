import os

def main():
    bookNames = []
    allFiles = os.listdir('.')
    for fileName in allFiles:
        if os.path.isdir(fileName):
            bookNames.append(fileName)
    bookDir = []
    bookPNGs = []
    for eachBookName in bookNames:
        PNGNames = os.listdir(eachBookName)
        bookPNGs.append(PNGNames)
    
    cmds = []
    for i in range(0, len(bookNames)):
        tmp = 'mutool.exe convert -o PDF\\' + bookNames[i] + '.pdf '
        for j in range(0, len(bookPNGs[i])):
            #print(bookPNGs[i][j])
            tmp = tmp + str(bookNames[i]) + '\\' + str(bookPNGs[i][j] + ' ')
        cmds.append(tmp)
    
    os.system('mkdir PDF')
    for cmd in cmds:
        os.system(cmd)
    
if __name__ == '__main__':
    main()