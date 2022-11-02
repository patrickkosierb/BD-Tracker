###
#   Author @ Patrick Kosierb
#   Run    @ python bd_parse.py
###
import subprocess
import datetime

def check_bd():
    try:
        f = open("B-D_log.txt","r")
        # continue writting here
    except FileNotFoundError:
        print(datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")+" :: New log file created.")
        f = open("B-D_log.txt","w")

    return 0;

def write_bd(driver, bios):
    ct = datetime.datetime.now()
    f = open("B-D_log.txt","a")
    f.write("----------------------------------------------------\n"+"TIME   --- "+ct.strftime("%m/%d/%Y, %H:%M:%S")+" --- \n"+"SBIOS  --- "+bios+"\n"+"DRIVER --- "+driver)
    reason = "some reason"
    f.write("----\nREASON: \n"+reason+"\n")
    f.close()
    return 0;

def get_bd():
    ct = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")

    info = subprocess.run('systeminfo | findstr BIOS', shell=True, capture_output=True)
    if info.returncode != 0:
        print(ct+" :: Failed to execute: 'systeminfo' :: Exiting process")
        return -1
    raw_bios = info.stdout.decode().split(":")
    bios = raw_bios[1].strip()

    info = subprocess.run('cd | dir',shell=True, cwd='Desktop\DRIVER',capture_output=True)
    if info.returncode != 0:
        print(ct+" :: Failed to execute: 'cd | dir :: Exiting process")
        return -1
    raw_driver = info.stdout.decode().split("<DIR>")
    driver = raw_driver[3].strip().split(" ")[0]

    return driver, bios;
