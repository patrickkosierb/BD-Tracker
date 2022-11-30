# BD-Tracker
The purpose of this software is to record a log of current SBIOS and Driver for debug purposes.  

### Setup 
Currently in order for successful driver parsing, the driver package must be in the path: \Desktop\DRIVER\your_driver_package_name and it must be the only driver in package in the folder.


run.bat setup:

@echo off
cd "path to app directory (BD-Tracker)"
"path to python.exe" "path to main.py"

