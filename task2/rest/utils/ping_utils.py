import platform
import os
import subprocess

def ping(hostname, times):
    """
    pings given hostname given # of times and returns cmd output
    :param hostname: hostname to ping
    :param times: #of times to ping
    :return:
    """
    pl = platform.system()
    # assume every platform other than Windows uses -c for ping count
    count_arg = '-n' if pl == 'Windows' else '-c'
    proc = subprocess.Popen(["ping", count_arg, str(times), hostname], stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    return out