import os
import shutil
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Define the directories
DIRECTORIES = {
    "png": r"C:\PNG",
    "jpeg": r"C:\JPEG",
    "jpg": r"C:\JPG",
    "mp4": r"C:\MP4",
    "mp3": r"C:\MP3"
}

# Define your Downloads directory
DOWNLOADS_FOLDER = r"C:\Users\oit\Dropbox\PC\Downloads"

class FileHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return
        # Add a small delay to ensure the file is fully written
        time.sleep(2)
        file_extension = event.src_path.split(".")[-1].lower()
        destination_dir = DIRECTORIES.get(file_extension)
        if destination_dir:
            self.move_file(event.src_path, destination_dir)

    def move_file(self, src_path, dest_dir):
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)
        # Retry moving the file up to 5 times with a delay
        for _ in range(5):
            try:
                shutil.move(src_path, dest_dir)
                print(f"Moved {src_path} to {dest_dir}")
                break
            except FileNotFoundError as e:
                print(f"File not found, retrying: {e}")
                time.sleep(2)
            except PermissionError as e:
                print(f"Permission error, retrying: {e}")
                time.sleep(2)
            except Exception as e:
                print(f"Error moving file, retrying: {e}")
                time.sleep(2)
        else:
            print(f"Failed to move file after multiple attempts: {src_path}")

if __name__ == "__main__":
    event_handler = FileHandler()
    observer = Observer()
    observer.schedule(event_handler, DOWNLOADS_FOLDER, recursive=False)
    observer.start()

    print("Script is running...")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
