from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import time
from datetime import datetime
import json

with open('data.json', 'r') as data_file:
    data = json.load(data_file)
directory = []
extension = []
for i in data.values():
    directory.append(i['directory'])
    extension.append(i['extension'])
    config_data = dict(zip(directory, extension))


class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for file_name in os.listdir(folder_to_track):
            file_source = folder_to_track + "/" + file_name
            # getting the file extensions
            split_tup = os.path.splitext(file_name)
            file_extension = split_tup[1]
            # statement for each selected extensions
            for a, b in config_data.items():
                if file_extension == b:
                    new_destination = a + "/" + file_name
                    os.rename(file_source, new_destination)
                    print(f'\033[4m{datetime.now().strftime("%H:%M:%S")}\033[0m - [{file_extension.upper()}] \033[95m{file_name}\033[0m was moved to \033[92m{a}\033[0m')
                else:
                    pass


folder_to_track = "/Users/guillaumefalvet/Downloads"


print(f'STARTING \n')
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