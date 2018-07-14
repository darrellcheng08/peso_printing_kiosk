import subprocess

cmd = 'sudo hciconfig hci0 piscan'
subprocess.check_output(cmd, shell=True)