# How to generate QR codes
## Using `pyqrcode` package ##
You can generate QR codes in Python using the `pyqrcode` package. You also need to install the `pypng` and `pillow` if preferring the PNG format and opening after the generation. Here's a simple example:

```python
import pyqrcode
# Create a QR code
qr = pyqrcode.create('https://wwww.biomodels.org')
# Save the QR code as a PNG file
qr.png('qrcode.png', scale=6)
```
Check the sample code [generate-qrcode.py](/demo/generate-qrcode.py) for the complete demonstration.