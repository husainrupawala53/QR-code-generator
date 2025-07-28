import qrcode
website_link=input("enter your website link")
qr=qrcode.QRCode(version=1,box_size=5,border=5)
qr.add_data(website_link)
qr.make()
img=qr.make_image(fill_color="black",back_color="white")
qr_code_name=input("enter the name for your qr code")
img.save(f"{qr_code_name}.png")