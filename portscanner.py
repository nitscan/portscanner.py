#created by prashanthvarma ,for any query message me at www.facebook.com/prashanthvarmadomma
#you need to have nmap and python2.7

import subprocess
import os.path
import os
import optparse
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
if(os.path.isfile('/usr/lib/python2.7/nmap.py')):
                                                 import nmap
else:
     downfile=raw_input("[-]you don't have nmap installed in your python library \n[*]Do you want install nmap.py file ? [y/n]")
     if (downfile=='y'):
                        url='wget '+'http://xael.org/norman/python/python-nmap/python-nmap-0.1.4.tar.gz'
                        p=subprocess.Popen(url, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                        for line in p.stdout.readlines():
				                         print bcolors.OKGREEN+line,
		        retval = p.wait()
                        
		        if(os.path.isfile('python-nmap-0.1.4.tar.gz')):
				                                       cmd='tar -zxvf python-nmap-0.1.4.tar.gz '
				                                       c=subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
				        
					                               for line in c.stdout.readlines():
				                                                                        print bcolors.OKGREEN+line,
				                                       retval = c.wait()
				        
				                                       os.system('sudo cp python-nmap-0.1.4/nmap/nmap.py /usr/lib/python2.7/')
								       if(os.path.isfile('/usr/lib/python2.7/nmap.py')):
															print "[+] nmap installed run program again to scan network "
                                                                                                                        import nmap 					                                    
 
                        
     if(downfile=='n'):
                           exit(0)
 

def scan(h,p):
              nm=nmap.PortScanner()
              nm.scan(h,p)
              s=nm[h]['tcp'][int(p)]['state']
              print bcolors.OKGREEN+"[*] "+h+" tcp / "+p+" "+s
             
                          
def main():
           opt=optparse.OptionParser('USAGE: \n -t <target host> -p <target port> -a <to scan all ports [Y/N]>')
           opt.add_option('-t',dest='tgt',type='string',help='specify target host')
           opt.add_option('-p',dest='port',type='string',help='specify target ports with commas')
           opt.add_option('-a',dest='allports',type='string',help='specify to scan all ports')
           (options,args)=opt.parse_args()
           tgt=options.tgt
           ports=str(options.port).split(',')
           allports=options.allports
           if (tgt==None) | (allports=='N'):
                                                             print opt.usage
					                     exit(0)
           if (allports=='Y'):
                              for ap in range(1,1000):
                                                           ap=str(ap)
                                                           print "scaning port no : "+ap+"/";
						           scan(tgt,ap)
                                                           
                              print bcolors.ENDC+"[+] scan ended";                                       
           else :
                 for port in ports:
                                   print "scanning port no :"+port+"/";
                                   scan(tgt,port)
                 print bcolors.ENDC+"[+] scan ended";                   
                                    
if __name__=='__main__':
                       main()
                                           
