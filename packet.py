
_reg_names = {
    0x00: ['XG_OFFS_TC'        ,'GYRO',[
          [7,7,['PWR_MODE'   ,'PWR' ,'P']],
          [6,1,['XG_OFFS_TC' ,'OFFS','O']],
          [0,0,['OTP_BNK_VLD','VLD' ,'V']]
          ],True],
    0x01: ['YG_OFFS_TC'        ,'GYRO',[
          [7,7,['PWR_MODE'   ,'PWR' ,'P']],
          [6,1,['YG_OFFS_TC' ,'OFFS','O']],
          [0,0,['OTP_BNK_VLD','VLD' ,'V']]
          ],True],
    0x02: ['ZG_OFFS_TC'        ,'GYRO',[
          [7,7,['PWR_MODE'   ,'PWR' ,'P']],
          [6,1,['ZG_OFFS_TC' ,'OFFS','O']],
          [0,0,['OTP_BNK_VLD','VLD' ,'V']]
          ],True],
    0x03: ['X_FINE_GAIN'       ,'OTHER',None,True],
    0x04: ['Y_FINE_GAIN'       ,'OTHER',None,True],
    0x05: ['Z_FINE_GAIN'       ,'OTHER',None,True],
    0x06: ['XA_OFFS_H'         ,'ACCEL',None,True],
    0x07: ['XA_OFFS_L_TC'      ,'ACCEL',None,True],
    0x08: ['YA_OFFS_H'         ,'ACCEL',None,True],
    0x09: ['YA_OFFS_L_TC'      ,'ACCEL',None,True],
    0x0a: ['ZA_OFFS_H'         ,'ACCEL',None,True],
    0x0b: ['ZA_OFFS_L_TC'      ,'ACCEL',None,True],
    0x0d: ['SELF_TEST_X'       ,'OTHER',[
          [7,5,['XA_TEST[4-2]'   ,'XAT' ,'A']],
          [4,0,['XG_TEST[4-0]'   ,'XGT' ,'G']],
          ],True],
    0x0e: ['SELF_TEST_Y'       ,'OTHER',[
          [7,5,['YA_TEST[4-2]'   ,'YAT' ,'A']],
          [4,0,['YG_TEST[4-0]'   ,'YGT' ,'G']],
          ],True],
    0x0f: ['SELF_TEST_Z'       ,'OTHER',[
          [7,5,['ZA_TEST[4-2]'   ,'ZAT' ,'A']],
          [4,0,['ZG_TEST[4-0]'   ,'ZGT' ,'G']],
          ],True],
    0x10: ['SELF_TEST_A'       ,'OTHER',[
          [7,6,['-'              ,'-'   ,'-']],
          [5,4,['XA_TEST[1-0]'   ,'XAT' ,'X']],
          [3,2,['YA_TEST[1-0]'   ,'YAT' ,'Y']],
          [1,0,['ZA_TEST[1-0]'   ,'ZAT' ,'Z']],
          ],True],
    0x13: ['XG_OFFS_USRH'      ,'GYRO'  ,None,True],
    0x14: ['XG_OFFS_USRL'      ,'GYRO'  ,None,True],
    0x15: ['YG_OFFS_USRH'      ,'GYRO'  ,None,True],
    0x16: ['YG_OFFS_USRL'      ,'GYRO'  ,None,True],
    0x17: ['ZG_OFFS_USRH'      ,'GYRO'  ,None,True],
    0x18: ['ZG_OFFS_USRL'      ,'GYRO'  ,None,True],
    0x19: ['SMPLRT_DIV'        ,'CONFIG',None,True],
    0x1a: ['CONFIG'            ,'CONFIG',[
          [7,6,['-'           ,'-'   ,'-']],
          [5,3,['EXT_SYNC_SET','EXT' ,'S']],
          [2,0,['DLPF_CFG'    ,'DLPF','F']]
          ],True],
    0x1b: ['GYRO_CONFIG'       ,'GYRO',[
          [7,7,['XG_ST'  ,'XST','X']],
          [6,6,['YG_ST'  ,'YST','Y']],
          [5,5,['ZG_ST'  ,'ZST','Z']],
          [4,3,['GFS_SEL','FS' ,'F']],
          [2,0,['-'     ,'-'  ,'-']]
          ],True],
    0x1c: ['ACCEL_CONFIG'      ,'ACCEL',[
          [7,7,['XA_ST'  ,'XST','X']],
          [6,6,['YA_ST'  ,'YST','Y']],
          [5,5,['ZA_ST'  ,'ZST','Z']],
          [4,3,['AFS_SEL','FS' ,'F']],
          [2,0,['-'      ,'-'  ,'-']]
          ],True],
    0x1d: ['FF_THR'            ,'OTHER',None,True],
    0x1e: ['FF_DUR'            ,'OTHER',None,True],
    0x1f: ['MOT_THR'           ,'OTHER',None,True],
    0x20: ['MOT_DUR'           ,'OTHER',None,True],
    0x21: ['ZRMOT_THR'         ,'OTHER',None,True],
    0x22: ['ZRMOT_DUR'         ,'OTHER',None,True],
    0x23: ['FIFO_EN'           ,'FIFO' ,None,True],
    0x24: ['I2C_MST_CTRL'      ,'I2C'  ,None,True],
    0x25: ['I2C_SLV0_ADDR'     ,'I2C'  ,None,True],
    0x26: ['I2C_SLV0_REG'      ,'I2C'  ,None,True],
    0x27: ['I2C_SLV0_CTRL'     ,'I2C'  ,None,True],
    0x28: ['I2C_SLV1_ADDR'     ,'I2C'  ,None,True],
    0x29: ['I2C_SLV1_REG'      ,'I2C'  ,None,True],
    0x2a: ['I2C_SLV1_CTRL'     ,'I2C'  ,None,True],
    0x2b: ['I2C_SLV2_ADDR'     ,'I2C'  ,None,True],
    0x2c: ['I2C_SLV2_REG'      ,'I2C'  ,None,True],
    0x2d: ['I2C_SLV2_CTRL'     ,'I2C'  ,None,True],
    0x2e: ['I2C_SLV3_ADDR'     ,'I2C'  ,None,True],
    0x2f: ['I2C_SLV3_REG'      ,'I2C'  ,None,True],
    0x30: ['I2C_SLV3_CTRL'     ,'I2C'  ,None,True],
    0x31: ['I2C_SLV4_ADDR'     ,'I2C'  ,None,True],
    0x32: ['I2C_SLV4_REG'      ,'I2C'  ,None,True],
    0x33: ['I2C_SLV4_DO'       ,'I2C'  ,None,True],
    0x34: ['I2C_SLV4_CTRL'     ,'I2C'  ,None,True],
    0x35: ['I2C_SLV4_DI'       ,'I2C'  ,None,True],
    0x36: ['I2C_MST_STATUS'    ,'I2C'  ,None,True],
    0x37: ['INT_PIN_CFG'       ,'INT'  ,None,True],
    0x38: ['INT_ENABLE'        ,'INT',[
          [7, 7, ['FF_EN'        , 'FF'  , 'F']],
          [6, 6, ['MOT_EN'       , 'MOT' , 'M']],
          [5, 5, ['ZMOT_EN'      , 'ZMOT', 'Z']],
          [4, 4, ['FIFO_OFLOW_EN', 'FIF' , 'F']],
          [3, 3, ['I2C_MST_EN'   , 'I2C' , 'I']],
          [2, 2, ['PLL_RDY_EN'   , 'PLL' , 'P']],
          [1, 1, ['DMP_RDY_EN'   , 'DMP' , 'D']],
          [0, 0, ['DATA_RDY_EN'  , 'DAT' , 'D']]
          ],True],
    0x39: ['DMP_INT_STATUS'    ,'DMP',None,True],
    0x3a: ['INT_STATUS'        ,'INT',[
          [7, 7, ['FF_INT'        , 'FF'  , 'F']],
          [6, 6, ['MOT_INT'       , 'MOT' , 'M']],
          [5, 5, ['ZMOT_INT'      , 'ZMOT', 'Z']],
          [4, 4, ['FIFO_OFLOW_INT', 'FIF' , 'F']],
          [3, 3, ['I2C_MST_INT'   , 'I2C' , 'I']],
          [2, 2, ['PLL_RDY_INT'   , 'PLL' , 'P']],
          [1, 1, ['DMP_RDY_INT'   , 'DMP' , 'D']],
          [0, 0, ['DATA_RDY_INT'  , 'DAT' , 'D']]
          ],True],
    0x3b: ['ACCEL_XOUT_H'      ,'ACCEL'   ,None,True],
    0x3c: ['ACCEL_XOUT_L'      ,'ACCEL'   ,None,True],
    0x3d: ['ACCEL_YOUT_H'      ,'ACCEL'   ,None,True],
    0x3e: ['ACCEL_YOUT_L'      ,'ACCEL'   ,None,True],
    0x3f: ['ACCEL_ZOUT_H'      ,'ACCEL'   ,None,True],
    0x40: ['ACCEL_ZOUT_L'      ,'ACCEL'   ,None,True],
    0x41: ['TEMP_OUT_H'        ,'TEMP'    ,None,True],
    0x42: ['TEMP_OUT_L'        ,'TEMP'    ,None,True],
    0x43: ['GYRO_XOUT_H'       ,'GYRO'    ,None,True],
    0x44: ['GYRO_XOUT_L'       ,'GYRO'    ,None,True],
    0x45: ['GYRO_YOUT_H'       ,'GYRO'    ,None,True],
    0x46: ['GYRO_YOUT_L'       ,'GYRO'    ,None,True],
    0x47: ['GYRO_ZOUT_H'       ,'GYRO'    ,None,True],
    0x48: ['GYRO_ZOUT_L'       ,'GYRO'    ,None,True],
    0x49: ['EXT_SENS_DATA_00'  ,'EXT_SENS',None,True],
    0x4a: ['EXT_SENS_DATA_01'  ,'EXT_SENS',None,True],
    0x4b: ['EXT_SENS_DATA_02'  ,'EXT_SENS',None,True],
    0x4c: ['EXT_SENS_DATA_03'  ,'EXT_SENS',None,True],
    0x4d: ['EXT_SENS_DATA_04'  ,'EXT_SENS',None,True],
    0x4e: ['EXT_SENS_DATA_05'  ,'EXT_SENS',None,True],
    0x4f: ['EXT_SENS_DATA_06'  ,'EXT_SENS',None,True],
    0x50: ['EXT_SENS_DATA_07'  ,'EXT_SENS',None,True],
    0x51: ['EXT_SENS_DATA_08'  ,'EXT_SENS',None,True],
    0x52: ['EXT_SENS_DATA_09'  ,'EXT_SENS',None,True],
    0x53: ['EXT_SENS_DATA_10'  ,'EXT_SENS',None,True],
    0x54: ['EXT_SENS_DATA_11'  ,'EXT_SENS',None,True],
    0x55: ['EXT_SENS_DATA_12'  ,'EXT_SENS',None,True],
    0x56: ['EXT_SENS_DATA_13'  ,'EXT_SENS',None,True],
    0x57: ['EXT_SENS_DATA_14'  ,'EXT_SENS',None,True],
    0x58: ['EXT_SENS_DATA_15'  ,'EXT_SENS',None,True],
    0x59: ['EXT_SENS_DATA_16'  ,'EXT_SENS',None,True],
    0x5a: ['EXT_SENS_DATA_17'  ,'EXT_SENS',None,True],
    0x5b: ['EXT_SENS_DATA_18'  ,'EXT_SENS',None,True],
    0x5c: ['EXT_SENS_DATA_19'  ,'EXT_SENS',None,True],
    0x5d: ['EXT_SENS_DATA_20'  ,'EXT_SENS',None,True],
    0x5e: ['EXT_SENS_DATA_21'  ,'EXT_SENS',None,True],
    0x5f: ['EXT_SENS_DATA_22'  ,'EXT_SENS',None,True],
    0x60: ['EXT_SENS_DATA_23'  ,'EXT_SENS',None,True],
    0x61: ['MOT_DETECT_STATUS' ,'CONFIG'  ,None,True],
    0x63: ['I2C_SLV0_DO'       ,'I2C'     ,None,True],
    0x64: ['I2C_SLV1_DO'       ,'I2C'     ,None,True],
    0x65: ['I2C_SLV2_DO'       ,'I2C'     ,None,True],
    0x66: ['I2C_SLV3_DO'       ,'I2C'     ,None,True],
    0x67: ['I2C_MST_DELAY_CTRL','I2C',[
          [7,7,['DELAY_ES_SHADOW', 'DEL' , 'D']],
          [6,5,['-'              , '-'   , '-']],
          [4,4,['I2C_SLV4_DLY_EN', 'SLV4', '4']],
          [3,3,['I2C_SLV3_DLY_EN', 'SLV3', '3']],
          [2,2,['I2C_SLV2_DLY_EN', 'SLV2', '2']],
          [1,1,['I2C_SLV1_DLY_EN', 'SLV1', '1']],
          [0,0,['I2C_SLV0_DLY_EN', 'SLV0', '0']]
          ],True],
    0x68: ['SIGNAL_PATH_RESET' ,'OTHER',[
          [7,3,['-'              , '-'   , '-']],
          [2,2,['GYRO_RESET' , 'GRS', 'G']],
          [2,2,['ACCEL_RESET', 'ARS', 'A']],
          [0,0,['TEMP_RESET' , 'TRS', 'T']]
          ],True],
    0x69: ['MOT_DETECT_CTRL'   ,'CONFIG',[
          [7,6,['-'             , '-'   , '-']],
          [5,4,['ACCEL_ON_DELAY', 'ADL', 'A']],
          [3,2,['FF_COUNT'      , 'FCT', 'F']],
          [1,0,['MOT_COUNT'     , 'MCT', 'M']]
          ],True],
    0x6a: ['USER_CTRL'         ,'CONFIG',[
          [7,7,['DMP_EN'      , 'DME', 'D']],
          [6,6,['FIFO_EN'     , 'FFE', 'F']],
          [5,5,['I2C_MST_EN'  , 'IME', 'I']],
          [4,4,['I2C_IF_DIS'  , 'IID', 'I']],
          [3,3,['DMP_RES'     , 'DMR', 'D']],
          [2,2,['FIFO_RES'    , 'FFR', 'F']],
          [1,1,['I2C_MST_RES' , 'IMR', 'I']],
          [0,0,['SIG_COND_RES', 'SCR', 'S']]
          ],True],
    0x6b: ['PWR_MGMT_1'        ,'CONFIG',[
          [7,7,['DEVICE_RESET','RES','R']],
          [6,6,['SLEEP'       ,'SLP','S']],
          [5,5,['CYCLE'       ,'CYC','Y']],
          [4,4,['-'           ,'-'  ,'-']],
          [3,3,['TEMP_DIS'    ,'TMP','T']],
          [2,0,['CLKSEL'      ,'CLK','C']]
          ],True],
    0x6c: ['PWR_MGMT_2'        ,'CONFIG',[
          [7,6,['LP_WAKE_CTRL','WARE','W']],
          [5,5,['STBY_XA'     ,'SXA' ,'X']],
          [4,4,['STBY_YA'     ,'SYA' ,'Y']],
          [3,3,['STBY_ZA'     ,'SZA' ,'Z']],
          [2,2,['STBY_XG'     ,'SXG' ,'X']],
          [1,1,['STBY_YG'     ,'SYG' ,'Y']],
          [0,0,['STBY_ZG'     ,'SZG' ,'Z']]
          ],True],
    0x6d: ['BANK_SEL'          ,'PROG_MEMORY',None,True],
    0x6e: ['MEM_START_ADDR'    ,'PROG_MEMORY',None,True],
    0x6f: ['MEM_R_W'           ,'PROG_MEMORY',None,False],
    0x70: ['DMP_CFG_1'         ,'DMP'        ,None,True],
    0x71: ['DMP_CFG_2'         ,'DMP'        ,None,True],
    0x72: ['FIFO_COUNTH'       ,'FIFO'       ,None,True],
    0x73: ['FIFO_COUNTL'       ,'FIFO'       ,None,True],
    0x74: ['FIFO_R_W'          ,'FIFO'       ,None,False],
    0x75: ['WHO_AM_I'          ,'CONFIG',[
          [7,7,['-'            ,'-'  ,'-']],
          [5,1,['WHO_AM_I'     ,'ID'  ,'I']],
          [0,0,['-'            ,'-' ,'-']]
          ],False]
    }

_bit_mask = (0b00000001, #0
             0b00000011, #1
             0b00000111, #2
             0b00001111, #3
             0b00011111, #4
             0b00111111, #5
             0b01111111, #6
             0b11111111  #7
             )


class Mpu6050Packet:

    class Data:
        def __init__(self,reg,data,addr):
            self.Reg  = reg
            self.Data = data
            self.Address = addr

    def __init__(self):
        self.__pmBankNumber = 0
        self.__pmBankAddress = 0
        self.clear()

    def clear(self):
        self.__startReg = 256
        self.__currentReg = 256
        self.__ioDirection = 'WRITE'
        self.__ioType      = 'REG'
        self.__data = []
        self.__startPacketSample = 0
        self.__emdPacketSample = 0
        self.__warningString = ''
        self.__lastRegister=256
        self.__lastRegisterFormat = None

    def setDirection(self, dir):
        self.__ioDirection = dir

    def direction(self):
        return self.__ioDirection

    def ioType(self):
        return self.__ioType

    def setStartSample(self, ss):
        self.__startPacketSample = ss

    def startSample(self):
        return self.__startPacketSample

    def setEndSample(self, es):
        self.__emdPacketSample = es

    def endSample(self):
        return self.__emdPacketSample

    def warning(self):
        return self.__warningString

    def isWarning(self):
        return len(self.__warningString)>0

    def __getRegisterData(self, reg):
        if reg==self.__lastRegister: return self.__lastRegisterFormat
        self.__lastRegister=reg
        if reg is not None:
            self.__lastRegisterFormat = _reg_names.get(reg)
        else:
            self.__lastRegisterFormat = None
        return self.__lastRegisterFormat

    def setRegister(self, reg):
        reg = reg & 0xFF
        val = self.__getRegisterData(reg)
        if val is None:
            self.__addWarning("Unknown registry number %02x" % reg)
        if self.__startReg>255: self.__startReg = reg
        self.__currentReg = reg

    def startRegister(self):
        return self.__startReg

    def currentRegister(self):
        return self.__currentReg

    def registerName(self,reg=None):
        if reg is None:
            if len(self.__data)>0: reg = self.__data[-1].Reg
            else:                  reg = self.__currentReg
        val = self.__getRegisterData(reg)
        if val is not None: return val[0]
        return "REG " + self.__byteToHexString(self.__currentReg)

    def registerType(self,reg=None):
        if reg is None:
            if len(self.__data)>0: reg = self.__data[-1].Reg
            else:                  reg = self.__currentReg
        val = self.__getRegisterData(reg)
        if val is not None: return val[1]
        return "???"

    def bitNames(self):
        if self.__currentReg is not None and len(self.__data)>0:
            data = self.__data[-1]
            val = self.__getRegisterData(data.Reg)
            if val is not None and val[2] is not None:
                return val[2]
            else:
                return [[7,0,['0x' + self.__byteToHexString(data.Data)]]]
        return [[7,0,['????']]]

    def addData(self, byte):
        if self.__currentReg == 0x6f: #MEM_R_W
            if self.__pmBankAddress>0xFF:
                self.__addWarning("Going beyond the boundaries of the memory bank.")
                self.__pmBankAddress = self.__pmBankAddress & 0xFF

        self.__data.append(self.Data(self.__currentReg,byte,self.__pmBankNumber*256 + self.__pmBankAddress))

        old_reg = _reg_names.get(self.__currentReg)
        r_name,r_type,r_bits,r_incr = ('','','',False)
        if old_reg is not None:
            r_name,r_type,r_bits,r_incr = old_reg
        if self.__currentReg   == 0x6d: #BANK_SEL
            self.__pmBankNumber = byte
        elif self.__currentReg == 0x6e: #MEM_START_ADDR
            self.__pmBankAddress = byte
        elif self.__currentReg == 0x6f: #MEM_R_W
            self.__pmBankAddress+=1
            self.__ioType      = 'MEMORY'

        if r_incr:
            self.__currentReg+=1
            new_reg = _reg_names.get(self.__currentReg)
            if new_reg is None:
                self.__addWarning("Unknown registry number " + self.__byteToHexString(reg))
            else:
                if len(self.__data)>1 and r_incr!=new_reg[3]:
                    self.__addWarning("There may be an error when processing the sequence.")


    def lastData(self):
        if len(self.__data)>0:
            return self.__data[-1]
        else:
            return None

    def __addWarning(self, warn_string):
        self.__warningString = warn_string
        # if len(self.__warningString)<=0:
        #     self.__warningString = warn_string
        # else:
        #     self.__warningString = self.__warningString + ', ' + warn_string

    def __byteToHexString(self, byte):
        ret = '%02x' % byte
        return ret.upper()

    '''
    Возвращает человеческое представленние пакета
    '''
    def humanString(self):
        ret = ''
        if len(self.__data)<=0: return '???'
        if self.__ioDirection=="READ": ret = "Read "
        else:                          ret = "Write "
        if len(self.__data)==1:
            return ret +  self.registerHumanString(self.__data[0])
        else:
            for data in self.__data:
                ret = ret + self.registerHumanString(data)
            return ret

    def registerHumanString(self,data):
        val = _reg_names.get(data.Reg)
        ret = self.__byteToHexString(data.Reg)
        if val is not None:
            return val[0] + ': ' + self.__bitHumanString(data.Data,val[2]) + ' '
        return self.__byteToHexString(data.Reg) + ': ' + self.__byteToHexString(data.Data) + ' '


    def __bitHumanString(self,data,bits):
        if bits is None:
            return self.__byteToHexString(data)
        ret = ''
        for format_string in bits:
            # [7,7,['DEVICE_RESET','RES','R']]
            start, end,names = format_string
            if names[0]!='-':
                if len(ret)>0: ret = ret + ', '
                bit = data >> end
                bit_count = start - end
                bit = bit & _bit_mask[bit_count & 0x7]
                ret = ret + names[0].rstrip().lstrip() + ': %d'%bit
        return ret
