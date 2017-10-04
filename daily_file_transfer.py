import shutil
import os
import datetime
from datetime import timedelta

src = 'C:\Users\Daler Rakhmet-Zade\Desktop\The Tech Academy\Python\Python Drills\shutil drill\Folder A' #'source'
dst = 'C:\Users\Daler Rakhmet-Zade\Desktop\The Tech Academy\Python\Python Drills\shutil drill\Folder B' #'destination'

files = os.listdir(src)

new_files = datetime.datetime.now() - datetime.timedelta(hours=24)
    
for file in files:
    src_file = os.path.join(src, file)
    dst_file = os.path.join(dst, file)
    mod_time = datetime.datetime.fromtimestamp(os.stat(src_file).st_mtime)
    if mod_time < new_files:
        shutil.move(src_file, dst_file)
        print(src_file, dst_file)
        
    
