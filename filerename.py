# rename files in a directory

import os

def rename_files():
    #get filenames from a folder
    file_list = os.listdir(r"/home/roni/Documents/Udacity_OOPPython_Repo/OOPPython/prank")
    print(file_list)

    #switch working directory
    saved_path = os.getcwd()
    print("Current working directory = "+saved_path)
    os.chdir(r"/home/roni/Documents/Udacity_OOPPython_Repo/OOPPython/prank")

    #rename
    for file_name in file_list:
        os.rename(file_name, file_name.translate(None, "0123456789"))

    #return to prev working dir
    os.chdir(saved_path)
        
    file_list = os.listdir(r"/home/roni/Documents/Udacity_OOPPython_Repo/OOPPython/prank")
    print file_list


rename_files()
