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

## Using `segno` package ##
You can also generate QR codes using the `segno` package. Here's a simple example:

```python
import segno
# Create a QR code
qr = segno.make('https://wwww.biomodels.org')
# Save the QR code as a PNG file
qr.save('qrcode.png')
```
Check out the [complete tutorial](https://realpython.com/python-generate-qr-code/).