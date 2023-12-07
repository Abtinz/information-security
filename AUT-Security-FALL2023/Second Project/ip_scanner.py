import ipaddress
from icmplib import ping
import pickle


def ip_scanner(start_ip, end_ip):
    '''
        this function will get starting and ending range of scanning ip for 
        checking if they are alive or not and will save them is their result files...
        params:
           start_ip -> this ip will show starting range of scanning process 
           end_ip -> this ip will show ending range of scanning process 
    '''

    print("IP Scanning process is started")   

    #finding the starting and ending ip addresses
    start, end = int(ipaddress.IPv6Address(start_ip)), int(ipaddress.IPv6Address(end_ip))
    ip_range = [str(ipaddress.IPv6Address(ip)) for ip in range(start, end + 1)]

    #we will need this classes for saving ip scanning results
    alive_devices = []
    not_alive_devices = []
    with open('scanner_result.txt', 'a') as file:
    
        for ip in ip_range:
            
            #checking that if ip is alive or not
            is_current_ip_alive = ping(ip = ip, count=2, interval=0.1).is_alive

            if is_current_ip_alive:                
                print(f"alive IP:{str(ip)} ...")
                file.write(f"alive IP:{str(ip)} ...")
                alive_devices.append(ip)
            else:
                print(f"not alive IP:{str(ip)} ...")
                file.write(f"not alive IP:{str(ip)} ...")
                not_alive_devices.append(ip)

    
    with open('alive_list.txt', 'a') as file:
        for ip in alive_devices:
            file.write(str(ip))

     
    with open('not_alive_list.txt', 'a') as file:
        for ip in not_alive_devices:
            file.write(str(ip))
    
    print("IP Scanning process is finished")   
