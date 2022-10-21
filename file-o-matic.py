#!/usr/bin/env python3
import pycurl
import argparse
import json
import os
from io import BytesIO

def main():
    os.system('tput setaf 0')
    print("""
        
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣶⡿⠿⠿⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⡛⡛⠛⠻⠿⠿⠿⠿⠿⠿⠿⢶⣶⣶⣶⣶⣤⣤⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⡿⠛⠁⠀⠀⠀⠀⠀⣀⣠⠴⠒⠛⠉⠉⣁⣀⣀⣀⣈⣉⡉⠁⠀⠀⠒⠒⠒⠒⠒⠒⠚⠛⠛⠛⠛⠻⠿⣶⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⠟⠀⠀⠀⠀⠀⣠⡴⠛⢉⣠⠴⠖⠛⣉⣉⣀⣀⣀⣀⣀⠀⠉⠉⠛⠒⠒⠒⠒⠒⠒⠒⠛⠛⠋⠉⠉⠙⠢⠀⠉⠻⢿⣦⣀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⠋⠀⠀⠀⣠⠴⠋⢁⡴⠊⣡⠴⠒⠉⠉⠀⠀⠀⠀⠀⠙⢦⠀⠀⠀⠀⠀⠀⠀⠠⠶⠒⠒⠒⠉⠉⠓⠲⣤⡀⠀⠀⠀⠀⠙⢿⣦⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⣰⣿⠃⠀⠀⠀⠈⠁⢀⡼⢋⡴⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡇⠀⠀⠀⠀⠀⠀⠀⣸⠃⠀⠀⠀⠀⠀⠀⠀⠹⡄⠀⠀⠀⠀⠸⣿⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⢀⣴⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⣠⣴⣶⣿⣿⣿⣿⡿⠿⣿⣶⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠃⠀⠀⣀⣀⣀⣀⣀⡀⠀⠁⠀⠀⠀⠀⠀⢿⣧⡀⠀⠀⠀
            ⠀⠀⠀⢀⣴⣿⣿⣷⣒⡂⠀⠀⠀⠀⣤⣤⡖⢠⣾⣟⣭⣿⣿⣿⣿⣿⣧⣤⣀⠉⠻⣿⣦⡀⠀⠀⠀⠀⠀⣀⣠⣶⣿⣿⣿⣿⣿⣿⣿⣷⠀⠤⣤⣤⣤⣤⡈⠻⣿⣦⡀⠀
            ⠀⠀⣴⣿⢫⠟⠁⢀⣠⣴⣶⣶⣶⣦⣄⡀⠞⠀⠉⠉⠉⠁⢀⣰⣶⠈⠉⠙⠻⢿⣶⣿⠟⠁⠀⠀⠀⠘⠿⣿⣿⡿⠟⠛⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⢦⣙⠲⣌⠻⣿⡀
            ⠀⣾⡟⢡⠏⠀⣠⣿⠟⠉⠁⢰⡎⠙⠛⠿⢷⣶⣤⣤⣴⣶⡿⠛⠁⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⣀⣀⠀⢀⣤⣶⡶⠶⣶⣦⡈⡇⠈⢧⣿⡇
            ⠘⣿⠁⢸⠀⢀⣿⠃⠀⠀⢀⣾⣿⣦⣄⡀⠀⠈⠉⠉⠉⠀⠀⠀⠀⠀⠀⢀⡀⠀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠘⢿⣷⣄⡀⠀⠀⠙⠿⠿⠿⠿⠁⣴⠀⠈⠉⠁⢹⠀⢸⣿⡇
            ⠀⣿⡀⢸⡀⠘⣿⡀⢶⣾⣿⣿⡉⠉⠛⢿⣷⣦⣄⡀⠀⠀⠠⠤⠴⠒⠒⠚⢱⣿⠟⠛⠃⠀⠀⠀⠀⠀⠀⠀⠀⠉⣿⣿⣦⡀⠀⠀⠀⠀⠀⢠⣿⣧⠀⠀⣴⠏⢀⣯⣿⠇
            ⠀⢿⣧⠀⢧⠀⢻⣧⠀⠀⠀⣿⣷⣄⠀⠀⠈⠙⣿⡿⢿⣶⣦⣤⣀⡀⠀⠀⠸⣿⡄⢸⡿⠿⠿⠗⠀⠀⠀⠀⢀⣴⣿⠟⠛⠉⠓⠦⣄⠀⢀⣾⣿⣿⡇⢀⡥⠖⢋⣾⡟⠀
            ⠀⠈⢻⣷⣌⠛⠶⣄⠀⠀⠀⠘⢿⣿⣿⣶⣤⡀⣿⣧⡀⠀⠉⠙⠛⠿⢿⣷⣶⣬⣇⣀⡀⠀⠀⠀⠀⠘⠿⣾⡿⠟⠁⠀⠀⠀⢀⣀⣤⣾⣿⢿⣷⣿⣧⠀⠀⢀⣾⡟⠀⠀
            ⠀⠀⠀⠙⢿⣿⡒⠀⠀⠀⠀⠀⠈⢻⣷⡉⠛⠿⣿⣿⣿⣦⣤⣀⠀⠀⠀⣿⡏⠉⠛⠛⠻⠿⣿⣷⣶⣶⣶⣶⣶⣶⣶⣶⡶⢾⣿⣿⠋⠉⣿⡀⢻⣿⣿⠀⠀⢸⣿⠀⠀⠀
            ⠀⠀⠀⠀⠀⠹⣿⣆⠀⠀⠀⠀⠀⠀⠙⣿⣆⠀⣿⡟⠛⠿⢿⣿⣿⣷⣾⣿⣄⣀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⢻⣏⠀⠀⠀⠀⢹⣿⠀⣠⣿⣷⣾⣿⣿⠀⠀⢸⣿⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠘⣿⣆⠀⠀⠀⠀⠀⠀⠈⠻⣷⣿⠃⠀⠀⠀⠈⠉⢻⣿⡿⣿⣿⣿⣿⣷⣶⣾⣿⣷⣶⣶⣶⣿⣿⣷⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⢸⣿⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠘⣿⣦⡀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣦⣀⠀⠀⠀⣸⣿⠃⠀⠉⠉⠛⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⢸⣿⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠙⠿⣷⣦⣠⣿⠏⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠈⢹⣿⠟⠉⠉⣻⡿⠋⢩⣿⠏⣸⣿⣼⡿⠀⠀⠀⢸⣿⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣷⣦⡙⠳⢤⣈⠑⠢⢄⣀⠈⠙⠛⠿⣷⣶⣤⣤⣀⣀⣀⣸⣷⠀⠀⠀⠀⣸⡿⠀⠀⣰⣿⣃⣀⣿⣯⣤⣶⡿⠋⠀⠀⠀⠀⢸⣿⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⢿⣷⣤⣈⠛⠶⢤⣈⠛⠢⢤⣀⠀⠀⠉⠙⠛⠛⠛⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠟⠛⠛⠋⠉⠀⠀⡀⠀⠀⠀⠀⢸⣿⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠻⢷⣦⣤⣈⠙⠒⠦⢌⣉⠓⠲⠤⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡴⠋⠀⠀⢠⡇⠀⢸⣿⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠻⢿⣶⣤⣀⠈⠉⠑⠒⠲⠭⠭⣍⣉⣒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠋⠁⠀⠀⣠⡴⠋⠀⠀⠀⣿⡆⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠻⢿⣶⣤⣀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠓⠒⠒⠒⠒⠒⠒⠒⠒⠒⠋⠁⠀⠀⠀⠀⣼⣿⠁⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠻⠿⣷⣶⣤⣤⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⡿⠁⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠙⠛⠻⠿⢿⣷⣦⣤⣤⣀⣀⣀⣀⣀⣀⣀⣀⣀⣤⣶⡿⠟⠋⠀⠀⠀⠀⠀
    """)


    os.system("tput setaf 3")
    print("""
            ⠀⠀⠀⠀⠀⠀⠀⠀An automated wide range file uploader written in python3.

    """)



def fileChecker(filename):
    try:
        print("[+] Checking file if available...\n")
        
        # Opening the file in read-only mode
        # If the file can be opened, it means the file is found
        # else it will raise an exception/error
        file = open(filename,'r')
        result = filename if (file) else 'Error: Cannot read/open file'
        # It's necessary to close the file after using it or opening it
        file.close()
        print('File found: %s\n' % result)
        return result # Putting this to last section so the file.close() method is not throwing unreachable
    except FileNotFoundError:
        print('ERROR: FILE NOT FOUND.')
        print('Try checking if you enter the correct directory or filename...\n')
        exit()
    except IsADirectoryError:
        print('ERROR: CURRENT SELECTION IS A DIRECTORY')
        print('Compress it to .zip, .7z or .rar and then try again...\n')
        exit()


def successUploadChecker(data):
    os.system("tput setaf 2")
    url = data['data']['file']['url']['short']
    size = data['data']['file']['metadata']['size']['readable']
    return "Uploaded: " + url + " size: " + size



def errorUploadChecker(data):
    os.system("tput setaf 1")
    type = data['error']['type']
    message = data['error']['message']
    return type + ":" + message



def upload(file_to_upload):
    main()
    os.system("tput setaf 8")
    filename = fileChecker(file_to_upload)
    
    try:
        
        print("Starting upload...")
        
        # Lists of file hostings available to upload
        apis = ["https://api.anonfiles.com/upload","https://api.letsupload.cc/upload","https://api.megaupload.nz/upload","https://api.myfile.is/upload","https://api.share-online.is/upload","https://api.vshare.is/upload","https://api.hotfile.io/upload","https://api.rapidshare.nu/upload","https://api.lolabits.se/upload","https://api.upvid.cc/upload","https://api.filechan.org/upload"]
        
        for api in apis:
            
            buffer = BytesIO() # Creating buffer for cURL
            
            # Creating cURL instance
            c = pycurl.Curl()
            
            c.setopt(c.URL, api) # Setting up options for cURL instance
            c.setopt(c.HTTPPOST, [("file", (c.FORM_FILE, filename))])
            c.setopt(c.WRITEDATA, buffer)
            c.perform() # perform file transfer
            c.close() # Close the session of cURL instance
            
            # Parse the response
            data = json.loads(buffer.getvalue())
            
            #Checking the status of file upload
            status = data['status']
            if status:
                print(successUploadChecker(data))
            else:
                print(errorUploadChecker(data))
                
    except pycurl.error:
        print("There's an error uploading file to the server %s" % filename)



os.system("tput setaf 8")
parser = argparse.ArgumentParser(prog='file-o-matic.py' ,usage='python3 %(prog)s --file path/to/<filename>')
parser.add_argument('--file',help='path/to/filename.ext to upload')
args = parser.parse_args()

if args.file:
    upload(args.file)


if not any(vars(args).values()):
    print("Usage: python3 file-o-matic.py --file path/to/<filename>")