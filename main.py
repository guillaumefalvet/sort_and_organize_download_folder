from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import os
import time
from datetime import datetime

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class MyHandler(FileSystemEventHandler):
    i = 1

    def on_modified(self, event):
        for file_name in os.listdir(folder_to_track):
            src = folder_to_track + "/" + file_name
            # getting the file extensions
            split_tup = os.path.splitext(file_name)
            file_extension = split_tup[1]

            if file_extension == ".jpg" or file_extension == ".jpeg" or file_extension == ".gif" or file_extension == ".png":
                file_location = folder_img
                new_destination = file_location + "/" + file_name
                os.rename(src, new_destination)
                log_file(file_extension, file_name, file_location)

            elif file_extension == ".psd":
                file_location = folder_psd
                new_destination = file_location + "/" + file_name
                os.rename(src, new_destination)
                log_file(file_extension, file_name, file_location)

            elif file_extension == ".pdf":
                file_location = folder_pdf
                new_destination = file_location + "/" + file_name
                os.rename(src, new_destination)
                log_file(file_extension, file_name, file_location)

            elif file_extension == ".zip" or file_extension == ".gz" or file_extension == ".tgz":
                file_location = folder_zip
                new_destination = file_location + "/" + file_name
                os.rename(src, new_destination)
                log_file(file_extension, file_name, file_location)

            elif file_extension == ".ipa":
                file_location = folder_ipa
                new_destination = file_location + "/" + file_name
                os.rename(src, new_destination)
                log_file(file_extension, file_name, file_location)

            elif file_extension == ".dmg":
                file_location = folder_dmg
                new_destination = file_location + "/" + file_name
                os.rename(src, new_destination)
                log_file(file_extension, file_name, file_location)

            else:
                pass


def log_file(file_extension, file_name, file_location):
    print(f'{bcolors.UNDERLINE}{dt_string}{bcolors.ENDC} - [{file_extension.upper()}] {bcolors.HEADER}{file_name}{bcolors.ENDC} was moved to {bcolors.OKGREEN}{file_location}{bcolors.ENDC}')


now = datetime.now()
dt_string = now.strftime("%H:%M:%S")

folder_to_track = "/Users/guillaumefalvet/Downloads"
folder_img = "/Users/guillaumefalvet/Pictures"
folder_psd = "/Users/guillaumefalvet/Downlaods/Folder_PSD"
folder_pdf = "/Users/guillaumefalvet/Downloads/Folder_PDF"
folder_zip = "/Users/guillaumefalvet/Downloads/Folder_ZIP"
folder_ipa = "/Users/guillaumefalvet/Downloads/Folder_IPA"
folder_dmg = "/Users/guillaumefalvet/Downloads/Folder_DMG"
print('start')
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()
try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()
