<div align="center">
  <h1>QR Code Generator</h1>
</div>

<div align="justify">

   This Python code allows you to generate a QR code for a given URL address (or any other text).

   *How the code works:* the user enters a URL (or any other text) for which a QR code needs to be generated. **QRCodeGenerator** generates a QR code using the [*qrcode*](https://github.com/lincolnloop/python-qrcode) *library* and sets color of the background and color of the QR code. **QRCodeModifier** changes the size and color of the background and the color of the QR code according to the selected parameters. **QRCodeSaver** saves the QR code in the selected format.

   *Code usage:* the program can be used to generate QR codes for any links or texts that can be used both in web applications and placed on various printed and digital media, advertising banners, electronic documents, etc.

</div>

<br>

<div align="center">

   # Settings

   To use it, you need to complete the following steps:

<br>

#### 📁 Clone this repository

   ```
      git clone https://github.com/lazycatcoder/qrcode-generator.git
   ```


#### 📦 Install dependencies
   
   ```
   pip install -r requirements.txt
   ```

<br>

## ✨How to use
___

<div align="left">

1. Import all required classes from the `qr_module` module

```
   from qr_module import QRCodeGenerator, QRCodeModifier, QRCodeSaver
``` 
2. Pass the URL (text) for which you want to generate a QR code or enter it manually

```
   url = 'https://www.example.com' 

   # url = str(input('Enter URL (or any other text): '))
``` 
3. Create an instance of the **QRCodeGenerator** class with the given URL

```
   qr_gen = QRCodeGenerator(url)
```

4. Create an instance of the **QRCodeModifier** class with modified QR code parameters

```
   qr_mod = QRCodeModifier(qr_gen.get_qrcode(), size='large', color='#FFFF01', bg_color='#4a4a4a')
```

5. Change the QR code

```
   modified_qr = qr_mod.modify_qrcode()
```

6. Create an instance of the **QRCodeSaver** class and save the QR code

```
   qr_saver = QRCodeSaver(modified_qr, save_path='qrcodes', format='bmp') 
   qr_saver.save_qrcode()
```

<br>

❗*also, you can run the ready-made `test.py` file to check the functionality of the code*

</div>

<br>

   ## 📝Parameters and values
___

<div align="left">

The code consists of three classes:
   - **QRCodeGenerator** - generates a QR code for the given URL address or text
   - **QRCodeModifier** - changes the QR code parameters: size, color, background
   - **QRCodeSaver** - saves the QR code in the selected format
<br>

<div align="center">

   ###  *Description of parameters and values:*

</div>

**QRCodeGenerator** class:
   - url (type: string) - URL address (or any other text) to generate QR code

**QRCodeModifier** class:
   - *qr_code* (type: PIL.Image.Image) - QR code image
   - *size* (type: string) - size of the QR code. Valid values are 'small', 'middle' and 'large'. Default is 'middle'
   - *color* (type: string) - QR code color in RGB format. Valid values: Any color specified in RGB format (#RRGGBB). Default is '#000000'
   - *bg_color* (type: string) - QR code background color in RGB format. Valid values: Any color specified in RGB format (#RRGGBB). Default is '#FFFFFF'

**QRCodeSaver** class:
   - *qr_code* (type: PIL.Image.Image) - QR code image
   - *save_path* (type: string) - path to save the QR code. If the specified path does not exist, it will be created. Default - 'qrcodes'
   - *format* (type: string) - file format to save. Valid values: 'bmp', 'jpeg', 'png', 'gif', 'webp'. Default - 'png'

</div>
