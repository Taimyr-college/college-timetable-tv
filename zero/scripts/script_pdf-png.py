from pathlib import Path
from pdf2image import convert_from_path
# "poppler" need install too

def convert(badPdf, locate):
    images = convert_from_path(f'{badPdf}', 100)
    for i, image in enumerate(images):
        image.save(f'{locate}/{i}.png', 'PNG')


www = Path('..')
today = Path(www,'todayPDF','1.pdf')
tomorrow = Path(www, 'tomorrowPDF','1.pdf')
png_today = Path(www, 'web_images', 'today/')
png_tomorrow = Path(www, 'web_images', 'tomorrow/')

print(today.is_file(), tomorrow.is_file())
if today.is_file():
  print("convert today's")
  convert(today, png_today)
else:
    print("nothing to convert from today's", today)

if tomorrow.is_file():
  print("convert tomorrow's")
  convert(tomorrow, png_tomorrow)
else:
    print("nothing to convert from tomorrow's")
