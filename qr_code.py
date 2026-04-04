import qrcode

url = input("Enter your URL :").strip()
name = input("Enter the QR name :")
file_path = f"D:\\qrcode\\{name}.png"

qr = qrcode.QRCode()
qr.add_data(url)

img = qr.make_image()
img.save(file_path)
print("QRCode Generated Successfully..")
print("Check D:\\qrcode\\ location")