import socket

def scan_ports(start_port, end_port, protocol_mode):
    with open('active_list.txt', 'r') as file:
        alive_devices = file.read().splitlines()
        socket_type = socket.SOCK_STREAM if protocol_mode == "tcp" else socket.SOCK_DGRAM
        print("Start Scanning")

        with open(protocol_mode + '_scan_result.txt', 'a') as file:
            for target in alive_devices:
                for port in range(start_port, end_port + 1):
                    sock = socket.socket(socket.AF_INET, socket_type)
                    sock.settimeout(1)
                    result = sock.connect_ex((target, port))
                    if result == 0:
                        print(protocol_mode + " Port " + str(port) + " for " + str(target) + " is open" + '\t------------>\t' + get_service_name(port, protocol_mode) + '\n')
                        file.write(
                            protocol_mode + " Port " + str(port) + " for " + str(target) + " is open" + '\t------------>\t' + get_service_name(port, protocol_mode) + '\n')
                    else:
                        print(protocol_mode + " Port " + str(port) + " for " + str(target) + " is closed\n")
                        file.write(protocol_mode + " Port " + str(port) + " for " + str(target) + " is closed\n")
                    sock.close()
    


def get_service_name(port, protocol):
    try:
        service = socket.getservbyport(port, protocol.lower())
        return service
    except OSError:
        return "Can not get service name"