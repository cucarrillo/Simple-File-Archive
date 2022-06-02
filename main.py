# File Archiver
# 
# Created by Cesar Carrillo

# TODO: add these command-line arguments
#-h --help , help menu
#-o --onlyfolder , only create the folder
# sys.argv

# TODO: add GUI version
# see idea.png for details

# Imports
import os
import sys
import shutil
import re
import datetime
import time

SAVE_FOLDER_PATH    = "save";
PATHS_FILE_PATH     = "paths";
ARCHIVE_TYPE        = "zip";

# Copy a folder from one location to another
def copyFolder(folder, output):
    shutil.copytree(folder, output, dirs_exist_ok=True);

    print(F"Copied \"{folder}\" into \"{output}\"");

# Zip a folder
def zipup(savePath, archiveType):
    shutil.make_archive(savePath, archiveType, savePath);

    print(F"Zipped save folder to \"{savePath}\"");

# Return the paths of a directory
def grabPaths(pathsPath):
    try:
        pathsFile = open(pathsPath, "r");

        pathsList = pathsFile.readlines();

        for path in pathsList:
            info = re.split(r"\t+", path.split("\n")[0]);

            copyFolder(info[1], F"save/{info[0]}");

        return True;
    except FileNotFoundError:

        if(not ".txt" in pathsPath):
            return grabPaths(pathsPath + ".txt");
        else:
            print(F"Paths File \"{pathsPath}\" was not found.");
            return False;

# Writes the info file
def writeInfo():
    today = datetime.datetime.now();
    todayStr = today.strftime("%x at %X");

    readme = open("save/readme.txt", "w");
    readme.write(F"This archive was created on {todayStr}.");
    readme.write("Created using File Archiver");

    readme.close();

# Entry point
def main():
    nocomp      = False;     # No compression
    type        = "zip";    # Compression type
    filepath    = PATHS_FILE_PATH;  # File path
    keepfolder  = False;    # Keep folder after compression
    onlyfolder  = False;    # Only create the folder

    arguments = sys.argv[1:];

    # For double clicking .sfa files meant for windows users
    if(len(arguments) > 0):
        if(".sfa" in arguments[0]):
            filepath = arguments[0];
            arguments = [];
            
    i = 0;

    while(i < len(arguments)):

        argument = arguments[i];

        validArgument = False;

        #-n --nocomp , does not compress the created folder
        if(argument == "-n" or argument == "--nozip"): 
            nocomp = True;
            validArgument = True;

        #-k --keepfolder , keep the folder created
        if(argument == "-k" or argument == "--keepfolder"): 
            keepfolder = True;
            validArgument = True;

        #-o --onlyfolder , only create the folder
        if(argument == "-o" or argument == "--onlyfolder"): 
            onlyfolder = False;
            validArgument = True;
        
        #-t --type , set the compress filetype
        if(argument == "-t" or argument == "--type"):
            i += 1;

            if(i < len(arguments)):
                type = arguments[i];
                validArgument = True;
            else:
                print("Error: -t/--type needs a value");
                return;

        #-f --filepath , the path file location
        if(argument == "-f" or argument == "--filepath"): 
            i += 1;

            if(i < len(arguments)):
                filepath = arguments[i];
                validArgument = True;
            else:
                print("Error: -f/--filepath needs a value");
                return;

        if(not validArgument):
            print(F"Invalid argument ({argument}).");
            return;

        i += 1;

    result = grabPaths(filepath);

    if(not result): return;

    writeInfo();

    if(not nocomp):
        zipup(SAVE_FOLDER_PATH, type);
        if(not keepfolder):
            shutil.rmtree(SAVE_FOLDER_PATH);
            print(F"Delted \"{SAVE_FOLDER_PATH}\"");

if __name__ == "__main__":
    main();