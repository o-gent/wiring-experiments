import os
from time import sleep
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from wireviz import wireviz

class Handler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path == r".\demo.yml": # in this example, we only care about this one file
            print("regen")
            try:
                with wireviz.open_file_read("./demo.yml") as fh:
                    file_out, _ = os.path.splitext("demo.yml")
                    yaml_input = fh.read()
                    wireviz.parse(yaml_input, file_out=file_out)
            except:
                print("wireviz failure")

observer = Observer()
observer.schedule(Handler(), ".") # watch the local directory
observer.start()

try:
    while True:
        sleep(1)
except KeyboardInterrupt:
    observer.stop()

observer.join()