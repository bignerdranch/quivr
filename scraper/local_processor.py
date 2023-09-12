import glob
import os

import requests

from parsers.audio import process_audio
from parsers.code_python import process_python
from parsers.csv import process_csv
from parsers.docx import process_docx
from parsers.epub import process_epub
from parsers.html import process_html
from parsers.markdown import process_markdown
from parsers.notebook import process_ipnyb
from parsers.odt import process_odt
from parsers.pdf import process_pdf
from parsers.powerpoint import process_powerpoint
from parsers.txt import process_txt
from parsers.xlsx import process_xlsx

UPLOAD = "http://localhost:5050/upload"

DIR = "upload/*"

file_processors = {
    ".txt": process_txt,
    ".csv": process_csv,
    ".md": process_markdown,
    ".markdown": process_markdown,
    ".m4a": process_audio,
    ".mp3": process_audio,
    ".webm": process_audio,
    ".mp4": process_audio,
    ".mpga": process_audio,
    ".wav": process_audio,
    ".mpeg": process_audio,
    ".pdf": process_pdf,
    ".html": process_html,
    ".pptx": process_powerpoint,
    ".docx": process_docx,
    ".odt": process_odt,
    ".xlsx": process_xlsx,
    ".xls": process_xlsx,
    ".epub": process_epub,
    ".ipynb": process_ipnyb,
    ".py": process_python,
}

for file in glob.glob(DIR):
    file_name, file_ext = os.path.splitext(file)
    if file_ext in file_processors:
        data = open(file, 'rb').read()
        headers = {
            "Content-Type": "application/binary"
        }
        requests.post(UPLOAD, data=data, headers=headers)
