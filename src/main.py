import os

from pdfmethod import *

# Change by the correct URL to get the medical files
PROJECT_DIR = FILE = os.getcwd()

FILE_PATH = PROJECT_DIR + r'/input/QualisNovo.pdf'
OUTPUT_FOLDER = PROJECT_DIR + r'/output/'

TabulaPDF(FILE_PATH, OUTPUT_FOLDER)

TikaPDF(FILE_PATH, OUTPUT_FOLDER)

PDFBoxPDF(FILE_PATH, OUTPUT_FOLDER)

TextractPDF(FILE_PATH, OUTPUT_FOLDER)