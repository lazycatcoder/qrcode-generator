import qrcode
import os
import os.path
from datetime import date


# QRCodeGenerator class constructor
# QR code generation
class QRCodeGenerator:
    def __init__(self, url):
        # Initialize QR code with qrcode.QRCode
        self.qr = qrcode.QRCode(version=None, box_size=10, border=4)
        self.qr.add_data(url)
        self.qr.make(fit=True)

        # Get the image of the QR code with make_image, set the background and text colors
        self.qr_image = self.qr.make_image(fill_color="black", back_color="white")

        # Add link information to additional image data
        self.qr_image.info['url'] = url
    
    def get_qrcode(self):
        return self.qr_image


# QRCodeModifier class constructor
# QR code modification
class QRCodeModifier:
    def __init__(self, qr_code, size='middle', color='#000000', bg_color='#FFFFFF'):
        self.qr_code = qr_code
        self.size = size
        self.color = color
        self.bg_color = bg_color
    
    def modify_qrcode(self):
        # Set the dimensions of the QR code in pixels depending on the selected size
        sizes = {
            'small': 400,
            'middle': 800,
            'large': 1200
        }

        if self.size not in sizes:
            self.size = 'middle'
        qr_size = sizes[self.size]

        # Scale the image to the desired size
        img = self.qr_code.resize((qr_size, qr_size))

        # Convert image to RGB and get pixels
        img = img.convert('RGB')
        pixels = img.load()

        # Replace the background and text colors in the QR code with the specified ones
        for i in range(img.size[0]):
            for j in range(img.size[1]):
                if pixels[i,j] == (0, 0, 0):
                    pixels[i,j] = tuple(int(self.color.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))
                elif pixels[i,j] == (255, 255, 255):
                    pixels[i,j] = tuple(int(self.bg_color.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))

        return img


# QRCodeSaver class constructor
# Save QR code to file
class QRCodeSaver:
    # Allowed file extensions to save
    ALLOWED_EXTENSIONS = ['bmp', 'jpeg', 'png', 'gif', 'webp']

    def __init__(self, qr_code, save_path='qrcodes', format=None):
        self.qr_code = qr_code
        self.save_path = save_path

        # If no format is specified, save as PNG by default
        self.format = format.lower() if format else 'png'

    def save_qrcode(self):
        # Create a save directory if it doesn't exist
        if not os.path.exists(self.save_path):
            os.makedirs(self.save_path)

        # Formation of the file name. Getting information about the link from the additional data of the QR code
        url = self.qr_code.info['url']
        domain = url.split('//')[-1].split('/')[0].replace('.', '_')
        today = date.today().strftime('%d-%m-%Y')
        index = ''
        
        while True:
            file_name = f'{domain}_{today}{index}.{self.format}'
            file_path = os.path.join(self.save_path, file_name)

            # If the file exists, add an index to the name
            if os.path.exists(file_path):
                if index == '':
                    index = '_01'
                else:
                    index = f'_{int(index[1:])+1:02d}'
            else:
                break

        # Check for a supported file format
        if self.format not in self.ALLOWED_EXTENSIONS:
            raise ValueError(f'Unsupported file format: {self.format}')
        
        # Save the file
        self.qr_code.save(file_path)
        return file_path