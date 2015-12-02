# FileRenamer.py
# Mendel Hornbacher
# November 29 2015
# Simple bulk file renamer Importable as function and runable from terminal/cmd

import os, sys

#function
def rename(folder, ext):
    #clean up path given
    folder = folder.replace('"', '')    #Get rid of " in path
    if not folder.endswith('\\'):       #Check for windows path divider at the end
        if folder.find('\\') > 0:       #Check if it is windows
            folder += '\\'              #Add path divider to the end
            print('windows')            
    elif not folder.endswith('/'):      #Same for unix/linux
        if folder.find('/') > 0:
            folder += '/'
            print('unix like')

    #Rename files
    for filename in os.listdir(folder):             #for every file in the folder
        infilepath = os.path.join(folder, filename) #make a path out of it
        if os.path.isfile(infilepath) == False:     #Check if it is valid
            continue                                #if not: next

        oldname = os.path.splitext(filename)        #split the name and extension
        newname = folder + oldname[0] + '.' + ext   #add the name to the new extension
        os.rename(infilepath, newname)              #rename the file
        

#Terminal code when run directly / interface
running = True
while (running):
    folder = input("Folder location: ")
    ext = input("New file extension: ")
    rename(folder, ext)

    #keep running?
    continuerunning = input("Another folder (y/else)? ")
    print(continuerunning)
    if continuerunning.lower() == 'y':
        running = True
    else:
        running = False
