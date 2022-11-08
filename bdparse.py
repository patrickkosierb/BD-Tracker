###
#   Author @ Patrick Kosierb
#   Run    @ python bd_parse.py
###
import subprocess
import datetime
import bdui

class BDError:
    __OK =                  0
    __PREV_LOG =            1
    __ERROR_SUBPROCESS =    251
    __ERROR_EXIST =         404
    __ERROR_UNKNOWN =       -1

    def OK(self):
        return self.__OK
    def PREV_LOG(self):
        return self.__PREV_LOG
    def ERROR_SUBPROCESS(self):
        return self.__ERROR_SUBPROCESS
    def ERROR_EXIST(self):
        return self.__ERROR_EXIST
    def ERROR_UNKNOWN(self):
        return self.__ERROR_UNKNOWN

class BDParse(BDError):
    status = BDError()

    def get_bd(self):
        ct = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")

        info = subprocess.run('systeminfo | findstr BIOS', shell=True, capture_output=True)
        if info.returncode != 0:
            print(ct+" :: Failed to execute: 'systeminfo' :: Exiting process")
            return self.status.ERROR_SUBPROCESS();
        raw_bios = info.stdout.decode().split(":")
        bios = raw_bios[1].strip()

        info = subprocess.run('cd | dir',shell=True, cwd='Desktop\DRIVER',capture_output=True)
        if info.returncode != 0:
            print(ct+" :: Failed to execute: 'cd | dir :: Exiting process")
            return self.status.ERROR_SUBPROCESS();
        raw_driver = info.stdout.decode().split("<DIR>")
        driver = raw_driver[3].strip().split(" ")[0]

        bios_s = "SBIOS  --- "+bios
        driver_s = "DRIVER --- "+driver

        return driver_s, bios_s;

    def check_bd(self, driver, bios):
        try:
            f = open("B-D_log.txt","r")
            sysinfo = []
            for element in range(0,4):
                line = f.readline()
                if(element>=2):
                    sysinfo.append(line)
            f.close()
            if(sysinfo[1].strip() == driver.strip() and sysinfo[0].strip()==bios):
                return self.status.PREV_LOG();
            else:
                return self.status.OK();

        except FileNotFoundError:
            print(datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")+" :: New log file created.")
            f = open("B-D_log.txt","w")
            return self.status.ERROR_EXIST();

        return self.status.ERROR_UNKNOWN();

    def write_bd(self,driver, bios):
        ct = datetime.datetime.now()
        try:
            f = open("B-D_log.txt","r+")
            data = f.read()
            f.seek(0,0)
            bdui.root.mainloop()
            f.write("----------------------------------------------------\n"+"TIME   --- "+ct.strftime("%m/%d/%Y, %H:%M:%S")+" --- \n"+bios+"\n"+driver+"----\nREASON: \n"+bdui.reason+"\n"+data)
            f.close()
            return self.status.OK();

        except FileNotFoundError:
            return self.status.ERROR_EXIST();

        return self.status.ERROR_UNKNOWN();
