import sys
import PyPDF2

input = sys.argv[1:]

def pdf_merger(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write('merged.pdf')

pdf_merger(input)