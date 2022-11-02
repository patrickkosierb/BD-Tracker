
from bdparse import check_bd, get_bd, datetime



def main():
    check_bd()
    ct = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    try:
        cur_driver, cur_bios = get_bd()
        print(ct+" :: Successfully retrieved SBIOS & DRIVER :: Procced to log \n")
    except TypeError:
        print(ct+" :: Failed to retrive SBIOS or DRIVER :: Exiting proccess")
        exit()

    return 0;

main();
