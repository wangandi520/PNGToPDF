import os

def main():
    bookNames = []
    allFiles = os.listdir('.')
    for fileName in allFiles:
        if os.path.splitext(fileName)[1] == '.pdf':
            bookNames.append(fileName)
            
    os.system('mkdir PNG')
    for bookName in bookNames:
        os.system('mkdir PNG\\' + os.path.splitext(bookName)[0])
        os.system('mutool.exe convert -o PNG\\' + os.path.splitext(bookName)[0] + '\\Image%d.png ' + bookName)
    
if __name__ == '__main__':
    main()