#coding=utf-8
#!C:\Program****\Anaconda2
import os,sys,StringIO
import time

# 杀掉kds进程（system里面的、lib里面的）
def kill_all():
    pre = "adb shell su -c"
    cmd = "%s '%s'"%(pre, r"ps")
    r = os.popen(cmd)
    text = r.read()
    buf = StringIO.StringIO(text)
    find_string = r't***'
    ps_num = []
    #get ps number
    for line in buf.readlines():
        if find_string in line:
            spp = line.split(' ')
            ps_num.append(spp[6])

    # kill t*** ps
    print "there are %d t*** threads" % (len(ps_num))
    for i in xrange(len(ps_num)):
        temp_cmd = r"kill -9 %s"%(ps_num[i])
        cmd = "%s '%s'"%(pre, temp_cmd)
        print cmd
        r = os.popen(cmd)

        
    
    os.popen("exit")

    
def execCmd(str):
    cmd = str
    r = os.popen(cmd)
    text = r.read()
    buf = StringIO.StringIO(text)
    for line in buf.readlines():
        print line
    
    
def execADBCmd(str):
    pre = "adb shell su -c"
    cmd = "%s '%s'"%(pre, str)
    r = os.popen(cmd)
    text = r.read()
    buf = StringIO.StringIO(text)
    for line in buf.readlines():
        print line
    os.popen("exit")
    
      
def kill_kernel():
    print "befor rmxmod:"
    execADBCmd(r"lsmod")
    execADBCmd(r"rmmod test1")
    execADBCmd(r"rmmod test2")
    execADBCmd(r"rmmod xcore")
    print "after rmxmod:"
    execADBCmd(r"lsmod xcore")
    
def start_xmod():
    while True:
        print "enter 1,clean the environment,enter 2,no clean!!,enter 'q' to quit"
        cat = raw_input()
        if(cat == str(1)):
            #replaceKO()    
            kill_all()
             
            print "kill tps is done,/****/****-lib/tps is romoving..."
            execADBCmd(r"rm -rf  /****/****-lib/tps")
            print "/****/****-lib/tps is romoved!! /****/local/tmp/xmoddaemon is removing..."
            kill_kernel()
            choosedaemon()
            break
            #execADBCmd(r"rm -rf  /****/local/tmp/xmoddaemon")
            #execADBCmd(r"rm /****/****-lib/tps/pref/pmgr")
            #print "/****/local/tmp/xmoddaemon is romoved!!!,next is star xmod..."
        elif(cat == str(2)):
            #kill_all()
            #print "kill tps process,but not the file!!!"
            choosedaemon()
            break
        elif (cat == 'q'):
            break
        else:
            print "please enter 1,2..\n"
            
        print "start  :"
        
   


def choosedaemon():
     while True:
        print ("\nChose daemon:\n"
        "Enter 1,push <(1.2.3);Enter 2,push (1.2.3)\n"
        "Enter 3,push (1.2.4);Enter 4,XMod-Daemon_V1.3.1\n"
        "Enter 5,XMod-Daemon_V1.3.1_c29;Enter 6,xmoddaemon_1.3.2_c32\n"
        "Enter 7,push xmoddaemon_release;Enter 'q' to quit!\n")
        switch = raw_input()
        if(switch == str(1)):
            print "you chose is the <(1.2.3) xmoddaemon!!!!"
            execCmd(r"adb push xmoddaemon /****/local/tmp/xmoddaemon")
            pushxmod()
            break
        elif(switch == str(2)):
            print "your chose is the 1.2.3 xmoddaemon!!!!"
            execCmd(r"adb push t***aemon /****/local/tmp/xmoddaemon")
            pushxmod()
            break
        elif(switch == str(3)):
            print "your chose is the 1.2.4 xmoddaemon!!!!"
            execCmd(r"adb push xmoddaemon_1.2.4 /****/local/tmp/xmoddaemon")
            pushxmod()
            break
        elif(switch == str(4)):
            print "your chose is the XMod-Daemon_V1.3.1 xmoddaemon!!!!"
            execCmd(r"adb push XMod-Daemon_V1.3.1 /****/local/tmp/xmoddaemon")
            pushxmod()
            break
        elif(switch == str(5)):
            print "your chose is xmoddaemon_1.3.1_c29 xmoddaemon!!!!"
            execCmd(r"adb push xmoddaemon_1.3.1_c29 /****/local/tmp/xmoddaemon")
            pushxmod()
            break
        elif(switch == str(6)):
            print "your chose is xmoddaemon_1.3.2_c32 xmoddaemon!!!!"
            execCmd(r"adb push xmoddaemon_1.3.2_c32 /****/local/tmp/xmoddaemon")
            pushxmod()
            break
            #xmoddaemon_release
        elif(switch == str(7)):
            print "your chose is the xmoddaemon_release xmoddaemon!!!!"
            execCmd(r"adb push xmoddaemon_release /****/local/tmp/xmoddaemon")
            pushxmod()
            break
        elif (switch == 'q'):
            break
        else:
            print "please enter 1,2,3!!!"
            
def pushxmod():
    print "push daemon succeed,daemon is starting..."
    execADBCmd(r"chmod 777 /****/local/tmp/xmoddaemon")
    execADBCmd(r"./****/local/tmp/xmoddaemon")
    #execADBCmd(r"ps | grep t***")

    
def replaceKO():
    id = "612"
    
    execCmd(r"adb push out/test_auto.zip /****/local/tmp")
    execADBCmd(r"ls /****/****-lib/tps/  | grep test")
    execADBCmd(r"rm /****/****-lib/tps/patches/patch_" + id)
    execADBCmd(r"ls /****/****-lib/tps/patches")
    execADBCmd(r"mv  /****/local/tmp/test_auto.zip /****/****-lib/tps/patches/patch_" + id)
    execADBCmd(r"ls /****/****-lib/tps/patches")
    




def run():

        start_xmod()
        #execADBCmd(r"ps | grep t***")

def bigRun():
    for i in range(0, 4):
        print i
        start_xmod()
        
#execCmd(r"java -jar patch.jar -PatchPath=xmod2 -OutputPath=out -UpdateUser=miawuKernel -ModId=0 -ModName=report**** -Version=1.0.2 -Verified=1 -InterfaceType=1 -ExploitType=3 -Type=4 -Status=1 -Weight=1000 -ChannelGroupId=10086 -PolicyPath=policy.txt")  
run()
#bigRun()
    
    