import qrcode, os, sys, pywhatkit
from flask import Flask, render_template, request, url_for, redirect
import pywhatkit as pyt

def create_qr(qrStr):
    qr = qrcode.QRCode()
    qr.add_data(qrStr)
    qr.make()
    img = qr.make_image()
    file_name = sys.path[0] + "\send_qr.jpg"
    img.save(file_name)

def sendWhatsapp():
    file_name = sys.path[0]+"\send_qr.jpg"
    pyt.sendwhats_image(
        phone_no="+918800533698",
        img_path= file_name
    )

app = Flask(__name__)

@app.route("/home", methods=["GET","POST"])
def home():        
    if request.method == "POST":
        qrText = request.form["sendText"]
        if request.form['btnGenerate'] == "Generate":
            #if qrText: 
            create_qr(qrText)
            print("QR Generated")
            return render_template("index.html")
        print("QR Code generated")
        sendWhatsapp()
    return render_template("index.html")

if __name__ == "__main__":
    app.run()
