import qrcode as qrc

bs = input("Enter the box-size: ")
br = input("Enter the border: ")
data = input("Enter the data off the qrcode: ")
save_name = input("Enter the save name off the qrcode: ")



qr = qrc.QRCode(
    version=1,
    box_size=bs,
    border=br,
)

qr.add_data(data)
qr.make(fit=True)

img = qr.make_image()
img.save(save_name)