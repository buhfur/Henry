import os
import sys

#script to handle all github operations automatically 


def update_git(file_name_array):
    #tool to add and then commit files
    FILES = file_name_array

    for file in FILES:
        try:

            os.system("git add {}").format(file)

            print("file {} was  added sucessfully").format(file)

            #now commit the files

        except Exception as e:
            print("couldent add file {}").format(file)
