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
config_data = []
for i in data["outputFolders"]:
    directory.append(i['directory'])
    extension.append(i['extension'])
    config_data = dict(zip(extension, directory))


class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for file_name in os.listdir(data["trackingFolder"]):
            file_source = data["trackingFolder"] + "/" + file_name
            split_tup = os.path.splitext(file_name)
            file_extension = split_tup[1]
            for config_data_ext, config_data_path in config_data.items():
                if file_extension == config_data_ext:
                    new_destination = config_data_path + "/" + file_name
                    os.rename(file_source, new_destination)
                    print(f'\033[4m{datetime.now().strftime("%H:%M:%S")}\033[0m - [{file_extension.upper()}] \033[95m{file_name}\033[0m was moved to \033[92m{config_data_path}\033[0m')
                else:
                    pass


print(f'STARTING \n')
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, data["trackingFolder"], recursive=True)

user_choice = True
while user_choice:
    observer.start()
    user_input = input('Press any to exit \n')
    if user_input:
        print('\x1B[3mstopping\x1B[0m')
        exit()
    else:
        pass
