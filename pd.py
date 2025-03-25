##
## This file is part of the libsigrokdecode project.
##
## Copyright (C) 2012-2014 Uwe Hermann <uwe@hermann-uwe.de>
## Copyright (C) 2013 Matt Ranostay <mranostay@gmail.com>
##
## This program is free software; you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation; either version 2 of the License, or
## (at your option) any later version.
##
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with this program; if not, see <http://www.gnu.org/licenses/>.
##

import re
import sigrokdecode as srd
from common.srdhelper import bcd2int
from .packet import Mpu6050Packet


MPU6050_I2C_ADDRESS = (0x68,0x68+1)

ann_reg_read, ann_reg_write, ann_pm_read, ann_pm_write, ann_accel, ann_gyro, ann_temp, ann_fifo, ann_i2c, ann_ext_sens, ann_interrupt, ann_config, ann_dmp, ann_prog_memory, ann_other_subsystem, ann_warning = range(16)

def subSytemNameToAnn(name):
    if name=='ACCEL'      : return ann_accel
    if name=='GYRO'       : return ann_gyro
    if name=='TEMP'       : return ann_temp
    if name=='FIFO'       : return ann_fifo
    if name=='I2C'        : return ann_i2c
    if name=='EXT_SENS'   : return ann_ext_sens
    if name=='DMP'        : return ann_dmp
    if name=='INT'        : return ann_interrupt
    if name=='CONFIG'     : return ann_config
    if name=='PROG_MEMORY': return ann_prog_memory
    return ann_other_subsystem


class Decoder(srd.Decoder):
    api_version = 3
    id = 'mpu6050'
    name = 'MPU6050'
    longname = 'InvenSense MPU6050'
    desc = 'Accelerometer module protocol.'
    license = 'gplv2+'
    inputs = ['i2c']
    outputs = ['mpu6050']
    annotations =(
        #Type
        ('reg-read'      , 'Read register'       ) , # 0
        ('reg-write'     , 'Write register'      ) , # 1
        ('prog-mem-read' , 'Read program memory' ) , # 2
        ('prog-mem-write', 'Write program memory') , # 3
        #Subsystem
        ('accel'         , 'Accelerometer'       ) , # 4
        ('gyro'          , 'Gyroscope'           ) , # 5
        ('temp'          , 'Temperature'         ) , # 6
        ('fifo'          , 'Fifo'                ) , # 7
        ('i2c'           , 'I2C'                 ) , # 8
        ('ext_sens'      , 'External sensor'     ) , # 9
        ('interrupt'     , 'Interrupt'           ) , # 10
        ('config'        , 'Configuration'       ) , # 11
        ('dmp'           , 'DMP'                 ) , # 12
        ('prog-memory'   , 'Programm memory'     ) , # 13
        ('unknown'       , 'Other'               ) , # 14
        #---
        ('warnings'      , 'Warnings'            ) , # 15
    )
    annotation_rows = (
        ('submodule'    , 'Submodule', (ann_accel, ann_gyro, ann_temp, ann_fifo, ann_i2c, ann_ext_sens, ann_dmp, ann_interrupt, ann_config, ann_prog_memory, ann_other_subsystem)),
        ('operation'    , 'Operation', (ann_reg_read, ann_reg_write, ann_pm_read, ann_pm_write)),
        ('warnings'     , 'Warnings' , (ann_warning,)),
    )

    def __init__(self):
        self.reset()

    def reset(self):
        self.state = 'IDLE'
        self.packet = Mpu6050Packet();
        self.packet.clear()
        self.bits = []

    def start(self):
        self.out_ann = self.register(srd.OUTPUT_ANN)

    def putx(self, data):
        self.put(self.ss, self.es, self.out_ann, data)

    def putd(self, bit1, bit2, data):
        self.put(self.bits[bit1][1], self.bits[bit2][2], self.out_ann, data)

    def showReg(self):#my_code
        reg = self.packet.startRegister()
        self.putd(7, 0, [subSytemNameToAnn(self.packet.registerType(reg)),[self.packet.registerName(reg)]])

    def showRegBits(self):#my_code
        bits = self.packet.bitNames()
        for bit in bits:
            start, stop, string = bit
            self.putd(start, stop, [subSytemNameToAnn(self.packet.registerType()),string])

    def showPacket(self):#my_code
        if self.packet.isWarning():
            self.put(self.packet.startSample(), self.packet.endSample(), self.out_ann,[ann_warning,[self.packet.warning()]])

        if self.packet.ioType()=="REG":
            if self.packet.direction()=="READ": atype = ann_reg_read
            else:                               atype = ann_reg_write
        else:
            if self.packet.direction()=="READ": atype = ann_pm_read
            else:                               atype = ann_pm_write

        self.put(self.packet.startSample(), self.packet.endSample(), self.out_ann, [atype,[self.packet.humanString()]])

    def is_correct_chip(self, addr):
        print('is_correct_chip ', hex(addr))
        if addr in MPU6050_I2C_ADDRESS:
            return True
        self.put(self.ss_block, self.es, self.out_ann,
                 [28, ['Ignoring non-MPU6050 data (slave 0x%02X)' % addr]])
        return False

    def decode(self, ss, es, data):
        cmd, databyte = data

        # Store the start/end samples of this I²C packet.
        self.ss, self.es = ss, es
        self.packet.setEndSample(es)

        # Collect the 'BITS' packet, then return. The next packet is
        # guaranteed to belong to these bits we just stored.
        if cmd == 'BITS':
            self.bits = databyte
            print(self.state, cmd, [[hex(item) for item in group] for group in databyte])
            return
        elif cmd == 'STOP':#my_code
            self.showPacket()#my_code

        databyte_hex = None
        if databyte:
            databyte_hex = hex(databyte)

        print(self.state, cmd, databyte_hex)

        # State machine.
        if self.state == 'IDLE':
            # Wait for an I²C START condition.
            if cmd != 'START':
                return
            self.state = 'GET SLAVE ADDR'
            self.packet.clear()
            self.packet.setStartSample(ss)

        elif self.state == 'GET SLAVE ADDR':
            if cmd != 'ADDRESS WRITE' and cmd != 'ADDRESS READ':
                return
            if not self.is_correct_chip(databyte):
                self.state = 'IDLE'
                return
            self.state = 'GET REG ADDR'

        elif self.state == 'GET REG ADDR':
            if cmd == 'START REPEAT':
                self.state = 'GET SLAVE ADDR'
            elif cmd == 'STOP':
                self.state = 'IDLE'

            elif cmd == 'DATA WRITE':
                self.packet.setRegister(databyte)
                self.showReg()
                self.state = 'WRITE REGS'
            elif cmd == 'DATA READ':
                self.packet.setDirection("READ")
                self.packet.addData(databyte)
                self.showRegBits()

        elif self.state == 'WRITE REGS':
            if cmd == 'STOP':
                self.state = 'IDLE'
                return
            elif cmd == 'START REPEAT':
                self.state = 'GET SLAVE ADDR'
                return
            if databyte is not None:
                self.packet.addData(databyte)
                self.packet.setDirection("WRITE")
                self.showRegBits()
