import sys
import PyPDF2

actual_filename = sys.argv[1]
watermark_filename = sys.argv[2]
output_filename = sys.argv[3]
print(actual_filename, watermark_filename, output_filename)
template = PyPDF2.PdfFileReader(open(actual_filename, 'rb'))
watermark = PyPDF2.PdfFileReader(open(watermark_filename, 'rb'))
output = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
    page = template.getPage(i)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)
    with open(output_filename, 'wb') as file:
        output.write(file)
