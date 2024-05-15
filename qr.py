import qrcode

image = qrcode.make("https://127.0.0.1:8000")  # Web app URL
image.save("qr.png")
