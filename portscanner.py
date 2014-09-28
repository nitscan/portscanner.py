#created by prashanthvarma ,for any query message me at www.facebook.com/prashanthvarmadomma

import subprocess
import os.path
import os
import optparse
if(os.path.isfile('/usr/lib/python2.7/nmap.py')):
                                                 import nmap
else:
     downfile=raw_input("[-]you don't have nmap installed in your python library \n[*]Do you want install nmap.py file ? [y/n]")
     if (downfile=='y'):
                        url='wget '+'http://xael.org/norman/python/python-nmap/python-nmap-0.1.4.tar.gz'
                        p=subprocess.Popen(url, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                        for line in p.stdout.readlines():
				                         print line,
		        retval = p.wait()
                        
		        if(os.path.isfile('python-nmap-0.1.4.tar.gz')):
				                                       cmd='tar -zxvf python-nmap-0.1.4.tar.gz '
				                                       c=subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
				        
					                               for line in c.stdout.readlines():
				                                                                        print line,
				                                       retval = c.wait()
				        
				                                       os.system('sudo cp python-nmap-0.1.4/nmap/nmap.py /usr/lib/python2.7/')
								       if(os.path.isfile('/usr/lib/python2.7/nmap.py')):
															print "[+] nmap installed scanning network "
                                                                                                        		import nmap			                                    
 
                        
     if(downfile=='n'):
                           exit(0)
 

def scan(h,p):
              nm=nmap.PortScanner()
              nm.scan(h,p)
              s=nm[h]['tcp'][int(p)]['state']
              print "[*] "+h+" tcp / "+p+" "+s
                          
def main():
           opt=optparse.OptionParser('USAGE: \n -t <target host> -p <target port>')
           opt.add_option('-t',dest='tgt',type='string',help='specify target host')
           opt.add_option('-p',dest='port',type='string',help='specify target ports with commas')
           (options,args)=opt.parse_args()
           tgt=options.tgt
           ports=str(options.port).split(',')
           if (tgt==None) | (ports[0]==None):
                                             print opt.usage
					     exit(0)
           for port in ports:
                             scan(tgt,port)
if __name__=='__main__':
                       main()
                                           
