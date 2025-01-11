#Python file
#Author: Frikk Brændsrød

import os


import os
import shutil

print("Remeber to pull the repo for the latest save file")
input = int(input("update to new save = 1, backup current save = 2: "))


source_path = r'current_save.zip'
destination_path = r'C:\Users\fribr\AppData\Roaming\Factorio\saves\Gjøvik.zip'

if input == 1:
    shutil.copyfile(destination_path, source_path)

elif input == 2:
    shutil.copyfile(source_path, destination_path)

else:
    print("Invalid input")
    exit()