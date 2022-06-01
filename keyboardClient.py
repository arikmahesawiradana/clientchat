#!/usr/bin/env python

import socket
import keyboard
import time

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
IP = "localhost"
PORT = 9979
client.connect((IP, PORT))

kembali = 0

def mengirimPesan(message):
    pesan = message
    pesan.encode('utf-8')
    client.send(pesan)
    print("pesan" + pesan + "terkirim")

def keyboardlisten():
    if keyboard.is_pressed('a'):
        mengirimPesan("maju")
        print("a is presseed")
        time.sleep(0.5)
    elif keyboard.is_pressed('s'):
        mengirimPesan("mundur")
        print("s is pressed")
        time.sleep(0.5)
    elif keyboard.is_pressed('x'):
        global kembali
        kembali = 1

if __name__ == '__main__':
    print("tekan a maju")
    print("tekan s mundur")
    while True:
        try:
            keyboardlisten()
            if kembali == 1:
                break
        except:
            break