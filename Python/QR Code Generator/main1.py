import qrcode
from PIL import Image

qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=4)
link=input("Enter Link or Text : ")
fileName = input("Enter File Name : ")

inpu = input("Your want to customise your QR Code : ")
inp = inpu.lower()
if(inp == 'y' or inp == 'yes'):
    QRColor = input("Enter Color For QR Code : ")
    bgColor = input("Enter Background Color for your QR Code : ")
elif (inp == 'n' or inp =='no'):
    QRColor = 'black'
    bgColor = 'white'
else:
    print("Sorry!, We can't understand your answer so we use default settings...")
    QRColor = 'black'
    bgColor = 'white'

qr.add_data(f"{link}")
qr.make(fit=True)
img = qr.make_image(fill_color=QRColor, back_color=bgColor)
img.save(f"{fileName}.png")