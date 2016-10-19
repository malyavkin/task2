import platform
import os


def ping(hostname, times):
    pl = platform.system()
    # assume every platform other than Windows uses -c for ping count
    count_arg = '-n' if pl == 'Windows' else '-c'
    cmd = " ".join(['ping', count_arg, str(times), hostname])
    result = os.system(cmd)
    return result
