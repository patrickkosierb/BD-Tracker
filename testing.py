
class BDError:
    __OK =                  1
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

# have another class for parsing then make it inherit this

class BDParse(BDError):
    status = BDError()
    def trial(self):
        return self.status.OK()

test = BDParse()
print(test.trial())
