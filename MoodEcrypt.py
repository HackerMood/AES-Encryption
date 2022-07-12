'''
    Auteur : Hacker Mood
    github : https://github.com/raytano

    {AES Images Encryption}
'''

import base64
from fileinput import filename
import os
import pyAesCrypt
from os import stat, remove

def convert(file):
    
    files = file

    #Convert image to txt (base64)
    with open(file, "rb") as image2string:
        converted_string = base64.b64encode(image2string.read())
    print(converted_string)

    #detection file extension   
    filename, file_extension = os.path.splitext(file)

    #generate text in file {filename = name of the file + ext{txt}}
    with open(filename + '.txt', "wb") as file:
        file.write(converted_string)
        
    #remove existent file 
    os.remove(files)

    #calling function fileEnc to encrypt file
    fileEnc(filename + '.txt', file_extension)


#define key for encryption 
bufferSize = 64 * 1024
password = "***************" #any string size you want


def fileEnc(pthsgen , extens):
    
    # Detect file extension
    filename, file_extension = os.path.splitext(pthsgen)
    
    # opening the original file to encrypt and write
    with open(pthsgen, "rb") as fIn:
        with open(filename + extens + '.aes', "wb") as fOut:
            pyAesCrypt.encryptStream(fIn, fOut, password, bufferSize)
    
    #get size of output file
    encFileSize = stat(filename + extens + '.aes').st_size
    
    # Delete old the file
    os.remove(pthsgen)


def acces(dir_path):
    

    # list to store files
    res = []

    # Iterate directory
    for path in os.listdir(dir_path):
        # check if current path is a file
        if os.path.isfile(os.path.join(dir_path, path)):
            #res.append(path)
            convert(dir_path +'/'+ path)


dir_path = '********************' #directory for test  but you can put any directory you want

#choice user to select
print("Select Action please : {1 -> Local File } {2 -> USB OR Any Directory}")
choice = int(input("\n -- > "))

if(choice == 1):
    #encrypt image in {tes}
    acces(dir_path)
    
elif(choice == 2):
    #encrypt USB file {you ne to specify usb path}
    dir_path = input("Enter USB {letter path} : ")
    acces(dir_path)

