import os
max_value=int(input("enter the charge threshold for your laptops battery(in %):\t"))
if(max_value<100 and max_value>0):
    p=os.system(f'echo {max_value} |sudo tee /sys/class/power_supply/BAT0/charge_control_end_threshold')
else:
    print('Invalid input')