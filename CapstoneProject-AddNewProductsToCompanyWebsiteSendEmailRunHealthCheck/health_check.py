#!/usr/bin/env python3

import sys
import os
import shutil
import psutil
import socket
import emails


# Healthy if cpu_usage < 80%
def check_cpu_usage():
    usage = psutil.cpu_percent(1)            
    #usage = 82              # Testing
    if usage > 80:
        cpu_usage_alert = "Error - CPU usage is over 80% - " + str(usage)
        return cpu_usage_alert
    else:
        return


# Return True if > 20% free, False if less
def check_disk_usage():
    d_usage = shutil.disk_usage('/')                        # disk_usage return: 0=total,1=used,2=free
    d_free_pct = int((d_usage[2]/d_usage[0])*100)
    #d_free_pct = 19     # Testing
    if d_free_pct < 20:
        disk_usage_alert = "Error - Available disk space is less than 20% - " + str(d_free_pct)
        return disk_usage_alert
    else:
        return


# Report an error if available memory is less than 500MB
def check_avail_mem():
    values = psutil.virtual_memory() # virtual_memory return: 0=total,1=avail,2=% used,3=used,4=free,5=active,6=inactive
    avail_mem = int(values[1]/1048576)
    #avail_mem = 499           # Testing
    mem_alert = "Error - Available memory is less than 500MB - " + str(avail_mem)
    if avail_mem < 500:
        return mem_alert
    else:
        return


# Check if localhost resolves to '127.0.0.1'
def check_localhost():
    ip_address = socket.gethostbyname('localhost')      # gethostbyname() takes path param
    #ip_address = '192.0.0.1'        # Testing
    if ip_address != '127.0.0.1':
        localhost_alert = 'Error - localhost cannot be resolved to 127.0.0.1 - ' + str(ip_address)
        return localhost_alert
    else:
        return


# TODO: Create and Send Email via emails.generate_email(sender, receiver, subject, body, attachment)
def send_mail(check_return):
    sender = "automation@example.com"
    receiver = "chriswong@localhost"
    subject = check_return
    body = "Please check your system and resolve the issue as soon as possible."
    message = emails.generate_email(sender, receiver, subject, body)
    emails.send_email(message)


def main(argv):
    check_cpu_usage_return = check_cpu_usage()
    if check_cpu_usage_return != None:          # Only call send_mail() IF return is anything BUT None
        send_mail(check_cpu_usage_return)
        print(check_cpu_usage_return)

    check_disk_usage_return = check_disk_usage()
    if check_disk_usage_return != None:         # Only call send_mail() IF return is anything BUT None
        send_mail(check_disk_usage_return)
        print(check_disk_usage_return)        #print("available disk space below 20%")

    check_avail_mem_return = check_avail_mem()
    if check_avail_mem_return != None:          # Only call send_mail() IF return is anything BUT None
        send_mail(check_avail_mem_return)
        print(check_avail_mem_return)         #print("available memory is less than 500MB")

    check_localhost_return = check_localhost()
    if check_localhost_return != None:          # Only call send_mail() IF return is anything BUT None
        send_mail(check_localhost_return)
        print(check_localhost_return)         #print("localhost can't be resolved")





if __name__ == "__main__":
  main(sys.argv)


