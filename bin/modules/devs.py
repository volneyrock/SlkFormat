import subprocess

def devs():
    devices =  subprocess.check_output(['cat','/proc/partitions']).split('\n')
    return devices

if __name__ == '__main__':
 	d = devs()
 	for i in d:
 		print i[-4:]
