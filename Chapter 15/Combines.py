# import PyPDF2
# import os

# pdfFiles = []

# # Gather all PDF files in the current directory
# for filename in os.listdir('.'):
#     if filename.endswith('.pdf'):
#         pdfFiles.append(filename)

# # Sort the list of files alphabetically (case-insensitive)
# pdfFiles.sort(key=str.lower)

# # Create a PDF writer object
# pdfWriter = PyPDF2.PdfFileWriter()

# # Loop through all the PDF files
# for filename in pdfFiles:
#     pdfFileObj = open(filename, 'rb')
#     pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

#     # Add all pages except the first one from each file
#     for pageNum in range(1, pdfReader.numPages):
#         pageObj = pdfReader.getPage(pageNum)
#         pdfWriter.addPage(pageObj)

#     pdfFileObj.close()  # Close the file after reading

# # Write the collected pages to a new PDF
# with open('allminutes.pdf', 'wb') as pdfOutput:
#     pdfWriter.write(pdfOutput)
