#!/usr/bin/env python
import os
import subprocess
from time import sleep

class actor_process:
    pid = ''
    mem = 0

    def kill(self):
        print self.pid
        subprocess.call(["kill", "-9" , self.pid])
        sleep(1)


def get_proc_id_n_mem(process_line):
    fields = process_line.split(" ")
    fields = [field for field in fields if field != ""]
    return fields[1], float(fields[3])

def test_actor_status():
    daemon = actor_process()
    config = actor_process()

    a = subprocess.check_output(["ps", "aux"]).splitlines()
    for pross in a:
        if "atp-actors" not in pross or "config" not in pross:
            continue
        if "daemon" in pross:
            daemon.pid, daemon.mem = get_proc_id_n_mem(pross)
        elif "config" in pross:
            config.pid, config.mem = get_proc_id_n_mem(pross)

    print "config({} {})".format(config.pid, config.mem)
    if config.mem > 85.0:
        print 'Kill Config'
        daemon.kill()
        config.kill()
        subprocess.call(["atpctl", "stop"])
        sleep(7)
        subprocess.call(["atpctl", "start"])

    del daemon
    del config

def run_main_program():
    while True:
        test_actor_status()
        sleep(60)

if __name__ == "__main__":
    run_main_program()