import argparse
import ip_scanner

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
            ip_scanner(
                  start =args.ip[0], 
                  end = args.ip[1]
            )
    if args.portscan:
        if args.tcp is not None:
                mode = "tcp"
                start = args.tcp[0]
                end = args.tcp[1]
                scan_ports(start, end, mode)
        elif args.udp is not None:
                mode = "udp"
                start = args.udp[0]
                end = args.udp[1]
                scan_ports(start, end, mode)
