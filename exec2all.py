#!/usr/bin/python

import subprocess
import threading
import time
import os

class MyThread(threading.Thread):
    def __init__(self,ip,username,password):
        super(MyThread,self).__init__()
        self.ip = ip
        self.username = username
    	self.password = password
	    #self.actioncmd = actioncmd
    def getdata(self):
    	cmd = "./cmd.exp %s %s %s %s &"%(self.ip,self.username,self.password,'\'sleep 5 && echo 1\'')
    	run_cmd = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        self.result = run_cmd.stdout.read()
        return self.result
    def get_result(self):
        return self.result 

def readcfg(p):
    cfgList = []
    with open(p,'r') as f:
        lineList = f.readlines()
    for line in lineList:
        if len(line.strip()) == 0 or line.strip()[0] == "#":
            continue
        cfgList.append(line)
    return cfgList
       
def main():
    st = time.time()
    actioncmd = 'ls'
    starttime = time.time()
    threads = []
    for msg in readcfg('./saegw.cfg'):
        msgList = msg.split()
        name,ip,username,password = msgList[0],msgList[1],msgList[2],msgList[3]
    	#print name,ip,username,password
    	t = MyThread(ip,username,password)
    	threads.append(t)
    	t.start()
    for t in threads:
        #t.join()
        print t.getdata()
    et = time.time()
    print "%sFinished [run time: %.2f]" % ( "-" * 40, et - st)
    
main()


