import os

import pdfbox
import tabula
import PyPDF2
import textract
from tika import parser


def TabulaPDF(filePath: str, outputFolder: str):

    tabula.convert_into(filePath, outputFolder +
                        r'/exportedTabula.csv', output_format="csv", pages=3)


def TikaPDF(filePath: str, outputFolder: str):
    raw = parser.from_file(filePath)

    fileToWritePath = outputFolder + r'exportedTika.txt'
    fileToExport = open(fileToWritePath, "w")  # write mode
    fileToExport.write(raw['content'])
    fileToExport.close()


def PDFBoxPDF(filePath: str, outputFolder: str):

    p = pdfbox.PDFBox()

    p.extract_text(input_path=filePath,
                   output_path=outputFolder + r'exportedPDFBox.pdf')
    p.pdf_to_images(input_path=filePath)
    p.extract_images(input_path=filePath)


def PyPDF2PDF(filePath: str, outputFolder: str):

    pdfFileObj = open(filePath, 'rb')

    # creating a pdf reader object
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    # printing number of pages in pdf file
    print(pdfReader.numPages)

    # creating a page object
    pageObj = pdfReader.getPage(0)

    # extracting text from page
    txt = pageObj.extractText()

    # Write-Overwrites
    fileToWritePath = outputFolder + r'exportedPyPDF2PDF.pdf'
    fileToExport = open(fileToWritePath, "w")  # write mode
    fileToExport.write(txt)
    fileToExport.close()

    # closing the pdf file object
    pdfFileObj.close()

def TextractPDF (filePath: str, outputFolder: str):

    # Tesseract is an optical character recognition engine
    text = textract.process(
        filePath,
        language='pt',
    )
    text = text.decode("utf-8")

    # Write-Overwrites
    fileToWritePath = outputFolder + r'exportedTextractPDF.txt'
    fileToExport = open(fileToWritePath, "w")  # write mode
    fileToExport.write(text)
    fileToExport.close()
