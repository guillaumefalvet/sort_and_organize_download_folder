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

def log_file(file_extension, file_name, file_location):
    hour_and_minute = datetime.now().strftime("%H:%M:%S")
    print(f'{bcolors.UNDERLINE}{hour_and_minute}{bcolors.ENDC} - [{file_extension.upper()}] {bcolors.HEADER}{file_name}{bcolors.ENDC} was moved to {bcolors.OKGREEN}{file_location}{bcolors.ENDC}')


def file_transfer(file_location, file_name, file_extension, file_source):
    new_destination = file_location + "/" + file_name
    os.rename(file_source, new_destination)
    log_file(file_extension, file_name, file_location)


class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for file_name in os.listdir(folder_to_track):
            file_source = folder_to_track + "/" + file_name
            # getting the file extensions
            split_tup = os.path.splitext(file_name)
            file_extension = split_tup[1]
            # statement for each selected extensions
            if file_extension == ".jpg" or file_extension == ".jpeg" or file_extension == ".gif" or file_extension == ".png":
                file_location = folder_img
                file_transfer(file_location, file_name, file_extension, file_source)

            elif file_extension == ".psd":
                file_location = folder_psd
                file_transfer(file_location, file_name, file_extension, file_source)

            elif file_extension == ".pdf":
                file_location = folder_pdf
                file_transfer(file_location, file_name, file_extension, file_source)

            elif file_extension == ".zip" or file_extension == ".gz" or file_extension == ".tgz":
                file_location = folder_zip
                file_transfer(file_location, file_name, file_extension, file_source)

            elif file_extension == ".ipa":
                file_location = folder_ipa
                file_transfer(file_location, file_name, file_extension, file_source)

            elif file_extension == ".dmg":
                file_location = folder_dmg
                file_transfer(file_location, file_name, file_extension, file_source)

            else:
                pass

# Directory for each folder
folder_to_track = "/Users/guillaumefalvet/Downloads"
folder_img = "/Users/guillaumefalvet/Pictures"
folder_psd = "/Users/guillaumefalvet/Downlaods/Folder_PSD"
folder_pdf = "/Users/guillaumefalvet/Downloads/Folder_PDF"
folder_zip = "/Users/guillaumefalvet/Downloads/Folder_ZIP"
folder_ipa = "/Users/guillaumefalvet/Downloads/Folder_IPA"
folder_dmg = "/Users/guillaumefalvet/Downloads/Folder_DMG"


print(f'{bcolors.OKCYAN}STARTING{bcolors.ENDC} \n')
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)

user_choice = True
while user_choice:
    observer.start()
    user_input = int(input('Press 1 to exit \n'))
    if user_input == 1:
        print('\x1B[3mstopping\x1B[0m')
        exit()
    else:
        pass

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()