import bdparse
# from bdparse import check_bd, get_bd, write_bd, datetime

def main():

    bd = bdparse.BDParse()
    c_driver, c_bios = bd.get_bd()
    # ct = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    # try:
    #     cur_driver, cur_bios = get_bd()
    #     status = check_bd(cur_driver, cur_bios)
    #     if(status==bdparse.BD_OK):
    #         ct =datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    #         status=write_bd(cur_driver, cur_bios)
    #         if(status==bdparse.BD_OK):
    #             print(ct+" :: Successfully wrote SBIOS & DRIVER :: \n")
    #         else:
    #             print(ct+" :: Failed to write SBIOS & DRIVER :: Exiting process\n")
    #             exit()
    #     elif(status ==bdparse.BD_ERROR_EXIST):
    #         ct =datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    #         status=write_bd(cur_driver, cur_bios)
    #         if(status==bdparse.BD_OK):
    #             print(ct+" :: Successfully wrote SBIOS & DRIVER :: \n")
    #         else:
    #             print(ct+" :: Failed to write SBIOS & DRIVER :: Exiting process\n")
    #             exit()
    #     elif(status==bdparse.BD_PREV_LOG):
    #         print(ct+" :: SBIOS & DRIVER already logged :: \n")
    #     else:
    #         print(ct+" :: Unknown error :: Exiting proccess\n")
    #         exit()
    # except TypeError:
    #     print(ct+" :: Failed to retrive SBIOS or DRIVER :: Exiting proccess")
    #     exit()


    return 0;

main();
