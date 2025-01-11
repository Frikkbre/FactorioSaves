#Python file
#Author: Frikk Brændsrød
#Date: 2021-09-26
#Version: 1.0


import shutil
import subprocess

print("")
print("")
input = int(input("update to new save = 1, backup current save = 2: "))
print("You chose: ", input)
print("")
print("------------")


source_path = r'current_save.zip'
destination_path = r'C:\Users\fribr\AppData\Roaming\Factorio\saves\Gjøvik.zip'

if input == 1:
    shutil.copyfile(source_path, destination_path)
    subprocess.run(["git", "pull"])
    print("Updated to new save")

elif input == 2:
    shutil.copyfile(destination_path, source_path)

    subprocess.run(["git", "add", destination_path])
    subprocess.run(["git", "commit", "-m", "Updated latest save file"])
    subprocess.run(["git", "push"])
    print("Backup of current save done")


else:
    print("Invalid input")
    exit()