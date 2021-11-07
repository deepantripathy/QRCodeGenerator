# QRCodeGenerator
QR Code generation based on input from website

The basic idea of this little project came from a problem I faced when I had to pass along the password to wifi at my place to a group of friends.
So I created this basic website where you can pass any text; url, passwords, even a simple Hello and it will generate a QR code which can be sent over via wahatsapp.
Step 1: Load up website
Step 2: Enter text and click on generate
onClick function will initiate execution of python file (script.py). The python code will take the input text, send over for conversion to QR code which is saved as send_qr.jpg. This QR is then sent over via whatsapp.
