import os
from pathlib import Path
import shutil
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import errno

# This is the way I like to organize my files,
# But you can change in your way

# English version
# files_extensions = {
#     "Images": [".jpg", ".jpeg", ".jfif", ".pjpeg", ".pjp", ".png", ".gif", ".webp", ".apng", ".avif"],
#     "Videos": [".webm", ".MTS", ".M2TS", ".TS", ".mov", ".mp4", ".m4p", ".m4v", ".mxf", ".mkv"],
#     "Audios": [".3ga", ".aac", ".ac3", ".aif", ".aiff", ".alac", ".amr", ".ape", ".au", ".dss", ".flac", ".flv", ".m4a", ".m4b", ".m4p", ".mp3", ".mpga", ".ogg", ".oga", ".mogg", ".opus", ".qcp", ".tta", ".voc", ".wav", ".wma", ".wv"],
#     "Svg": [".svg"],
#     "Executables": [".exe"],
#     "Torrent": [".torrent"],
#     "ISO": [".iso"],
#     "Documents": [".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".txt", ".rtf", ".odt", ".ods", ".odp", ".csv"],
#     "Zipped": [".zip", ".rar"],
#     "Notepads": [".txt"],
# }

# Versão em português
files_extensions = {
    "Imagens": [".jpg", ".jpeg", ".jfif", ".pjpeg", ".pjp", ".png", ".gif", ".webp", ".apng", ".avif"],
    "Vídeos": [".webm", ".MTS", ".M2TS", ".TS", ".mov", ".mp4", ".m4p", ".m4v", ".mxf", ".mkv"],
    "Áudios": [".3ga", ".aac", ".ac3", ".aif", ".aiff", ".alac", ".amr", ".ape", ".au", ".dss", ".flac", ".flv", ".m4a", ".m4b", ".m4p", ".mp3", ".mpga", ".ogg", ".oga", ".mogg", ".opus", ".qcp", ".tta", ".voc", ".wav", ".wma", ".wv"],
    "Svg": [".svg"],
    "Executáveis": [".exe"],
    "Torrent": [".torrent"],
    "ISO": [".iso"],
    "Documentos": [".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".txt", ".rtf", ".odt", ".ods", ".odp", ".csv"],
    "Zipados": [".zip", ".rar"],
    "Blocos de Notas": [".txt"],
}

def get_folder_extension(ext):
    for folder, exts in files_extensions.items():
        if ext in exts:
            return folder
    # return "Others"
    return "Outros"

# Put your Download Directory
# Or just the Path you want to organize / watch
download_file_path = "C:\\Users\\gabri\\Documents\\HD\\AOp\\2023\\Python\\file-organizer\\testFile"

def organize_existing_files():
    for file in os.listdir(download_file_path):
        path_file = os.path.join(download_file_path, file)
        if os.path.isfile(path_file):
            organize_single_file(path_file)

def organize_single_file(file_path):
    file_name = os.path.basename(file_path)
    extension = os.path.splitext(file_name)[1].lower()
    folder = get_folder_extension(extension)
    destination_folder = os.path.join(download_file_path, folder)
    Path(destination_folder).mkdir(parents=True, exist_ok=True)

    destination_path = os.path.join(destination_folder, file_name)

    attempts = 5

    # The attempts is because if you copy and paste some file
    # In the directory, the file is being used, so the watcher
    # Can't interact with the file
    # So we try sometimes until we can move :)

    while attempts > 0:
        try: 
            shutil.move(file_path, destination_path)
            print("File moved succesfully")
            break
        except PermissionError as e:
            if e.errno == errno.EACCES:
                print("File in use, trying again in 1 second")
                time.sleep(1)
                attempts -= 1
            else: 
                raise e
        except FileNotFoundError as e:
            print(f"File not found: {e}")
            break
        except Exception as e:
            print(f"Error moving file: {e}")
            break
    else:
        print("Fail after several attemps")

class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            print(f"New file detected: {event.src_path}")
            try:
                organize_single_file(event.src_path)
            except:
                print(f"The file was not organized")

    def on_modified(self, event):
        if not event.is_directory:
            print(f"Modified file: {event.src_path}")
            try:
                organize_single_file(event.src_path)
            except Exception as e:
                print(f"Failed to organize file: {e}")


    def on_moved(self, event):
        if not event.is_directory:
            print(f"Moved file: {event.src_path} to {event.dest_path}")
            if Path(event.dest_path).parent == Path(download_file_path):
                print(f"File moved into observed directory")
                try:
                    organize_single_file(event.dest_path)
                except Exception as e:
                    print(f"Failed to organize file {e}")

if __name__ == "__main__":

    if not os.path.isdir(download_file_path):
        raise ValueError("This directory was not found")

    organize_existing_files()

    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, download_file_path, recursive=True)
    observer.start()

    try:
        print("Watching download history")

        while True:
            time.sleep(1)
    except KeyboardInterrupt as e:
        observer.stop()
        print(f"Error organizing file: {e}")

    observer.join()