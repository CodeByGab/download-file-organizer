import os
from pathlib import Path
import shutil
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import errno

# This is the way I like to organize my files,
# But you can change in your way

files_extensions = {
    "Imagens": [".jpg", ".jpeg", ".jfif", ".pjpeg", ".pjp", ".png", ".gif", ".webp", ".apng", ".avif"],
    "Vídeos": [".webm", ".MTS", ".M2TS", ".TS", ".mov", ".mp4", ".m4p", ".m4v", ".mxf", ".mkv"],
    "Áudio": [".3ga", ".aac", ".ac3", ".aif", ".aiff", ".alac", ".amr", ".ape", ".au", ".dss", ".flac", ".flv", ".m4a", ".m4b", ".m4p", ".mp3", ".mpga", ".ogg", ".oga", ".mogg", ".opus", ".qcp", ".tta", ".voc", ".wav", ".wma", ".wv"],
    "Svg": [".svg"],
    "Executáveis": [".exe"],
    "Torrent": [".torrent"],
    "ISO": [".iso"],
    "Documentos": [".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".txt", ".rtf", ".odt", ".ods", ".odp", ".csv"],
    "Zipados": [".zip", ".rar"],
    "Bloco de Notas": [".txt"],
}

def get_folder_extension(ext):
    for folder, exts in files_extensions.items():
        if ext in exts:
            return folder
    return "Outros"

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
    Path(folder).mkdir(exist_ok=True)

    destination_path = os.path.join(download_file_path, folder, file_name)

    attempts = 5

    while attempts > 0:
        try: 
            shutil.move(file_path, destination_path)
            print("arquivo movido com sucesso")
            break
        except PermissionError as e:
            if e.errno == errno.EACCES:
                print("arquivo em uso, tentando novamente em 1 segundo")
                time.sleep(1)
                attempts -= 1
            else: 
                raise e
        except FileNotFoundError as e:
            print("arquivo não encontrado")
            break
        except Exception as e:
            print("Erro ao mover o arquivo")
            break
    else:
        print("falha após várias tantaivas")

class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            print(f"Novo arquivo detectado: {event.src_path}")
            try:
                organize_single_file(event.src_path)
            except:
                print(f"arquivo nao foi organizado")

    def on_modified(self, event):
        if not event.is_directory:
            print(f"Arquivo modificado: {event.src_path}")
            organize_single_file(event.src_path)

    def on_moved(self, event):
        if not event.is_directory:
            print(f"Arquivo movido: {event.src_path} para {event.dest_path}")
            # Verifica se o arquivo movido está dentro do diretório observado
            if Path(event.dest_path).parent == Path(download_file_path):
                print(f"Arquivo movido para dentro do diretório observado")
                organize_single_file(event.dest_path)

if __name__ == "__main__":

    if not os.path.isdir(download_file_path):
        raise ValueError("This directory was not found")

    organize_existing_files()

    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, download_file_path, recursive=True)
    observer.start()

    try:
        print("Observando historico de downlaod")

        while True:
            time.sleep(1)
    except KeyboardInterrupt as e:
        observer.stop()
        print(f"Erro ao organizar arquivo: {e}")

    observer.join()