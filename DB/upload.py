import os
from ftplib import FTP

# FTP server credentials and file information
FTP_URL = 'https://famcartapi.elit-x.co'
FTP_BASE = '/'
FTP_HOST = '66.29.146.94'
FTP_USER = 'admin@famcartapi.elit-x.co'
FTP_PASSWORD = 'uAJewdm4Vy!l'
LOCAL_BASE = "../"
FILES = ['main.py', 'Resources.py']
FOLDERS = ['Controller', 'Model', 'Parsers', 'Public']

if __name__ == "__main__":
    try:

        print("CONNECTING")

        # Create an FTP connection
        ftp = FTP(FTP_HOST)

        # Login to the FTP server
        ftp.login(user=FTP_USER, passwd=FTP_PASSWORD)

        print("CONNECTED TO THE SERVER")

        # Change the working directory (if needed)
        # ftp.cwd("/remote_directory")


        def upload(path):
            # Open the local file in binary mode for uploading
            with open(LOCAL_BASE + path, "rb") as File:
                # Use the STOR command to upload the file
                ftp.storbinary("STOR " + FTP_BASE + path, File)


        print("UPLOADING FILES")
        for FILE in FILES:
            upload(FILE)

        for FOLDER in FOLDERS:
            files = os.listdir(LOCAL_BASE + FOLDER)
            print("UPLOADING FILES ON " + FOLDER)
            for file in files:
                if file.endswith(".py") or file.endswith(".php"):
                    upload(FOLDER + "/" + file)

        print("UPLOAD COMPLETED")
        # Close the FTP connection
        ftp.quit()

    except Exception as e:
        print("CONNECTION FAILED\nDUE TO\n", e)
