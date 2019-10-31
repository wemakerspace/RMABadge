from reportlab.graphics.shapes import Drawing, String
from reportlab.graphics import renderPM

from brother_ql.devicedependent import label_type_specs
from brother_ql import BrotherQLRaster, create_label
from brother_ql.backends.helpers import send

PRINTER = 'usb://0x04f9:0x20a7'
LABEL_NAME = '62'
DPI_600 = True

def printLabel(name):
   width = 500
   height = 100

   d = Drawing(width, height)
   d.add(String(5, 5, name, fontSize=40, fontName='Helvetica'))
   #d.add(String(5, 5, name, fontSize=60, fontName='Helvetica'))

   qlr = BrotherQLRaster('QL-1050')
   #qlr = BrotherQLRaster('QL-800')
   create_label(qlr, renderPM.drawToPIL(d), LABEL_NAME, rotate=90, cut=True, dpi_600=DPI_600)
   send(qlr.data, PRINTER)
