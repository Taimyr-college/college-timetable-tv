from pdf2image import convert_from_path
from pathlib import Path
import subprocess
# "poppler" need install too

def convertDOC(badDOC):
    subprocess.call([
        'libreoffice',
        'lowriter',
        '--headless',
        '--convert-to',
        'pdf',
        '--outdir',
        '/home/nas_web_dev/zero/converting',
        badDOC])
    badDOC.unlink()

def convertPDF(badPDF, locate):
    PNG.unlink()
    images = convert_from_path(f'{badPDF}', 130)
    for i, image in enumerate(images):
        image.save(f'{locate}/{i}.png', 'PNG')


www = Path('/home', 'nas_web_dev', 'zero')
wwwPNG = Path('/home', 'nas_web_dev')

DOC = Path(www, 'converting', '1.docx')
PDF = Path(www,'converting', '1.pdf')
PNG = Path(wwwPNG, '00_today/')
png = Path(wwwPNG, '00_today/0.png')

if DOC.is_file():
    print("converting DOCX-PDF")
    convertDOC(DOC)
    print("converting PDF-PNG")
    convertPDF(PDF, PNG)
    if not png.is_file():
        print("Something wrong! Trying again...")
        convertPDF(PDF, PNG)
        PDF.unlink()
    else: PDF.unlink()
else:
    print("nothing to convert")
