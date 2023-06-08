import subprocess
import chardet

hosts = ['yandex.ru', 'youtube.com', ]
LINE_COUNT = 3


def subproc_pings(*args) -> None:
    for host in args:
        line_count = 0
        subproc_ping = subprocess.Popen(args=('ping', host), stdout=subprocess.PIPE)
        for line in subproc_ping.stdout:
            line_count += 1
            result = chardet.detect(line)
            line = line.decode(result['encoding']).encode('utf-8')
            print(line.decode('utf-8'))

            if line_count > LINE_COUNT:
                subproc_ping.terminate()


subproc_pings(*hosts)

#
# PING yandex.ru (77.88.55.88) 56(84) bytes of data.
#
# 64 bytes from yandex.ru (77.88.55.88): icmp_seq=1 ttl=248 time=59.4 ms
#
# 64 bytes from yandex.ru (77.88.55.88): icmp_seq=2 ttl=248 time=57.8 ms
#
# 64 bytes from yandex.ru (77.88.55.88): icmp_seq=3 ttl=248 time=55.7 ms
#
# PING youtube.com (64.233.164.91) 56(84) bytes of data.
#
# 64 bytes from lf-in-f91.1e100.net (64.233.164.91): icmp_seq=1 ttl=60 time=61.3 ms
#
# 64 bytes from lf-in-f91.1e100.net (64.233.164.91): icmp_seq=2 ttl=60 time=60.3 ms
#
# 64 bytes from lf-in-f91.1e100.net (64.233.164.91): icmp_seq=3 ttl=60 time=62.1 ms
#
#
# Process finished with exit code 0