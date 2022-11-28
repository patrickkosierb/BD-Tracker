###
#   Author @ Patrick Kosierb
#   Run    @ python main.py
###
import bdparse
from bdparse import datetime

def main():
    bd = bdparse.BDParse()
    bd.init_bd()
    ct = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    try:
        cur_driver, cur_bios = bd.get_bd()
        status = bd.check_bd(cur_driver, cur_bios)
        if(status==bd.OK() or status==bd.ERROR_EXIST()):
            ct =datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
            status=bd.write_bd(cur_driver, cur_bios)
            if(status==bd.OK()):
                print(ct+" :: Successfully wrote SBIOS & DRIVER :: \n")
            else:
                print(ct+" :: Failed to write SBIOS & DRIVER :: Exiting process\n")
                exit()
        elif(status==bd.PREV_LOG()):
            print(ct+" :: SBIOS & DRIVER already logged \n")
        else:
            print(ct+" :: Unknown error :: Exiting proccess\n")
            exit()
    except TypeError:
        print(ct+" :: Failed to retrive SBIOS or DRIVER :: Exiting proccess")
        exit()

    return 0;

main();
