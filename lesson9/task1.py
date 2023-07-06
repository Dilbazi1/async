import os
from ipaddress import ip_address
from socket import gethostbyname

from tabulate import tabulate


def host_ping(hosts, output=True):
    reachable = []
    unreachable = []
    for item in hosts:
        if isinstance(item, (str, bytes, bytearray)):
            item = ip_address(gethostbyname(item))

        response = os.system(f"ping -n 1 {item} > ping.log")
        if response == 0:
            reachable.append(item)
        else:
            unreachable.append(item)
    if output:
        for item in reachable:
            print(f"{item} Узел доступен")
        for item in unreachable:
            print(f"{item} Узел недоступен")
    return {'reachable': reachable, 'unreachable': unreachable}


def host_range_ping(start_ip, stop_ip, output=True):
    start, stop = map(lambda x: int(
        ip_address(gethostbyname(x))), (start_ip, stop_ip))

    if (stop - start) + start % 256 > 255:
        print('Меняется только последний октет')
        return
    ip_addr = ip_address(gethostbyname(start_ip))
    hosts = [ip_addr + i for i in range(stop - start + 1)]
    return host_ping(hosts, output=output)


def host_range_ping_tab(start_ip, stop_ip):
    print(tabulate(host_range_ping(start_ip, stop_ip, output=False), headers='keys',
                   tablefmt="pipe",
                   stralign="center", ))


hosts = ['192.168.0.1', '192.168.0.8', 'google.com', 'mail.ru']

print(host_ping(hosts))
print(host_range_ping('5.255.255.70', '5.255.255.80'))
print(host_range_ping_tab('5.255.255.70', '5.255.255.80'))