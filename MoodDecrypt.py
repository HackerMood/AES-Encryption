'''
    Auteur : Hacker Mood
    github : https://github.com/HackerMood
    {AES Images Encryption}
'''


from asyncio import sleep
import base64
from fileinput import filename
import os
from cryptography.fernet import Fernet
import pyAesCrypt
from os import stat, remove
from PIL import Image
from io import BytesIO


#Define Key for encryption
bufferSize = 64 * 1024
password = "************" #key for decrypt


def fileDec(pthsgen):
    
    # Detect file extension
    filename, file_extension = os.path.splitext(pthsgen)
    d, s = os.path.splitext(filename)
   
    encFileSize = stat(pthsgen).st_size
    # opening the original file to encrypt and write
    with open(pthsgen, "rb") as fIn:
        try:
            with open(filename + ".txt", "wb") as fOut:
                # decrypt file stream
                pyAesCrypt.decryptStream(fIn, fOut, password, bufferSize, encFileSize)
        except ValueError:
            # remove output file on error
            remove(filename + ".txt")
    
    # Delete old the file
    os.remove(pthsgen)

    #read txt file (base64)
    with open(filename + '.txt', 'r') as f:
        data = f.read()

    #convert (base 64 to image)
    im = Image.open(BytesIO(base64.b64decode(data)))
    im.save(filename, "PNG")

    #delete file with {.txt --> extension} after decryption 
    os.remove(filename + '.txt')

def acces(dir_path):
    

    # list to store files
    res = []

    # Iterate directory
    for path in os.listdir(dir_path):
        # check if current path is a file
        if os.path.isfile(os.path.join(dir_path, path)):
            #res.append(path)
            fileDec(dir_path +'/'+ path)


dir_path = '********************' #Decryt Directory
#choice user to select
print("Select Action please : {1 -> Local File } {2 -> USB OR Any Directory}")
choice = int(input("\n -- > "))

if(choice == 1):
    #Decrypt image in {tes}    
    acces(dir_path)
    
elif(choice == 2):
    #DecryptUSB file {you ne to specify usb path}
    dir_path = input("Enter USB {letter path} : ")
    acces(dir_path)

