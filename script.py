# Made by pressfguillaume
# Created because I have an OCD when it comes to messy folders

import tkinter as tk
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
from datetime import datetime
from subprocess import call
import json
import pync


with open('data.json', 'r') as data_file:
    data = json.load(data_file)
directory = []
extension = []
color = []
config_color = []
config_data = []
for i in data["outputFolders"]:
    directory.append(i['directory'])
    extension.append(i['extension'])
    color.append(i['color'])
    config_data = dict(zip(extension, directory))
for i in data["outputFolders"]:
    extension.append(i['extension'])
    color.append(i['color'])
    config_color = dict(zip(extension, color))


def notification_of_file_movement(title, file_name, path):
    pync.notify('{} was moved to {}'.format(file_name, path),
                title='{}'.format(title),
                execute='open {}'.format(path),
                )


def disable_input():
    window.configure(state='disabled')


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
                    if file_extension == ".dmg":
                        call(["open", new_destination])
                    else:
                        pass
                    hour_and_minute = datetime.now().strftime("%H:%M:%S")
                    message = f'  [{hour_and_minute}] - {file_name} was moved to {config_data_path}\n'
                    print(f'\033[4m{datetime.now().strftime("%H:%M:%S")}\033[0m - [{file_extension.upper()}] \033[95m{file_name}\033[0m was moved to \033[92m{config_data_path}\033[0m')
                    file_path = config_data_path
                    notification_of_file_movement(file_extension.upper(), file_name, file_path)
                    folder_button = tk.Button(window, text='Open in finder',
                                              width=9,
                                              padx=2,
                                              pady=2,
                                              cursor="hand",
                                              bd=1,
                                              command=lambda: call(["open", file_path]))
                    open_file_button = tk.Button(window, text=f'Open file [{file_extension.upper()}]',
                                                 width=10,
                                                 padx=4,
                                                 pady=2,
                                                 anchor='w',
                                                 cursor="hand",
                                                 bd=1,
                                                 command=lambda: call(["open", new_destination]))

                    for config_color_ext, config_color_color in config_color.items():
                        if config_color_ext == config_data_ext:
                            open_file_button.config(highlightbackground=config_color_color, highlightthickness=2)
                            folder_button.config(highlightbackground=config_color_color, highlightthickness=2)
                        else:
                            pass
                    window.window_create(tk.END, window=open_file_button)
                    window.window_create(tk.END, window=folder_button)
                    window.configure(state='normal')
                    window.insert(tk.END, message)
                    window.configure(state='disabled')
                else:
                    pass


event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, data["trackingFolder"], recursive=True)
observer.start()
root = tk.Tk()
root.geometry("1000x400")
root.title('Log')
# Add some transparency
# root.attributes('-alpha', 0.95)
window = tk.Text(
    root,
    font=('Helvetica', 13),
    padx=10,
    pady=10,
    cursor='arrow'
)
window.pack(
    fill="both",
    expand=True,
    padx=0,
    pady=0
)
window.config(
    highlightthickness=0,
    borderwidth=0
)
disable_input()
root.mainloop()
