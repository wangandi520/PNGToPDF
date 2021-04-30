import os

def main():
    bookNames = []
    allFiles = os.listdir('.')
    for fileName in allFiles:
        if os.path.isdir(fileName) and fileName != 'PDF':
            bookNames.append(fileName)
    if not os.path.exists('PDF'):
        os.system('mkdir PDF')
    for bookName in bookNames:
        print('Converting PNG to PDF: ' + bookName)
        os.system('convert "' + bookName + '\\*.{png,jpeg,jpg}" -quality 100 PDF\\' + bookName + '.pdf')
        
if __name__ == '__main__':
    main()