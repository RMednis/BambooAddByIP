#!/usr/bin/env python3

# Script to send printer information to BambuStudio
# Based off a similar shell script available here:
# https://github.com/gashton/bambustudio_tools/blob/master/bambudiscovery.sh

import socket
import datetime
import time
import config
import subprocess


def send_magic_packet():
    response = (
        f"HTTP/1.1 200 OK\r\n"
        f"Server: Buildroot/2018.02-rc3 UPnP/1.0 ssdpd/1.8\r\n"
        f"Date: {datetime.datetime.now()}\r\n"
        f"Location: {config.PRINTER_IP}\r\n"
        f"ST: urn:bambulab-com:device:3dprinter:1\r\n"
        f"EXT:\r\n"
        f"USN: {config.PRINTER_USN}\r\n"
        f"Cache-Control: max-age=1800\r\n"
        f"DevModel.bambu.com: {config.PRINTER_DEV_MODEL}\r\n"
        f"DevName.bambu.com: {config.PRINTER_DEV_NAME}\r\n"
        f"DevSignal.bambu.com: {config.PRINTER_DEV_SIGNAL}\r\n"
        f"DevConnect.bambu.com: {config.PRINTER_DEV_CONNECT}\r\n"
        f"DevBind.bambu.com: {config.PRINTER_DEV_BIND}\r\n"
        f"\r\n"
    )

    clientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    clientSocket.sendto(str.encode(response), (config.TARGET_IP, 2021))
    print("Magic Packet Sent")


if config.RUN_BSTUDIO:
    print("Launching BambuStudio")
    try:
        subprocess.Popen(config.BSTUDIO_PATH)
    except FileNotFoundError:
        print("Could not find BambuStudio executable!")


    time.sleep(config.WAIT_TIME)
    send_magic_packet()

else:
    send_magic_packet()
