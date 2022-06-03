# Simple File Archiver (SFA)
# version:  1.0
# author:   Cesar Carrillo

# [TODO]
# - add GUI version

# Imports
import os
import sys
import shutil
import re
import datetime
import time

SAVE_FOLDER_PATH    = "save";

# Copy a folder from one location to another
def copyFolder(folder, output):
    shutil.copytree(folder, output, dirs_exist_ok=True);

    print(F"Copied \"{folder}\" into \"{output}\"");

# Zip a folder
def zipup(savePath, archiveType):
    try:
        shutil.make_archive(savePath, archiveType, savePath);

        print(F"Zipped save folder to \"{savePath}\"");

        return True;

    except ValueError: 
        
        print(F"Invalid compression type \"{archiveType}\""); return False;

# Return the paths of a directory
def grabPaths(pathsPath):
    try:
        # Open the file
        pathsFile = open(pathsPath, "r");
        pathsList = pathsFile.readlines();

        # Copy each file into the the speficied folder
        # Format: <folder> <path>
        for path in pathsList:
            info = re.split(r"\t+", path.split("\n")[0]);

            copyFolder(info[1], F"save/{info[0]}");

        return True;

    except FileNotFoundError:

        # Try this function again with a .txt extension
        if(not pathsPath.endswith(".txt")):
            return grabPaths(pathsPath + ".txt");
        else:
            print(F"Paths File \"{pathsPath}\" was not found."); return False;

# Writes the info file
def writeInfo():
    today = datetime.datetime.now();
    todayStr = today.strftime("%x at %X");

    readme = open("save/readme.txt", "w");
    readme.write(F"This archive was created on {todayStr}.\n");
    readme.write("Created using Simple File Archiver");

    readme.close();

# Entry point
def main():
    nocomp      = False;    # No compression
    type        = "zip";    # Compression type
    filepath    = "paths";  # File path
    keepfolder  = False;    # Keep folder after compression
    onlyfolder  = False;    # Only create the folder

    arguments = sys.argv[1:]; # Grab passed agruments

    # For double clicking .sfa files meant for windows users
    if(len(arguments) > 0):
        if(arguments[0].endswith(".sfa")):
            filepath = arguments[0];
            arguments = [];

    i = 0; # psuedo for loop

    # go through passed arguments and make the corresponding changes
    while(i < len(arguments)):

        argument = arguments[i]; # grab argument

        validArgument = False; # test if argument is valid

        #-h --help , help menu
        if(argument == "-h" or argument == "--help"):
            print("Simple File Archiver");
            print("copy and compress files and folders with a single command.");
            print("created by Cesar Carrillo.\n");
            print("usage: sfa [options] \n");
            print("options: ");
            print("     -h, --help           display this message");
            print("     -n, --nocomp         does not compress the folder");
            print("     -k, --keepfolder     keeps folder after compression");
            print("     -o, --onlyfolder     only creates the folder");
            print("     -t, --type TYPE      set the compression type (zip/tar/gztar)");
            print("     -f, --filepath PATH  speficiy the file to be used");
            return;
        
        #-n --nocomp , does not compress the created folder
        if(argument == "-n" or argument == "--nozip"): 
            nocomp          = True;
            validArgument   = True;

        #-k --keepfolder , keep the folder created
        if(argument == "-k" or argument == "--keepfolder"): 
            keepfolder      = True;
            validArgument   = True;

        #-o --onlyfolder , only create the folder
        if(argument == "-o" or argument == "--onlyfolder"): 
            onlyfolder      = False;
            validArgument   = True;
        
        #-t --type , set the compress filetype
        if(argument == "-t" or argument == "--type"):
            i += 1;

            if(i < len(arguments)):
                type            = arguments[i];
                validArgument   = True;
            else:
                print("Error: -t/--type needs a value"); return;

        #-f --filepath , the path file location
        if(argument == "-f" or argument == "--filepath"): 
            i += 1;

            if(i < len(arguments)):
                filepath        = arguments[i];
                validArgument   = True;
            else:
                print("Error: -f/--filepath needs a value"); return;

        # display error and return if not a valid argument
        if(not validArgument):
            print(F"Invalid argument ({argument}).");
            return;

        i += 1; # next argument

    result = grabPaths(filepath);

    if(not result): return; # exit if failed

    writeInfo(); # write info to folder

    # only do the following if the -o option was not passed
    if(not onlyfolder):

        # zip folder
        if(not nocomp):
            result = zipup(SAVE_FOLDER_PATH, type);

            if(not result): return; # exit if failed

            # delete folder
            if(not keepfolder):
                shutil.rmtree(SAVE_FOLDER_PATH);
                print(F"Deleted \"{SAVE_FOLDER_PATH}\"");
    
    print("SFA will exit in 10 seconds."); time.sleep(10);

if __name__ == "__main__": 
    try: main();
    except KeyboardInterrupt: print("Quitting SFA.");