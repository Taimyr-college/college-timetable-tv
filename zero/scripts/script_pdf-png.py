from pathlib import Path
import subprocess
from pdf2image import convert_from_path
# "poppler" need install too

def convertDOC(badDOC,locate):
    subprocess.call([
        'libreoffice',
        'lowriter',
        '--headless',
        '--convert-to',
        'pdf',
        '--outdir',
        '/home/nas_web_dev/zero/todayPDF',
        badDOC
    ])

def convertPDF(badPdf, locate):
    print(badPdf, locate)
    images = convert_from_path(f'{badPdf}', 100)
    for i, image in enumerate(images):
        image.save(f'{locate}/{i}.png', 'PNG')


www = Path('/home', 'nas_web_dev', 'zero')
wwwPNG = Path('/home', 'nas_web_dev')

todayDOC = Path(www, 'timeToday', '1.docx')
tomorrowDOC = Path(www, 'timeTomorrow', '1.docx')

todayPDF = Path(www,'todayPDF', '1.pdf')
tomorrowPDF = Path(www, 'tomorrowPDF','1.pdf')

todayPNG = Path(wwwPNG, '00_today/')
tomorrowPNG = Path(wwwPNG, '00_tomorrow/')

print(todayDOC.is_file(), todayDOC)

if todayDOC.is_file():
  print("convert today's DOCX")
  convertDOC(todayDOC, todayPDF)
  convertPDF(todayPDF, todayPNG)
else:
    print("nothing to convert from today's")

if tomorrowDOC.is_file():
  print("convert tomorrow's")
  convertPDF(tomorrowDOC, tomorrowPNG)
else:
    print("nothing to convert from tomorrow's")

