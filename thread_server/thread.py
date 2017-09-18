#/usr/bin/python
# -*- coding: UTF-8 -*- 
import threading
import time
import socket
from time import sleep
import ConfigParser
import os
import sys
import psutil

class myThread (threading.Thread):
    def __init__(self, threadID, name, counter,c,addr):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
	self.c=c
	self.addr=addr
    def run(self):
        
	print "Starting " + self.name
        #threadLock.acquire()
        #while True:
	    
        stri=self.c.recv(2048)
        print stri,"-------"
        with open('thread.out','a') as f:
	    f.write(stri+'\n')
        f.close()
            #threadLock.release()
        self.c.close()
        print "-----end------------------"
	    #except socket.error,e:
def print_time(threadName, delay, counter):
    while counter:
        time.sleep(delay)
        print "%s: %s" % (threadName, time.ctime(time.time()))
        counter -= 1

def get_ini():
    """ config file """
    config = ConfigParser.ConfigParser()
    start_f=open(cur_file_dir()+"/multi_thread.ini","rb")
    config.readfp(start_f)
    server_ip=config.get("server","ip")
    server_port=config.get("server","port")
    start_f.close()
    return server_ip,server_port
def cur_file_dir():
     path = sys.path[0]
     if os.path.isdir(path):
         return path
     elif os.path.isfile(path):
         return os.path.dirname(path)

#if __name__=="__main__":
 
#threadLock = threading.Lock()
#threads = []

s = socket.socket()         # 创建 socket 对象
#host = socket.gethostname() # 获取本地主机名i
host,port=get_ini()
#s.settimeout(5)
s.bind((host, int(port)))        # 绑定端口
count=0
s.listen(5)                 # 等待客户端连接
#while True:
#c, addr = s.accept()     # 建立客户端连接。
while True:
    c, addr = s.accept()     # 建立客户端连接。
    print c
    if c and addr:
    	count+=1
    	thread_count="thread"+str(count)
        thr=myThread(count, thread_count,2,c,addr).start()
        #threads.append(thr)
    	# 等待所有线程完成
    	#for t in threads:
        #    t.join()
    	#print "Exiting Main Thread"
s.close()
