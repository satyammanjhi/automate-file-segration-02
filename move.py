import os
import shutil

from_dir="C:/Users/M/Downloads"
to_dir="C:/Users/M/Desktop/download_files"

dir_tree = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Document_Files": ['.ppt', '.xls', '.xlsx' '.csv', '.pdf', '.txt'],
}

for file_name in dir_tree:
    name,extension=os.path.splitext(file_name)
    print(name)
    print(extension)

    if extension=='':
            continue
    if extension in ['.gif','.png','.jpg','.jpeg','.jfif','.pdf']:
            path1=from_dir+'/'+file_name
            path2=to_dir+'/'+'Document_Files'
            path3=to_dir+'/'+'Document_Files'+'/'+file_name

            if os.path.exists(path2):
                print("Moving")
                shutil.move(path1,path3)

            else:
                os.makedirs(path2)
                print("Moving")
                shutil.move(path1,path3)