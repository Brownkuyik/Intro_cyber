#code to lock pdf files.

from PyPDF2 import PdfFileWriter, PdfFileReader
import getpass
file_write = PdfFileWriter()

#path to the pdf file you want to lock
pad = PdfFileReader("C:/Users/kuyik/Documents/400L¹ Past-Questions.pdf")

#for each page lock

for page_number in range(pad.numPages):
    file_write.addPage(pad.getPage(page_number))

password = getpass.getpass(prompt='Enter you password: ')
file_write.encrypt(password)
with open("C:/Users/kuyik/Documents/400L¹ Past-Questions.pdf", 'wb') as file:
    file_write.write(file)
print('Your pdf file is now protected')