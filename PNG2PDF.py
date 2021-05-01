import os

def main():
    bookNames = []
    bookDirs = []
    allFiles = os.listdir('.')
    for fileName in allFiles:
        if os.path.isdir(fileName) and fileName != 'PDF':
            bookNames.append(fileName)
    for bookName in bookNames:
        if (os.path.isdir(bookName) and len(os.listdir(bookName)) == 1):
            bookDirs.append(bookName + '\\' + os.listdir(bookName)[0])
        else:
            bookDirs.append(bookName)
    print('Found ' + str(len(bookNames)) + ' books:')
    for bookName in bookNames:
        print('  ' + bookName)
    if not os.path.exists('PDF'):
        os.system('mkdir PDF')
    for bookName,bookDir in zip(bookNames,bookDirs):
        #print(bookDir)
        print('Converting PNG to PDF: ' + bookName + '...')
        os.system('convert "' + bookDir + '\\*.{png,jpeg,jpg}" -quality 100 PDF\\' + bookName + '.pdf')
        print('  Completed.')
        
if __name__ == '__main__':
    main()