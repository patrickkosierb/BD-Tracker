###
#   Author @ Patrick Kosierb
#   Run    @ python bd_parse.py
###
import subprocess
import datetime


## Return marcros ##
BD_OK =                  0
BD_PREV_LOG =            1
BD_ERROR_SUBPROCESS =    251
BD_ERROR_EXIST =         404
BD_ERROR_UNKNOWN =       -1

def check_bd(driver, bios):
    try:
        f = open("B-D_log.txt","r")
        sysinfo = []
        for element in range(0,4):
            line = f.readline()
            if(element>=2):
                sysinfo.append(line)
        f.close()
        if(sysinfo[1].strip() == driver.strip() and sysinfo[0].strip()==bios):
            return BD_PREV_LOG;
        else:
            return BD_OK;

    except FileNotFoundError:
        print(datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")+" :: New log file created.")
        f = open("B-D_log.txt","w")
        return BD_ERROR_EXIST;

    return BD_ERROR_UNKNOWN;

def write_bd(driver, bios):
    ct = datetime.datetime.now()
    try:
        f = open("B-D_log.txt","r+")
        data = f.read()
        f.seek(0,0)
        reason = "some reason"
        f.write("----------------------------------------------------\n"+"TIME   --- "+ct.strftime("%m/%d/%Y, %H:%M:%S")+" --- \n"+bios+"\n"+driver+"----\nREASON: \n"+reason+"\n"+data)
        f.close()
        return BD_OK;

    except FileNotFoundError:
        return BD_ERROR_EXIST;

    return BD_ERROR_UNKNOWN;

def get_bd():
    ct = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")

    info = subprocess.run('systeminfo | findstr BIOS', shell=True, capture_output=True)
    if info.returncode != 0:
        print(ct+" :: Failed to execute: 'systeminfo' :: Exiting process")
        return BD_ERROR_SUBPROCESS;
    raw_bios = info.stdout.decode().split(":")
    bios = raw_bios[1].strip()

    info = subprocess.run('cd | dir',shell=True, cwd='Desktop\DRIVER',capture_output=True)
    if info.returncode != 0:
        print(ct+" :: Failed to execute: 'cd | dir :: Exiting process")
        return BD_ERROR_SUBPROCESS;
    raw_driver = info.stdout.decode().split("<DIR>")
    driver = raw_driver[3].strip().split(" ")[0]

    bios_s = "SBIOS  --- "+bios
    driver_s = "DRIVER --- "+driver

    return driver_s, bios_s;
