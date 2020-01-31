#!/usr/bin/python3


"""
compteur interne dans un cyber cafe
Author: jerry harim
Date de creation : Jol 22 14:14:10 2018
"""

import time 
import os
import sys


TARIF = 0 # en Arirary

CURDATE = time.strftime("%Y-%m-%d")
BEGIN = time.strftime("%H:%M:%S")
END = time.strftime("%H:%M:%S")
DURATION = 0 # in s
NET_A_PAYER = 0

LOG_FILE = "cyberCounter.log"


def backup():
    """ backup last session to a Log file """

    # begin(AAAA-MM-DD:HH-MM), duration(h,m,s), net-a-payer

    curDate = time.strftime("%Y/%m/%d")
    duration = time.strftime("%H:%M:%S", time.gmtime(DURATION))
    with open(LOG_FILE, 'w') as log:
        log.write("Last session ")
        log.write("Date : %s\n" % curDate)
        log.write("Begin : %s\n" % BEGIN)
        log.write("End : %s\n" % END)
        log.write("Tarif : %sAr/Min\n" % TARIF)
        log.write("Duration : %s\n" % duration)
        log.write("Net a payer : %sAr\n" % NET_A_PAYER)

def refresh_screen():
    """ Interface , time to refresh : 1s """

    os.system("clear")

    print("Tarif : %sAr/Minute" % TARIF)
    print("Begin : %s" % BEGIN)
    print("-------------------")

    fDuration = time.strftime("%H:%M:%S", time.gmtime(DURATION))
    print("Duration : %s" % fDuration)
    print("Net a payer : %sAr" % NET_A_PAYER)


def compteur():
    """ gestion compteur : compte le nombre de minute """

    global DURATION
    global NET_A_PAYER 
    global END 

    time.sleep(1)
    DURATION += 1
    NET_A_PAYER = round(TARIF * (DURATION / 60))
    END = time.strftime("%H:%M:%S")
    
    # save to log file each minute
    if (DURATION % 2 == 0):
        backup()


def checkArg():
    """ check if argument is corrent """

    global TARIF    

    # request tarif if argument 1 missed 
    try:
        TARIF = sys.argv[1]
    except IndexError:
        TARIF = input("Tarif (Ar/Min) : ")

    # verification
    while True:
        try:
            TARIF = (int)(TARIF)
            if ( TARIF <= 0 ):
                raise ValueError()
            break

        except ValueError:
            print("Please use positif value")
            TARIF = input("Tarif (Ar/Min): ")

    return True

def main():
    checkArg()

    while(True):
        refresh_screen()
        compteur()

main()
