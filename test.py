from qr_module import QRCodeGenerator, QRCodeModifier, QRCodeSaver

# URL for which the QR code will be generated
url = 'https://www.example.com' 
# url = str(input('Enter URL (or any other text): '))

# Create an instance of the QRCodeGenerator class with the given URL
qr_gen = QRCodeGenerator(url)
# Create an instance of the QRCodeModifier class with modified QR code parameters
qr_mod = QRCodeModifier(qr_gen.get_qrcode(), size='large', color='#FFFF01', bg_color='#4a4a4a')
# Change the QR code
modified_qr = qr_mod.modify_qrcode()

# Create an instance of the QRCodeSaver class and save the QR code
qr_saver = QRCodeSaver(modified_qr, save_path='qrcodes', format='bmp') 
qr_saver.save_qrcode()

print("Your QR code has been successfully saved!")






# An example without using the QRCodeModifier class

# from qr_module import QRCodeGenerator, QRCodeSaver
# url = 'https://www.example.com' 
# qr_gen = QRCodeGenerator(url)
# qr_saver = QRCodeSaver(qr_gen.get_qrcode(), save_path='qrcodes', format='bmp') 
# qr_saver.save_qrcode()
# print("Your QR code has been successfully saved!")