from asyncio.windows_events import NULL
from tabnanny import check
import pyfiglet
import sys
import socket
from datetime import datetime
import ipaddress 


def generate_banner(text):
    ascii_banner = pyfiglet.figlet_format(text.upper())
    print(ascii_banner)

def validate_ip_address(address):
    try:
        ip = ipaddress.ip_address(address)
        print("\nIP address {} is valid. The object returned is {}".format(address, ip))
    except ValueError:
        print("\nIP address {} is not valid".format(address))

def check_int(str):
    if str.isdigit():
        return True
    return False

def validate_port_range():
    global start, end

    if int(start) >= int(end):
        temp = start
        start = end
        end = temp
    

def scan_ports() :
    target = input("\nEnter target example 192.168.1.108:")
    validate_ip_address(target)
    can_input_port = True

    while can_input_port:
        global start, end
        
        start = input("\nEnter starting port example 0:")
        end = input("\nEnter ending port example 100:")

        if check_int(start) and check_int(end):
            can_input_port = False

    validate_port_range()

    print("-" * 50)
    print("Scanning Target: " + str(target))
    print("Scanning started at: " + str(datetime.now()))
    print("-" * 50)
  
    try:
     
        for port in range(int(start), int(end)):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            result = s.connect_ex((target, port))
            if result == 0:
                print("Port {} is open".format(port))
            s.close()
         
    except KeyboardInterrupt:
        print("\nExiting Program !!!!")
        sys.exit()
    except socket.gaierror:
        print("\nHostname Could Not Be Resolved !!!!")
        sys.exit()
    except socket.error:
        print("\nServer not responding !!!!")
        sys.exit()

    print("Scanning ended at:" + str(datetime.now()))
    print("-" * 50)

def port_scanning_app():
    generate_banner("port analyser")
    scan_ports()

port_scanning_app()
