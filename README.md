# Simple File Archive
Copy and compress files and folders with a single command.

## Usage
To use SFA, create a file (recommended name `paths` or `paths.txt`).

This file can be under the same directory as the binary or anywhere you would like.

In this file, you can write which files/folders you would like to save alongside a name for the copies.

```
For example, in "paths.txt":
csgo  C:\Program Files (x86)\Steam\userdata\23443\730\local\cfg\

Essentially, the format is as follows:
<copy_name> <path>
```

If the file is under the same directory as the binary then you just have to run the binary with no options.

Otherwise, you will have to run the binary with the following option `-f <path/to/file>`

To see other options run `sfa -h`

### For Windows Users
Follow these steps to make the app easier to run.

- Add the extension `.SFA` to your file name
- Right-click on your file, choose `Open With -> Choose another app`
- Click on `More apps` and find the binary location and choose it.
- Enable `Always use this app to open .SFA files`
- Click `OK`

Now you can run any .SFA files 

## Requirements for building
- Python 3.10+ & PIP
- Pyinstaller

## Downloading
Windows binary found [here](https://github.com/cucarrillo/Simple-File-Archive/raw/main/bin/SFA.exe)
For Linux users, you are gonna have to compile from source

## Compiling
- Clone the reo `git clone https://github.com/cucarrillo/Simple-File-Archive.git`
- Install the requirements `pip install -r requirements`
- For Linux, run `compile_linux`
- For Windows, run `compile_windows.bat`
- Your binary will be compiles to the `bin` folder
