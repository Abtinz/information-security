import argparse
from ip_scanner import scanner

def main():
    parser = argparse.ArgumentParser(description='IP Scanner TurboV.2000')
    parser.add_argument("--ipscan", action="store_true", help="Ip scanning", required=False)
    parser.add_argument("-ip", required=False, help="starting and ending range of ip", nargs=2)
    parser.add_argument("-portscan", action="store_true", help="Port scanning", required=False)
    parser.add_argument("-m", type=int, help="Subnet mask", required=False)
    parser.add_argument("-tcp", required=False, nargs=2, type=int)
    parser.add_argument("-udp", required=False, nargs=2, type=int)
    args = parser.parse_args()
    if args.ipscan:
            
            scanner(
                  start_ip =args.ip[0], 
                  end_ip = args.ip[1],
                  address_counts = 2 ** (32 - args.m)
            )
    
main()
