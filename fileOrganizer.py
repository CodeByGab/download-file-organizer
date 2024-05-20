import os
from pathlib import Path
import shutil

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

os.chdir("C:\\Users\\gabri\\Documents\\HD\\AOp\\2023\\Python\\file-organizer\\testFile")

for file in os.listdir():
    if os.path.isfile(file):
        extension = os.path.splitext(file)[1].lower()
        folder = get_folder_extension(extension)
        Path(folder).mkdir(exist_ok=True)
        shutil.move(file, os.path.join(folder, file))