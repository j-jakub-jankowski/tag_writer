import ctypes
import os
import time

os.add_dll_directory(__file__)

mydll = ctypes.windll.LoadLibrary('./USB_UHFReader.dll')


def open_reader():
    """open connection with reader, must be done before other functions"""
    open_ = mydll.API_OpenUsb()
    if open_ != 1:
        print('Connection established')
    else:
        print('Reconnect reader and try again')


def close_reader():
    close_ = mydll.API_CloseUsb()
    if close_ != 1:
        pass
    else:
        pass


def read_tag_hex():
    """read tag and return in hex"""
    while True:
        uLen = ctypes.c_ubyte()
        uReadData = bytes(6)
        read_tag_hex = mydll.API_InventoryOnce
        read_ = read_tag_hex(uReadData, ctypes.byref(uLen))
        if read_ == 0:
            tag_hex = uReadData.hex()
            print(tag_hex)
            return tag_hex


def read_tag_int():
    """read tag, get hex value and transform to decimal
    max value """
    tag_hex = read_tag_hex()
    tag_int = int(tag_hex[8:12], 16)
    return tag_int


def enable_tag(epc):
    """set first EPC bytes to 14, allow reading by chrono device"""
    btAryPwd = bytes(4)
    epcLen = 6
    btMemBank = 1
    btWordAdd = 1
    btWordCnt = 1
    uReadData_list = [20, 0]
    uReadData = bytes(uReadData_list)
    while True:
        save_tag_ = mydll.API_WriteData(btAryPwd, epcLen, epc, btMemBank, btWordAdd, btWordCnt, uReadData)
        if save_tag_ == 0:
            print('Enabled')
            break
        else:
            print('Try Enable')
            time.sleep(0.3)


def save_tag(bib):
    """transform integer bib to hex value and save in EPC memory, enable reading,
    actually max value 65535 - FFFF"""
    tag_hex = read_tag_hex()
    btAryPwd = bytes(4)
    epcLen = 6
    epc = tag_hex
    btMemBank = 1
    btWordAdd = 2
    btWordCnt = 2
    uReadData = bib.to_bytes(btWordCnt * 2, byteorder='big')
    enable_tag(epc)
    while True:
        save_tag_ = mydll.API_WriteData(btAryPwd, epcLen, epc, btMemBank, btWordAdd, btWordCnt, uReadData)
        if save_tag_ == 0:
            print('Save')
            break
        else:
            print('Try Save')
            time.sleep(0.3)


def save_tag_and_check(bib):
    """saving with validation
    read -> enable -> save -> read -> check"""
    save_tag(bib)
    time.sleep(0.5)
    tag_int = read_tag_int()
    if bib == tag_int:
        print('Success')
