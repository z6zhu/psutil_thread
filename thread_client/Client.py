#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：client.py
import threading
import time
import socket
from time import sleep
import ConfigParser
import os
import sys
import psutil
import datetime
s = socket.socket()         # 创建 socket 对象

#host = socket.gethostname() # 获取本地主机名
#host="192.168.31.131"
#port = 12342                # 设置端口好

def get_ini():
    """ config file """
    config = ConfigParser.ConfigParser()
    start_f=open(cur_file_dir()+"/multi_thread.ini","rb")
    config.readfp(start_f)
    server_ip=config.get("server","ip")
    server_port=config.get("server","port")
    server_hostname=config.get("server","hostname")
    start_f.close()
    return server_ip,server_port,server_hostname
def cur_file_dir():
     path = sys.path[0]
     if os.path.isdir(path):
         return path
     elif os.path.isfile(path):
         return os.path.dirname(path)
#----------------------------------------
ps_cpu_per=psutil.cpu_times_percent(interval=1, percpu=False)

cpu_used=100-ps_cpu_per.idle
cpu_count=psutil.cpu_count()
#---------------------------------------
mem=psutil.virtual_memory()

mem_total=mem.total
mem_used=mem.percent
#----------------------------------
swap=psutil.swap_memory()

swap_total=swap.total
swap_used=swap.percent
#-----------------------------------
disk=psutil.disk_usage('/')

disk_total=disk.total
disk_used=disk.percent
#--------------------------------------
net=psutil.net_if_stats()
net_speed={}
for i in net.keys():
    net_speed.update({i:net[i].speed/8.0})

byte_net=psutil.net_io_counters(pernic=True)
net_byte={}
for i in byte_net.keys():
    net_byte.update({i:{"send":byte_net[i][0],"recv":byte_net[i][1]}})
#--------------------------------------
host,port,hostname=get_ini()
now=datetime.datetime.now()
dict={"cpu_used":cpu_used,"cpu_count":cpu_count,"mem_total":mem_total,"mem_used":mem_used,"swap_total":swap_total,"swap_used":swap_used,"disk_total":disk_total,"disk_used":disk_used,"net_byte":net_byte,"net_speed":net_speed,"hostname":hostname,"date":now}
log_f=open(cur_file_dir()+'/client_log.out','a')
log_f.write(str(dict)+"\n")
log_f.close()
s.connect((host,int(port)))
#while True:
#msg1=raw_input("input msg:")
s.send(str(dict))
print s.recv(1024)
s.close()
