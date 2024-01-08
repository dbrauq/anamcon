# -------------------------------
# This file is part of AnamCon
# by David Brau Queralt
# -------------------------------

from subprocess import (run,
                        Popen, 
                        PIPE)

def run_blocking_command(command):
    result = run(command, shell=True, text=True, stdout=PIPE, stderr=PIPE)
    return (result.stdout, result.stderr)

def run_nonblocking_command(command):
    process = Popen(command, shell=True, text=True, stdout=PIPE, stderr=PIPE)
    stdout, stderr = process.communicate()
    return (stdout, stderr)