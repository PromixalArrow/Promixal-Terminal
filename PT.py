import subprocess
import platform
import socket
import time
import os

path = 'C:/'
host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
print("Promixal Terminal\nV.0.1\nType help To Help.")
while True:
    code = input(">>> ")
    if code == 'ping':
        host = input("Enter Website To Ping: ")
        number = input("Enter How Many Times To Ping: ")
        
        def ping(host):
            param = '-n' if platform.system().lower() == 'windows' else '-c'
            command = ['ping', param, number, host]
            return subprocess.call(command)
        print(ping(host))
    if code == 'local':
        print("Your Local IPS is: ", host_ip)
        print("Your Desktop Name Is: ", host_name)
    if code == 'date':
        print("The Local Date is: ", time.strftime("%d/%m/%Y"))
    if code == 'list':
        dir_list = os.listdir(path)
        print("Files and Directorys in ", path, "' :")
        print(dir_list)
    if code == 'list -a':
        file = input("Enter The Direct File Path To Read: ")
        dir_list2 = os.listdir(file)
        print("Files and Directorys in ", file, "' :")
        print(dir_list2)
    if code == "echo me":
        echo = input("What Do You Want Me To Echo: ")
        print(echo)
    if code == "what are you":
        print("I am a terminal with a custom command language!")
    if code == "who created you":
        print("PromixalArrow42! I love him!")
    if code == "help":
        print("To Use Me Make Some Code")
        print("These Are My Commands!\nping: Will Ping A Website Of Your Choice\nlocal: Will Tell You Your IPS And Device Name\ndate: Will Tell You The Date\nlist: Will List Folders In C Drive\nlist -a: Will List Files In Any Directory\necho me: Will Echo You\nwhat are you: Will Tell You What I Am\nwho created you: Will Tell You Who Created Me\nhelp: Will Help With Commands.")
