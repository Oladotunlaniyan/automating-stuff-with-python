# # # import pyPDF2

# # # pdfFileObj = open('meetingminutes.pdf', 'rb')

# # # pdfReader.numPages
# # # pageObj = pdfReader.getPage(0)
# # # pageObj.extractText()

# # # pdfFileObj.close()

# # import PyPDF2
# # pdfReader = PyPDF2.PdfFileReader(open('encrypted.pdf', 'rb'))
# # pdfReader.isEncrypted
# # pdfReader.getPage(0)

# # pdfReader = PyPDF2.PdfFileReader(open('encrypted.pdf', 'rb'))
# # pdfReader.decrypt('rosebud')

# # pageObj = pdfReader.getPage(0)


# # import PyPDF2

# # minutesFile = open('meetingminutes.pdf', 'rb')
# # pdfReader = PyPDF2.pdfFileReader(minutesFile)
# # page = pdfReader.getPage(0)
# # page.rotateClockwise(90)

# # pdfWriter = PyPDF2.PdfFileWriter()
# # pdfWriter.write(resultPdfFile)
# # resultPdfFile.close()
# # minutesFile.close()


# # Encrypting PDFs 

# import PyPDF2 
# pdfFile = open('meetingminutes.pdf', 'rb')
# pdfReader = PyPDF2.PdfFileReader(pdfFile)
# pdfWriter = PyPDF2.PdFileWriter()
# for pageNum in range(pdfReader.numPages):
#     pdfWriter.addPage(pdfReader.getPage(pageNum))

#     pdfWriter.encrypt('swordfish')
#     resultPdf = open('encryptedminutes.pdf', 'wb')
#     pdfWriter.write(resultPdf)
#     resultPdf.close()