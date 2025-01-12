#Author: Frikk Brændsrød
#Date: 11.01.2025
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
destination_path = r'C:\Users\DINBRUKER\AppData\Roaming\Factorio\saves\Gjøvik.zip' #Change this to your own save file path

if input == 1:
    subprocess.run(["git", "fetch"])
    subprocess.run(["git", "pull"])
    shutil.copyfile(source_path, destination_path)
    print("Updated to new save")

elif input == 2:
    shutil.copyfile(destination_path, source_path)

    subprocess.run(["git", "add", source_path])
    subprocess.run(["git", "commit", "-m", "Updated latest save file"])
    subprocess.run(["git", "push"])
    print("Backup of current save done")


else:
    print("Invalid input")
    exit()