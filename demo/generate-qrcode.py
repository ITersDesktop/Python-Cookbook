import pyqrcode
from PIL import Image

link = input("Enter the link to generate QR code: ")
qr_code = pyqrcode.create(link)

# Save as SVG (scalable vector graphic, we don't need to install pypng for this format)
qr_code.svg("qrcode.svg", scale=8)

# To save as PNG, uncomment the following lines (and ensure pypng is installed):
# qr_code.png("qrcode.png", scale=8)
# img = Image.open("qrcode.png")
# img.show()
# print("QR code generated and saved as qrcode.png")
