#!/usr/bin/python3

# ansible managed
# ansibleguy.infra_mariadb

from sys import argv as sys_argv
from sys import exit as sys_exit
from subprocess import Popen as subprocess_popen
from subprocess import PIPE as subprocess_pipe

CMD_CONFIG = "grep -rscq %s %s"
CMD_LISTEN = "lsof -i -P -n | grep LISTEN | grep -cq ':%s'"


def check(cmd: str) -> bool:
    process = subprocess_popen(
        cmd,
        shell=True,
        stdout=subprocess_pipe,
        stderr=subprocess_pipe
    )
    process.communicate()

    if process.returncode == 0:
        return True

    return False


INSTANCE_PATH = sys_argv[1]
try:
    port = sys_argv[2]
    if check(CMD_CONFIG % (port, INSTANCE_PATH)) and check(CMD_LISTEN % port):
        print(1)

    else:
        print(0)

except IndexError:
    for i in range(3306, 3399):
        if not check(CMD_CONFIG % (i, INSTANCE_PATH)) and not \
                check(CMD_LISTEN % i):
            print(i)
            sys_exit(0)
